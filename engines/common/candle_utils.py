"""
=========================================================
KAI Smart Money AI

Common Candle Utilities

Shared candle helper functions used by every engine.

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations

from typing import Union

import pandas as pd

from .exceptions import (
    EmptyDataError,
    InvalidDataFrameError,
    InvalidIndexError,
    MissingColumnsError,
)

REQUIRED_COLUMNS = (
    "open",
    "high",
    "low",
    "close",
)


# ==========================================================
# VALIDATION
# ==========================================================

def validate_candles(candles: pd.DataFrame) -> None:
    """
    Validate OHLC DataFrame.
    """

    if not isinstance(candles, pd.DataFrame):
        raise InvalidDataFrameError(
            "Expected pandas DataFrame."
        )

    if candles.empty:
        raise EmptyDataError(
            "Candle DataFrame is empty."
        )

    missing = [
        c for c in REQUIRED_COLUMNS
        if c not in candles.columns
    ]

    if missing:
        raise MissingColumnsError(missing)


# ==========================================================
# ACCESS
# ==========================================================

def get_candle(
    candles: pd.DataFrame,
    index: int
) -> pd.Series:
    """
    Return one candle safely.
    """

    validate_candles(candles)

    if index < 0 or index >= len(candles):
        raise InvalidIndexError(
            f"Invalid candle index: {index}"
        )

    return candles.iloc[index]


def open_price(candle: Union[pd.Series, dict]) -> float:
    return float(candle["open"])


def high_price(candle: Union[pd.Series, dict]) -> float:
    return float(candle["high"])


def low_price(candle: Union[pd.Series, dict]) -> float:
    return float(candle["low"])


def close_price(candle: Union[pd.Series, dict]) -> float:
    return float(candle["close"])


# ==========================================================
# BODY / RANGE
# ==========================================================

def candle_body(candle) -> float:
    return abs(close_price(candle) - open_price(candle))


def candle_range(candle) -> float:
    return high_price(candle) - low_price(candle)


def body_ratio(candle) -> float:

    rng = candle_range(candle)

    if rng == 0:
        return 0.0

    return candle_body(candle) / rng


def body_strength(candle) -> float:
    """
    Returns 0-100
    """

    return body_ratio(candle) * 100.0


# ==========================================================
# WICKS
# ==========================================================

def upper_wick(candle) -> float:

    return (
        high_price(candle)
        - max(
            open_price(candle),
            close_price(candle),
        )
    )


def lower_wick(candle) -> float:

    return (
        min(
            open_price(candle),
            close_price(candle),
        )
        - low_price(candle)
    )


# ==========================================================
# DIRECTION
# ==========================================================

def is_bullish(candle) -> bool:
    return close_price(candle) > open_price(candle)


def is_bearish(candle) -> bool:
    return close_price(candle) < open_price(candle)


def is_doji(
    candle,
    threshold: float = 0.10
) -> bool:

    return body_ratio(candle) <= threshold


def candle_direction(candle) -> str:

    if is_bullish(candle):
        return "bullish"

    if is_bearish(candle):
        return "bearish"

    return "neutral"


# ==========================================================
# BODY QUALITY
# ==========================================================

def has_large_body(
    candle,
    minimum_ratio: float = 0.60
) -> bool:

    return body_ratio(candle) >= minimum_ratio


def has_small_body(
    candle,
    maximum_ratio: float = 0.30
) -> bool:

    return body_ratio(candle) <= maximum_ratio


# ==========================================================
# BAR PATTERNS
# ==========================================================

def is_inside_bar(
    current,
    previous
) -> bool:

    return (
        high_price(current) < high_price(previous)
        and
        low_price(current) > low_price(previous)
    )


def is_outside_bar(
    current,
    previous
) -> bool:

    return (
        high_price(current) > high_price(previous)
        and
        low_price(current) < low_price(previous)
    )


# ==========================================================
# PRICE DISTANCE
# ==========================================================

def price_distance(
    price1: float,
    price2: float
) -> float:

    return abs(price1 - price2)


def midpoint(candle) -> float:

    return (
        high_price(candle)
        + low_price(candle)
    ) / 2.0


# ==========================================================
# ENGULFING
# ==========================================================

def bullish_engulfing(
    current,
    previous
) -> bool:

    return (
        is_bullish(current)
        and
        is_bearish(previous)
        and
        close_price(current) > open_price(previous)
        and
        open_price(current) < close_price(previous)
    )


def bearish_engulfing(
    current,
    previous
) -> bool:

    return (
        is_bearish(current)
        and
        is_bullish(previous)
        and
        open_price(current) > close_price(previous)
        and
        close_price(current) < open_price(previous)
    )