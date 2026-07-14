"""
=========================================================
KAI Smart Money AI

Institutional Order Block Engine

lifecycle.py

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations

from typing import List

import pandas as pd

from engines.common.candle_utils import get_candle

from .models import OrderBlock


# ==========================================================
# MITIGATION
# ==========================================================

def is_mitigated(
    order_block: OrderBlock,
    candles: pd.DataFrame,
) -> bool:
    """
    Check whether price has mitigated
    the Order Block.
    """

    start = order_block.index + 1

    for i in range(start, len(candles)):

        candle = get_candle(candles, i)

        # Bullish Order Block

        if order_block.direction == "bullish":

            if candle["low"] <= order_block.high:

                return True

        # Bearish Order Block

        else:

            if candle["high"] >= order_block.low:

                return True

    return False


# ==========================================================
# RETEST
# ==========================================================

def count_retests(
    order_block: OrderBlock,
    candles: pd.DataFrame,
) -> int:
    """
    Count Order Block retests.
    """

    count = 0

    start = order_block.index + 1

    for i in range(start, len(candles)):

        candle = get_candle(candles, i)

        if order_block.direction == "bullish":

            if (

                candle["low"] <= order_block.high
                and
                candle["high"] >= order_block.low

            ):

                count += 1

        else:

            if (

                candle["high"] >= order_block.low
                and
                candle["low"] <= order_block.high

            ):

                count += 1

    return count


# ==========================================================
# INVALIDATION
# ==========================================================

def is_invalidated(
    order_block: OrderBlock,
    candles: pd.DataFrame,
) -> bool:
    """
    Check whether Order Block
    has failed.
    """

    start = order_block.index + 1

    for i in range(start, len(candles)):

        candle = get_candle(candles, i)

        if order_block.direction == "bullish":

            if candle["close"] < order_block.low:

                return True

        else:

            if candle["close"] > order_block.high:

                return True

    return False


# ==========================================================
# STATUS
# ==========================================================

def update_status(
    order_block: OrderBlock,
    candles: pd.DataFrame,
) -> OrderBlock:
    """
    Update lifecycle state.
    """

    order_block.retests = count_retests(
        order_block,
        candles,
    )

    order_block.mitigated = is_mitigated(
        order_block,
        candles,
    )

    order_block.invalidated = is_invalidated(
        order_block,
        candles,
    )

    if order_block.invalidated:

        order_block.status = "invalid"

    elif order_block.mitigated:

        order_block.status = "mitigated"

    elif order_block.retests > 0:

        order_block.status = "tested"

    else:

        order_block.status = "fresh"

    return order_block


# ==========================================================
# UPDATE MANY
# ==========================================================

def update_order_blocks(
    order_blocks: List[OrderBlock],
    candles: pd.DataFrame,
) -> List[OrderBlock]:
    """
    Update lifecycle of all
    Order Blocks.
    """

    updated = []

    for order_block in order_blocks:

        updated.append(

            update_status(
                order_block,
                candles,
            )

        )

    return updated


# ==========================================================
# ACTIVE
# ==========================================================

def active_order_blocks(
    order_blocks: List[OrderBlock],
) -> List[OrderBlock]:
    """
    Return active Order Blocks.
    """

    return [

        ob

        for ob in order_blocks

        if not ob.invalidated

    ]


# ==========================================================
# FRESH
# ==========================================================

def fresh_order_blocks(
    order_blocks: List[OrderBlock],
) -> List[OrderBlock]:
    """
    Return fresh Order Blocks.
    """

    return [

        ob

        for ob in order_blocks

        if ob.status == "fresh"

    ]


# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "is_mitigated",

    "count_retests",

    "is_invalidated",

    "update_status",

    "update_order_blocks",

    "active_order_blocks",

    "fresh_order_blocks",

]