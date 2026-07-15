"""
=========================================================
KAI Smart Money AI
File: candle.py

Description
-----------
Represents one completed market candle.

Every analysis engine in KAI receives Candle objects.

Author:
Vincent Chimezirim
=========================================================
"""

from dataclasses import dataclass
from datetime import datetime
import math


@dataclass(frozen=True)
class Candle:
    """
    Represents one completed market candle.
    """

    timestamp: datetime

    open: float
    high: float
    low: float
    close: float

    volume: float = 0.0

    def __post_init__(self):
        """
        Validate candle values after creation.
        """

        if self.high < self.low:
            raise ValueError(
                "High cannot be lower than Low."
            )

        if not (self.low <= self.open <= self.high):
            raise ValueError(
                "Open price must be between Low and High."
            )

        if not (self.low <= self.close <= self.high):
            raise ValueError(
                "Close price must be between Low and High."
            )

        if self.volume < 0:
            raise ValueError(
                "Volume cannot be negative."
            )

    @property
    def body_size(self) -> float:
        """
        Returns candle body size.
        """
        return abs(self.close - self.open)

    @property
    def range(self) -> float:
        """
        Returns total candle range.
        """
        return self.high - self.low

    @property
    def upper_wick(self) -> float:
        """
        Returns upper wick size.
        """
        return self.high - max(
            self.open,
            self.close,
        )

    @property
    def lower_wick(self) -> float:
        """
        Returns lower wick size.
        """
        return min(
            self.open,
            self.close,
        ) - self.low

    @property
    def midpoint(self) -> float:
        """
        Returns candle midpoint.
        """
        return (self.high + self.low) / 2

    @property
    def typical_price(self) -> float:
        """
        Returns the typical price.

        Formula:
        (High + Low + Close) / 3
        """
        return (
            self.high
            + self.low
            + self.close
        ) / 3

    @property
    def is_bullish(self) -> bool:
        """
        True if bullish candle.
        """
        return self.close > self.open

    @property
    def is_bearish(self) -> bool:
        """
        True if bearish candle.
        """
        return self.close < self.open

    @property
    def is_doji(self) -> bool:
        """
        True if Open and Close are nearly equal.
        """
        return math.isclose(
            self.open,
            self.close,
            abs_tol=1e-8,
        )