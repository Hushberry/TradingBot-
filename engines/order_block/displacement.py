"""
=========================================================
KAI Smart Money AI

Institutional Order Block Engine

displacement.py

Institutional Displacement Detection

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations

from typing import Optional

import pandas as pd

from engines.common.candle_utils import (
    get_candle,
    candle_body,
    candle_range,
    body_ratio,
    is_bullish,
)

from engines.common.math_utils import (
    average,
    atr,
    clamp,
)

from .models import Displacement


# ==========================================================
# BODY STRENGTH
# ==========================================================

def calculate_body_strength(candle) -> float:
    """
    Returns body strength (0-100).
    """

    return clamp(
        body_ratio(candle) * 100.0,
        0.0,
        100.0,
    )


# ==========================================================
# RANGE EXPANSION
# ==========================================================

def calculate_expansion(
    current,
    previous,
) -> float:
    """
    Candle range expansion.
    """

    previous_range = candle_range(previous)

    if previous_range <= 0:
        return 0.0

    return candle_range(current) / previous_range


# ==========================================================
# DISPLACEMENT DISTANCE
# ==========================================================

def calculate_distance(
    current,
    previous,
) -> float:

    return abs(

        float(current["close"])

        -

        float(previous["close"])

    )


# ==========================================================
# DISPLACEMENT VELOCITY
# ==========================================================

def calculate_velocity(
    current,
    previous,
) -> float:

    previous_body = candle_body(previous)

    if previous_body <= 0:
        return 0.0

    return calculate_distance(
        current,
        previous,
    ) / previous_body


# ==========================================================
# DISPLACEMENT ACCELERATION
# ==========================================================

def calculate_acceleration(
    candles: pd.DataFrame,
    index: int,
) -> float:

    if index < 2:
        return 0.0

    c0 = get_candle(candles, index)

    c1 = get_candle(candles, index - 1)

    c2 = get_candle(candles, index - 2)

    velocity1 = calculate_velocity(c1, c2)

    velocity2 = calculate_velocity(c0, c1)

    return max(

        velocity2 - velocity1,

        0.0,

    )


# ==========================================================
# ATR RATIO
# ==========================================================

def calculate_atr_ratio(
    candles: pd.DataFrame,
    index: int,
    period: int = 14,
) -> float:
    """
    Current candle range divided by ATR.
    """

    atr_values = atr(
        candles,
        period,
    )

    current_atr = atr_values.iloc[index]

    if pd.isna(current_atr):
        return 0.0

    current = get_candle(
        candles,
        index,
    )

    rng = candle_range(current)

    if current_atr <= 0:
        return 0.0

    return rng / current_atr


# ==========================================================
# VOLUME RATIO
# ==========================================================

def calculate_volume_ratio(
    candles: pd.DataFrame,
    index: int,
    lookback: int = 20,
) -> float:

    if "tick_volume" not in candles.columns:
        return 1.0

    start = max(
        0,
        index - lookback,
    )

    avg_volume = average(

        candles[
            "tick_volume"
        ].iloc[start:index]

    )

    if avg_volume <= 0:
        return 1.0

    current_volume = float(

        candles.iloc[index][
            "tick_volume"
        ]

    )

    return current_volume / avg_volume


# ==========================================================
# IMPULSE SCORE
# ==========================================================

def calculate_impulse_score(
    candles: pd.DataFrame,
    index: int,
) -> float:

    current = get_candle(
        candles,
        index,
    )

    previous = get_candle(
        candles,
        index - 1,
    )

    score = 0.0

    score += calculate_body_strength(
        current
    ) * 0.25

    score += min(

        calculate_expansion(
            current,
            previous,
        ),

        3.0,

    ) * 10

    score += min(

        calculate_velocity(
            current,
            previous,
        ),

        3.0,

    ) * 8

    score += min(

        calculate_acceleration(
            candles,
            index,
        ),

        2.0,

    ) * 6

    score += min(

        calculate_atr_ratio(
            candles,
            index,
        ),

        3.0,

    ) * 10

    score += min(

        calculate_volume_ratio(
            candles,
            index,
        ),

        3.0,

    ) * 6

    return clamp(

        score,

        0.0,

        100.0,

    )


# ==========================================================
# MARKET STRUCTURE
# ==========================================================

def has_bos(
    index: int,
    market_structure: dict | None,
) -> bool:
    """
    Check whether a BOS occurred at or before index.
    """

    if not market_structure:
        return False

    events = market_structure.get("events", [])

    for event in events:

        if event.get("event") != "BOS":
            continue

        if event.get("index", -1) <= index:
            return True

    return False


def has_choch(
    index: int,
    market_structure: dict | None,
) -> bool:
    """
    Check whether a CHoCH occurred.
    """

    if not market_structure:
        return False

    events = market_structure.get("events", [])

    for event in events:

        if event.get("event") != "CHoCH":
            continue

        if event.get("index", -1) <= index:
            return True

    return False


# ==========================================================
# LIQUIDITY
# ==========================================================

def has_liquidity_sweep(
    index: int,
    liquidity: dict | None,
) -> bool:
    """
    Check liquidity sweep.
    """

    if not liquidity:
        return False

    sweeps = liquidity.get(
        "sweeps",
        [],
    )

    for sweep in sweeps:

        if sweep.get(
            "index",
            -1,
        ) == index:

            return True

    return False


# ==========================================================
# FAIR VALUE GAP
# ==========================================================

def creates_fvg(
    index: int,
    fair_value_gaps: list | None,
) -> bool:
    """
    Check whether displacement created an FVG.
    """

    if not fair_value_gaps:
        return False

    for gap in fair_value_gaps:

        if gap.get(
            "created_index",
            -1,
        ) == index:

            return True

    return False


# ==========================================================
# INSTITUTIONAL CONFIRMATION
# ==========================================================

def institutional_confirmation_score(
    index: int,
    market_structure,
    liquidity,
    fair_value_gaps,
) -> float:
    """
    Institutional confluence score.
    """

    score = 0.0

    if has_bos(
        index,
        market_structure,
    ):
        score += 35

    if has_choch(
        index,
        market_structure,
    ):
        score += 15

    if has_liquidity_sweep(
        index,
        liquidity,
    ):
        score += 25

    if creates_fvg(
        index,
        fair_value_gaps,
    ):
        score += 25

    return min(
        score,
        100.0,
    )


# ==========================================================
# VALIDATION
# ==========================================================

def validate_displacement(
    candles,
    index,
    market_structure=None,
    liquidity=None,
    fair_value_gaps=None,
    minimum_score=65,
):
    """
    Validate institutional displacement.
    """

    impulse = calculate_impulse_score(
        candles,
        index,
    )

    institutional = institutional_confirmation_score(

        index,

        market_structure,

        liquidity,

        fair_value_gaps,

    )

    final_score = (
        impulse * 0.60
        +
        institutional * 0.40
    )

    return final_score >= minimum_score


# ==========================================================
# DETECT DISPLACEMENT
# ==========================================================

def detect_displacement(
    candles,
    index,
    market_structure=None,
    liquidity=None,
    fair_value_gaps=None,
):
    """
    Detect one institutional displacement.
    """

    if index < 1:
        return None

    if not validate_displacement(
        candles,
        index,
        market_structure,
        liquidity,
        fair_value_gaps,
    ):
        return None

    current = get_candle(
        candles,
        index,
    )

    previous = get_candle(
        candles,
        index - 1,
    )

    displacement = Displacement()

    displacement.valid = True

    displacement.direction = (
        "bullish"
        if is_bullish(current)
        else "bearish"
    )

    displacement.start_index = index - 1

    displacement.end_index = index

    displacement.distance = calculate_distance(
        current,
        previous,
    )

    displacement.expansion = calculate_expansion(
        current,
        previous,
    )

    displacement.velocity = calculate_velocity(
        current,
        previous,
    )

    displacement.acceleration = calculate_acceleration(
        candles,
        index,
    )

    displacement.atr_ratio = calculate_atr_ratio(
        candles,
        index,
    )

    displacement.volume_ratio = calculate_volume_ratio(
        candles,
        index,
    )

    displacement.impulse_score = calculate_impulse_score(
        candles,
        index,
    )

    displacement.confirmation_score = (
        institutional_confirmation_score(
            index,
            market_structure,
            liquidity,
            fair_value_gaps,
        )
    )

    displacement.score = (
        displacement.impulse_score * 0.60
        +
        displacement.confirmation_score * 0.40
    )

    displacement.bos_confirmed = has_bos(
        index,
        market_structure,
    )

    displacement.choch_confirmed = has_choch(
        index,
        market_structure,
    )

    displacement.liquidity_confirmed = (
        has_liquidity_sweep(
            index,
            liquidity,
        )
    )

    displacement.fvg_confirmed = creates_fvg(
        index,
        fair_value_gaps,
    )

    displacement.strength = displacement.score

    displacement.reason = []

    if displacement.bos_confirmed:
        displacement.reason.append(
            "Break of Structure"
        )

    if displacement.choch_confirmed:
        displacement.reason.append(
            "Change of Character"
        )

    if displacement.liquidity_confirmed:
        displacement.reason.append(
            "Liquidity Sweep"
        )

    if displacement.fvg_confirmed:
        displacement.reason.append(
            "Fair Value Gap"
        )

    return displacement


# ==========================================================
# FIND ONE
# ==========================================================

def find_displacement(
    candles,
    index,
    market_structure=None,
    liquidity=None,
    fair_value_gaps=None,
):
    """
    Public wrapper.
    """

    return detect_displacement(
        candles,
        index,
        market_structure,
        liquidity,
        fair_value_gaps,
    )


# ==========================================================
# FIND ALL
# ==========================================================

def find_all_displacements(
    candles,
    market_structure=None,
    liquidity=None,
    fair_value_gaps=None,
):
    """
    Detect every displacement.
    """

    displacements = []

    for index in range(1, len(candles)):

        displacement = detect_displacement(
            candles,
            index,
            market_structure,
            liquidity,
            fair_value_gaps,
        )

        if displacement:

            displacements.append(
                displacement
            )

    return displacements


# ==========================================================
# FILTERS
# ==========================================================

def bullish_displacements(
    displacements,
):

    return [
        d
        for d in displacements
        if d.direction == "bullish"
    ]


def bearish_displacements(
    displacements,
):

    return [
        d
        for d in displacements
        if d.direction == "bearish"
    ]


def strongest_displacement(
    displacements,
):

    if not displacements:
        return None

    return max(
        displacements,
        key=lambda x: x.score,
    )


# ==========================================================
# STATISTICS
# ==========================================================

def displacement_statistics(
    displacements,
):
    """
    Summary statistics.
    """

    if not displacements:

        return {

            "count": 0,

            "average_score": 0,

            "highest_score": 0,

            "bullish": 0,

            "bearish": 0,

        }

    scores = [
        d.score
        for d in displacements
    ]

    return {

        "count": len(displacements),

        "average_score": (
            sum(scores) / len(scores)
        ),

        "highest_score": max(scores),

        "bullish": len(
            bullish_displacements(
                displacements
            )
        ),

        "bearish": len(
            bearish_displacements(
                displacements
            )
        ),

    }


# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "detect_displacement",

    "find_displacement",

    "find_all_displacements",

    "bullish_displacements",

    "bearish_displacements",

    "strongest_displacement",

    "displacement_statistics",

]