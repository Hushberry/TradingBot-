"""
=========================================================
KAI Smart Money AI

Fair Value Gap Engine

utils.py

FVG Calculation Utilities

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations

import pandas as pd


from engines.common.candle_utils import (
    get_candle,
    candle_range,
)



# ==========================================================
# GAP SIZE
# ==========================================================

def calculate_gap_size(
    top: float,
    bottom: float,
) -> float:
    """
    Calculate FVG size.
    """

    return abs(
        top - bottom
    )



# ==========================================================
# GAP PERCENTAGE
# ==========================================================

def calculate_gap_percent(
    gap_size: float,
    price: float,
) -> float:
    """
    Calculate gap percentage.
    """

    if price <= 0:
        return 0.0

    return (
        gap_size / price
    )



# ==========================================================
# BULLISH FVG CHECK
# ==========================================================

def is_bullish_fvg(
    candles: pd.DataFrame,
    index: int,
) -> bool:
    """
    Bullish FVG:

    Candle 1 high
    below
    Candle 3 low
    """

    if index < 2:
        return False


    candle_1 = get_candle(
        candles,
        index - 2,
    )


    candle_3 = get_candle(
        candles,
        index,
    )


    return (

        float(candle_1["high"])

        <

        float(candle_3["low"])

    )



# ==========================================================
# BEARISH FVG CHECK
# ==========================================================

def is_bearish_fvg(
    candles: pd.DataFrame,
    index: int,
) -> bool:
    """
    Bearish FVG:

    Candle 1 low
    above
    Candle 3 high
    """

    if index < 2:
        return False


    candle_1 = get_candle(
        candles,
        index - 2,
    )


    candle_3 = get_candle(
        candles,
        index,
    )


    return (

        float(candle_1["low"])

        >

        float(candle_3["high"])

    )



# ==========================================================
# BULLISH ZONE
# ==========================================================

def bullish_gap_zone(
    candles: pd.DataFrame,
    index: int,
):
    """
    Return bullish FVG zone.
    """

    candle_1 = get_candle(
        candles,
        index - 2,
    )


    candle_3 = get_candle(
        candles,
        index,
    )


    top = float(
        candle_3["low"]
    )


    bottom = float(
        candle_1["high"]
    )


    return {

        "top": top,

        "bottom": bottom,

        "midpoint": (
            top + bottom
        ) / 2,

    }



# ==========================================================
# BEARISH ZONE
# ==========================================================

def bearish_gap_zone(
    candles: pd.DataFrame,
    index: int,
):
    """
    Return bearish FVG zone.
    """

    candle_1 = get_candle(
        candles,
        index - 2,
    )


    candle_3 = get_candle(
        candles,
        index,
    )


    top = float(
        candle_1["low"]
    )


    bottom = float(
        candle_3["high"]
    )


    return {

        "top": top,

        "bottom": bottom,

        "midpoint": (
            top + bottom
        ) / 2,

    }



# ==========================================================
# PRICE INSIDE GAP
# ==========================================================

def price_inside_gap(
    price: float,
    top: float,
    bottom: float,
) -> bool:
    """
    Check if price entered FVG zone.
    """

    return (

        bottom <= price <= top

    )



# ==========================================================
# GAP RANGE QUALITY
# ==========================================================

def gap_quality(
    candles,
    index: int,
) -> float:
    """
    Compare gap size with candle range.
    """

    if index < 2:
        return 0.0


    candle = get_candle(
        candles,
        index,
    )


    rng = candle_range(
        candle
    )


    if rng <= 0:
        return 0.0


    return min(
        abs(
            float(candle["close"])
            -
            float(candle["open"])
        )
        /
        rng
        *
        100,

        100.0,
    )



# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "calculate_gap_size",

    "calculate_gap_percent",

    "is_bullish_fvg",

    "is_bearish_fvg",

    "bullish_gap_zone",

    "bearish_gap_zone",

    "price_inside_gap",

    "gap_quality",

]