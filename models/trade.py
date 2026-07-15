"""
=========================================================
KAI Smart Money AI
File: trade.py

Description
-----------
Represents a complete trade setup generated
by KAI after all analysis is finished.

Author:
Vincent Chimezirim
=========================================================
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Literal


@dataclass
class Trade:
    """
    Represents a trade setup.
    """

    symbol: str

    timeframe: str

    timestamp: datetime

    direction: Literal["BUY", "SELL"]

    entry: float

    stop_loss: float

    take_profit: float

    confidence: float = 0.0

    risk_reward: float = 0.0

    probability: float = 0.0

    active: bool = True

    executed: bool = False

    def __post_init__(self) -> None:
        """
        Validate trade values.
        """

        if self.entry <= 0:
            raise ValueError(
                "Entry price must be greater than zero."
            )

        if self.stop_loss <= 0:
            raise ValueError(
                "Stop Loss must be greater than zero."
            )

        if self.take_profit <= 0:
            raise ValueError(
                "Take Profit must be greater than zero."
            )

        if not (0 <= self.confidence <= 100):
            raise ValueError(
                "Confidence must be between 0 and 100."
            )

        if not (0 <= self.probability <= 100):
            raise ValueError(
                "Probability must be between 0 and 100."
            )

        if self.risk_reward < 0:
            raise ValueError(
                "Risk Reward cannot be negative."
            )

    @property
    def is_buy(self) -> bool:
        """
        Returns True if Buy setup.
        """
        return self.direction == "BUY"

    @property
    def is_sell(self) -> bool:
        """
        Returns True if Sell setup.
        """
        return self.direction == "SELL"