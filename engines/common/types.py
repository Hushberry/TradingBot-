"""
=========================================================
KAI Smart Money AI

Common Types

Shared enums and dataclasses.

Author: Vincent Chimezirim
=========================================================
"""

from enum import Enum
from dataclasses import dataclass


class Direction(str, Enum):
    BULLISH = "bullish"
    BEARISH = "bearish"
    NEUTRAL = "neutral"


class Trend(str, Enum):
    BULLISH = "bullish"
    BEARISH = "bearish"
    RANGING = "ranging"


class Status(str, Enum):
    FRESH = "fresh"
    MITIGATED = "mitigated"
    INVALID = "invalid"


class StructureEvent(str, Enum):
    BOS = "BOS"
    CHOCH = "CHOCH"
    NONE = "NONE"


@dataclass(slots=True)
class PriceLevel:
    price: float
    index: int
    label: str = ""


@dataclass(slots=True)
class CandleRange:
    high: float
    low: float

    @property
    def size(self):
        return self.high - self.low