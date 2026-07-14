"""
=========================================================
KAI Smart Money AI

Institutional Order Block Engine

candidate_detector.py

Detect institutional Order Block candidates.

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations

from typing import List

import pandas as pd

from engines.common.candle_utils import (
    get_candle,
    is_bullish,
    is_bearish,
    candle_body,
    candle_range,
)

from .models import (
    OrderBlockCandidate,
)

from .displacement import (
    find_displacement,
)


# ==========================================================
# BUILD CANDIDATE
# ==========================================================

def build_candidate(
    candle,
    index: int,
    direction: str,
    displacement,
) -> OrderBlockCandidate:
    """
    Build Order Block candidate object.
    """

    candidate = OrderBlockCandidate()

    candidate.index = index

    candidate.direction = direction

    candidate.time = candle.get("time")

    candidate.open = float(candle["open"])

    candidate.high = float(candle["high"])

    candidate.low = float(candle["low"])

    candidate.close = float(candle["close"])

    candidate.body = candle_body(candle)

    candidate.range = candle_range(candle)

    candidate.displacement = displacement

    candidate.score = 0.0

    candidate.valid = False

    candidate.reason = []

    return candidate


# ==========================================================
# BULLISH CANDIDATE
# ==========================================================

def detect_bullish_candidate(
    candles: pd.DataFrame,
    index: int,
    market_structure=None,
    liquidity=None,
    fair_value_gaps=None,
):
    """
    Last bearish candle before bullish displacement.
    """

    candle = get_candle(
        candles,
        index,
    )

    if not is_bearish(candle):
        return None

    displacement = find_displacement(
        candles,
        index + 1,
        market_structure,
        liquidity,
        fair_value_gaps,
    )

    if displacement is None:
        return None

    if displacement.direction != "bullish":
        return None

    return build_candidate(

        candle,

        index,

        "bullish",

        displacement,

    )


# ==========================================================
# BEARISH CANDIDATE
# ==========================================================

def detect_bearish_candidate(
    candles: pd.DataFrame,
    index: int,
    market_structure=None,
    liquidity=None,
    fair_value_gaps=None,
):
    """
    Last bullish candle before bearish displacement.
    """

    candle = get_candle(
        candles,
        index,
    )

    if not is_bullish(candle):
        return None

    displacement = find_displacement(
        candles,
        index + 1,
        market_structure,
        liquidity,
        fair_value_gaps,
    )

    if displacement is None:
        return None

    if displacement.direction != "bearish":
        return None

    return build_candidate(

        candle,

        index,

        "bearish",

        displacement,

    )

# ==========================================================
# FIND BULLISH CANDIDATES
# ==========================================================

def find_bullish_candidates(
    candles: pd.DataFrame,
    market_structure=None,
    liquidity=None,
    fair_value_gaps=None,
) -> List[OrderBlockCandidate]:
    """
    Scan for bullish Order Block candidates.
    """

    candidates = []

    for index in range(len(candles) - 1):

        candidate = detect_bullish_candidate(
            candles,
            index,
            market_structure,
            liquidity,
            fair_value_gaps,
        )

        if candidate is None:
            continue

        candidates.append(candidate)

    return candidates


# ==========================================================
# FIND BEARISH CANDIDATES
# ==========================================================

def find_bearish_candidates(
    candles: pd.DataFrame,
    market_structure=None,
    liquidity=None,
    fair_value_gaps=None,
) -> List[OrderBlockCandidate]:
    """
    Scan for bearish Order Block candidates.
    """

    candidates = []

    for index in range(len(candles) - 1):

        candidate = detect_bearish_candidate(
            candles,
            index,
            market_structure,
            liquidity,
            fair_value_gaps,
        )

        if candidate is None:
            continue

        candidates.append(candidate)

    return candidates


# ==========================================================
# REMOVE DUPLICATES
# ==========================================================

def remove_duplicate_candidates(
    candidates: List[OrderBlockCandidate],
) -> List[OrderBlockCandidate]:
    """
    Remove duplicate Order Blocks using
    (index, direction) as the unique key.
    """

    unique = {}

    for candidate in candidates:

        key = (
            candidate.index,
            candidate.direction,
        )

        if key not in unique:
            unique[key] = candidate
            continue

        if (
            candidate.displacement.score >
            unique[key].displacement.score
        ):
            unique[key] = candidate

    return sorted(
        unique.values(),
        key=lambda x: x.index,
    )


# ==========================================================
# FILTER BY DISPLACEMENT SCORE
# ==========================================================

def filter_candidates(
    candidates: List[OrderBlockCandidate],
    minimum_score: float = 65.0,
) -> List[OrderBlockCandidate]:
    """
    Keep only candidates backed by
    strong institutional displacement.
    """

    return [

        candidate

        for candidate in candidates

        if (
            candidate.displacement
            and
            candidate.displacement.score >= minimum_score
        )

    ]


# ==========================================================
# MAIN DETECTOR
# ==========================================================

def find_candidate_order_blocks(
    candles: pd.DataFrame,
    market_structure=None,
    liquidity=None,
    fair_value_gaps=None,
) -> List[OrderBlockCandidate]:
    """
    Detect all Order Block candidates.
    """

    bullish = find_bullish_candidates(
        candles,
        market_structure,
        liquidity,
        fair_value_gaps,
    )

    bearish = find_bearish_candidates(
        candles,
        market_structure,
        liquidity,
        fair_value_gaps,
    )

    candidates = bullish + bearish

    candidates = remove_duplicate_candidates(
        candidates,
    )

    candidates = filter_candidates(
        candidates,
    )

    return candidates


# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "build_candidate",

    "detect_bullish_candidate",

    "detect_bearish_candidate",

    "find_bullish_candidates",

    "find_bearish_candidates",

    "remove_duplicate_candidates",

    "filter_candidates",

    "find_candidate_order_blocks",

]