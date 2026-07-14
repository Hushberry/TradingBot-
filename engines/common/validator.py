"""
=========================================================
KAI Smart Money AI

Common Validators

Shared validation utilities for all engines.

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations

from typing import Iterable

import pandas as pd

from .exceptions import (
    InvalidDataFrameError,
    MissingColumnsError,
    InvalidPriceError,
    InvalidIndexError,
)


# ==========================================================
# DATAFRAME
# ==========================================================

def validate_dataframe(df) -> bool:
    """
    Validate pandas DataFrame.
    """

    if not isinstance(df, pd.DataFrame):
        raise InvalidDataFrameError(
            "Expected pandas DataFrame."
        )

    return True


def validate_required_columns(
    df: pd.DataFrame,
    columns: Iterable[str],
) -> bool:
    """
    Ensure required columns exist.
    """

    validate_dataframe(df)

    missing = [
        col
        for col in columns
        if col not in df.columns
    ]

    if missing:
        raise MissingColumnsError(missing)

    return True


# ==========================================================
# INDEX
# ==========================================================

def validate_index(
    index: int,
    length: int,
) -> bool:
    """
    Validate DataFrame index.
    """

    if index < 0 or index >= length:
        raise InvalidIndexError(
            f"Index {index} out of range."
        )

    return True


# ==========================================================
# PRICE
# ==========================================================

def validate_price(price: float) -> bool:
    """
    Validate market price.
    """

    if not isinstance(price, (int, float)):
        raise InvalidPriceError(
            "Price must be numeric."
        )

    if price <= 0:
        raise InvalidPriceError(
            "Price must be greater than zero."
        )

    return True


def validate_ohlc(
    open_price: float,
    high_price: float,
    low_price: float,
    close_price: float,
) -> bool:
    """
    Validate OHLC relationship.
    """

    validate_price(open_price)
    validate_price(high_price)
    validate_price(low_price)
    validate_price(close_price)

    if high_price < low_price:
        raise InvalidPriceError(
            "High price cannot be below Low price."
        )

    if high_price < open_price:
        raise InvalidPriceError(
            "High price below Open."
        )

    if high_price < close_price:
        raise InvalidPriceError(
            "High price below Close."
        )

    if low_price > open_price:
        raise InvalidPriceError(
            "Low price above Open."
        )

    if low_price > close_price:
        raise InvalidPriceError(
            "Low price above Close."
        )

    return True


# ==========================================================
# SCORE
# ==========================================================

def validate_score(
    score: float,
    minimum: float = 0,
    maximum: float = 100,
) -> bool:
    """
    Validate score range.
    """

    if score < minimum or score > maximum:
        raise ValueError(
            f"Score must be between {minimum} and {maximum}."
        )

    return True


# ==========================================================
# TREND
# ==========================================================

VALID_TRENDS = {
    "bullish",
    "bearish",
    "ranging",
}


def validate_trend(
    trend: str,
) -> bool:
    """
    Validate trend value.
    """

    if trend not in VALID_TRENDS:
        raise ValueError(
            f"Invalid trend: {trend}"
        )

    return True


# ==========================================================
# DIRECTION
# ==========================================================

VALID_DIRECTIONS = {
    "bullish",
    "bearish",
    "neutral",
}


def validate_direction(
    direction: str,
) -> bool:
    """
    Validate direction.
    """

    if direction not in VALID_DIRECTIONS:
        raise ValueError(
            f"Invalid direction: {direction}"
        )

    return True


# ==========================================================
# CANDLE COUNT
# ==========================================================

def validate_history(
    candles: pd.DataFrame,
    minimum: int,
) -> bool:
    """
    Ensure sufficient historical candles.
    """

    validate_dataframe(candles)

    if len(candles) < minimum:
        raise ValueError(
            f"Minimum {minimum} candles required."
        )

    return True