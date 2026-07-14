"""
=========================================================
KAI Smart Money AI

Common Math Utilities

Shared mathematical utilities used by all engines.

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations

from typing import Iterable, Sequence

import math
import pandas as pd


# ==========================================================
# BASIC
# ==========================================================

def clamp(value: float, minimum: float, maximum: float) -> float:
    """
    Restrict value between minimum and maximum.
    """
    return max(minimum, min(value, maximum))


def safe_divide(
    numerator: float,
    denominator: float,
    default: float = 0.0,
) -> float:
    """
    Safe division.
    """
    if denominator == 0:
        return default

    return numerator / denominator


def percentage(part: float, whole: float) -> float:
    """
    Calculate percentage.
    """
    return safe_divide(part * 100.0, whole)


def percentage_change(old: float, new: float) -> float:
    """
    Percentage difference.
    """
    if old == 0:
        return 0.0

    return ((new - old) / old) * 100.0


# ==========================================================
# PRICE
# ==========================================================

def distance(price1: float, price2: float) -> float:
    return abs(price1 - price2)


def midpoint(value1: float, value2: float) -> float:
    return (value1 + value2) / 2.0


def normalize(
    value: float,
    minimum: float,
    maximum: float,
) -> float:
    """
    Normalize to 0-1.
    """

    if maximum == minimum:
        return 0.0

    return (value - minimum) / (maximum - minimum)


# ==========================================================
# AVERAGES
# ==========================================================

def average(values: Sequence[float]) -> float:
    """
    Arithmetic mean.
    """

    if len(values) == 0:
        return 0.0

    return sum(values) / len(values)


def rolling_average(
    values: Sequence[float],
    window: int,
) -> list[float]:

    if window <= 0:
        raise ValueError("Window must be positive.")

    result = []

    for i in range(len(values)):

        start = max(0, i - window + 1)

        subset = values[start:i + 1]

        result.append(average(subset))

    return result


# ==========================================================
# PANDAS MOVING AVERAGES
# ==========================================================

def sma(series: pd.Series, period: int) -> pd.Series:
    """
    Simple Moving Average.
    """
    return series.rolling(period).mean()


def ema(series: pd.Series, period: int) -> pd.Series:
    """
    Exponential Moving Average.
    """
    return series.ewm(span=period, adjust=False).mean()


# ==========================================================
# ATR
# ==========================================================

def true_range(
    high: float,
    low: float,
    previous_close: float,
) -> float:

    return max(

        high - low,

        abs(high - previous_close),

        abs(low - previous_close)

    )


def atr(
    candles: pd.DataFrame,
    period: int = 14,
) -> pd.Series:
    """
    Average True Range.
    """

    previous_close = candles["close"].shift(1)

    tr = pd.concat(

        [

            candles["high"] - candles["low"],

            (candles["high"] - previous_close).abs(),

            (candles["low"] - previous_close).abs()

        ],

        axis=1

    ).max(axis=1)

    return tr.rolling(period).mean()


# ==========================================================
# VOLATILITY
# ==========================================================

def standard_deviation(values: Sequence[float]) -> float:

    if len(values) <= 1:
        return 0.0

    mean = average(values)

    variance = sum(

        (x - mean) ** 2

        for x in values

    ) / len(values)

    return math.sqrt(variance)


# ==========================================================
# SCALING
# ==========================================================

def normalize_score(
    score: float,
    maximum: float = 100.0,
) -> float:
    """
    Normalize score between 0 and 1.
    """

    return clamp(score / maximum, 0.0, 1.0)


def grade_score(score: float) -> str:

    if score >= 90:
        return "A"

    if score >= 80:
        return "B"

    if score >= 70:
        return "C"

    if score >= 60:
        return "D"

    return "F"


# ==========================================================
# PRICE ROUNDING
# ==========================================================

def round_price(
    price: float,
    digits: int = 5,
) -> float:

    return round(price, digits)


# ==========================================================
# PIPS
# ==========================================================

def pip_distance(
    price1: float,
    price2: float,
    pip_size: float = 0.0001,
) -> float:
    """
    Distance in pips.
    """

    if pip_size <= 0:
        raise ValueError("pip_size must be positive.")

    return abs(price1 - price2) / pip_size


# ==========================================================
# MAX / MIN
# ==========================================================

def highest(values: Iterable[float]) -> float:
    values = list(values)
    return max(values) if values else 0.0


def lowest(values: Iterable[float]) -> float:
    values = list(values)
    return min(values) if values else 0.0