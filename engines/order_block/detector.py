"""
=========================================================
KAI Smart Money AI

Institutional Order Block Engine

detector.py

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations

import pandas as pd

from .candidate_detector import (
    find_candidate_order_blocks,
)

from .validator import (
    validate_candidates,
)

from .scorer import (
    score_candidates,
)

from .lifecycle import (
    update_order_blocks,
)

from .models import (
    OrderBlock,
)


# ==========================================================
# CONVERT CANDIDATE
# ==========================================================

def candidate_to_order_block(
    candidate,
) -> OrderBlock:
    """
    Convert validated candidate into
    a final OrderBlock object.
    """

    order_block = OrderBlock()

    order_block.index = candidate.index

    order_block.time = candidate.time

    order_block.direction = candidate.direction

    order_block.open = candidate.open

    order_block.high = candidate.high

    order_block.low = candidate.low

    order_block.close = candidate.close

    order_block.body = candidate.body

    order_block.range = candidate.range

    order_block.score = candidate.score

    order_block.reason = list(candidate.reason)

    order_block.displacement = candidate.displacement

    order_block.valid = candidate.valid

    order_block.status = "fresh"

    order_block.mitigated = False

    order_block.invalidated = False

    order_block.retests = 0

    return order_block


# ==========================================================
# BUILD ORDER BLOCKS
# ==========================================================

def build_order_blocks(
    candidates,
):
    """
    Convert candidates to Order Blocks.
    """

    order_blocks = []

    for candidate in candidates:

        order_blocks.append(

            candidate_to_order_block(
                candidate
            )

        )

    return order_blocks


# ==========================================================
# DETECT ORDER BLOCKS
# ==========================================================

def detect_order_blocks(
    candles: pd.DataFrame,
    market_structure=None,
    liquidity=None,
    fair_value_gaps=None,
):
    """
    Complete Order Block detection pipeline.

    Flow:

    Candles
       |
       v
    Candidate Detection
       |
       v
    Validation
       |
       v
    Scoring
       |
       v
    Conversion
       |
       v
    Lifecycle Update
       |
       v
    Final Order Blocks
    """

    if candles is None or candles.empty:
        return []


    # ----------------------------------
    # 1. Find Candidates
    # ----------------------------------

    candidates = find_candidate_order_blocks(

        candles,

        market_structure,

        liquidity,

        fair_value_gaps,

    )


    if not candidates:
        return []


    # ----------------------------------
    # 2. Validate Candidates
    # ----------------------------------

    validated = validate_candidates(
        candidates,
    )


    if not validated:
        return []


    # ----------------------------------
    # 3. Score Candidates
    # ----------------------------------

    scored = score_candidates(
        validated,
    )


    # ----------------------------------
    # 4. Convert
    # ----------------------------------

    order_blocks = build_order_blocks(
        scored,
    )


    # ----------------------------------
    # 5. Lifecycle
    # ----------------------------------

    order_blocks = update_order_blocks(

        order_blocks,

        candles,

    )


    # ----------------------------------
    # 6. Highest quality first
    # ----------------------------------

    order_blocks.sort(

        key=lambda x: x.score,

        reverse=True,

    )


    return order_blocks



# ==========================================================
# FILTER VALID ORDER BLOCKS
# ==========================================================

def filter_active_blocks(
    order_blocks,
):
    """
    Return only active blocks.
    """

    return [

        block

        for block in order_blocks

        if not block.invalidated

    ]



# ==========================================================
# FILTER FRESH BLOCKS
# ==========================================================

def filter_fresh_blocks(
    order_blocks,
):
    """
    Return only fresh blocks.
    """

    return [

        block

        for block in order_blocks

        if block.status == "fresh"

    ]



# ==========================================================
# BEST ORDER BLOCK
# ==========================================================

def best_order_block(
    order_blocks,
):
    """
    Return strongest institutional block.
    """

    if not order_blocks:
        return None


    return max(

        order_blocks,

        key=lambda x: x.score,

    )



# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "candidate_to_order_block",

    "build_order_blocks",

    "detect_order_blocks",

    "filter_active_blocks",

    "filter_fresh_blocks",

    "best_order_block",

]