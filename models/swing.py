"""
=========================================================
KAI Smart Money AI
File: swing.py

Description
-----------
Represents a validated market swing (High or Low).

Swing objects are produced by the Market Structure
Engine and consumed by BOS, CHOCH, MSS, Liquidity,
Order Blocks and Trend analysis.

Author:
Vincent Chimezirim
=========================================================
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Literal


@dataclass
class Swing:
    """
    Represents a market swing.
    """

    timestamp: datetime

    index: int

    price: float

    direction: Literal["HIGH", "LOW"]

    strength: float = 0.0

    broken: bool = False

    def __post_init__(self):
        """
        Validate swing data.
        """

        if self.index < 0:
            raise ValueError(
                "Index cannot be negative."
            )

        if self.price <= 0:
            raise ValueError(
                "Price must be greater than zero."
            )

        if self.strength < 0:
            raise ValueError(
                "Strength cannot be negative."
            )

    @property
    def is_high(self) -> bool:
        """
        Returns True if this is a swing high.
        """
        return self.type == "HIGH"

    @property
    def is_low(self) -> bool:
        """
        Returns True if this is a swing low.
        """
        return self.type == "LOW"