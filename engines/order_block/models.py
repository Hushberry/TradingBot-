"""
=========================================================
KAI Smart Money AI
Institutional Order Block Engine

models.py

Data models used by the Order Block Engine.

Author: Vincent Chimezirim
=========================================================
"""

from dataclasses import dataclass, field
from typing import List, Optional


# ==========================================================
# DISPLACEMENT
# ==========================================================

@dataclass(slots=True)
class Displacement:
    """
    Represents an institutional displacement move.
    """

    valid: bool = False

    direction: str = ""

    score: float = 0.0

    distance: float = 0.0

    strength: float = 0.0

    velocity: float = 0.0

    expansion: float = 0.0

    acceleration: float = 0.0

    start_index: int = -1

    end_index: int = -1

    created_fvg: bool = False

    liquidity_sweep: bool = False

    structure_break: bool = False

    reason: List[str] = field(default_factory=list)


# ==========================================================
# ORDER BLOCK CANDIDATE
# ==========================================================

@dataclass(slots=True)
class OrderBlockCandidate:
    """
    Candidate before validation.
    """

    index: int

    candle_time: Optional[object]

    type: str

    open: float

    high: float

    low: float

    close: float

    displacement: Displacement

    body_ratio: float

    range_size: float

    valid: bool = False

    rejection_reason: Optional[str] = None


# ==========================================================
# FINAL ORDER BLOCK
# ==========================================================

@dataclass(slots=True)
class OrderBlock:
    """
    Final validated institutional order block.
    """

    id: int

    type: str

    high: float

    low: float

    open: float

    close: float

    created_index: int

    created_time: Optional[object]

    mitigation_index: Optional[int] = None

    mitigation_time: Optional[object] = None

    status: str = "fresh"

    strength: float = 0.0

    confidence: float = 0.0

    score: float = 0.0

    grade: str = "D"

    retests: int = 0

    age: int = 0

    displacement: Optional[Displacement] = None

    reason: List[str] = field(default_factory=list)

    tags: List[str] = field(default_factory=list)


# ==========================================================
# ENGINE STATISTICS
# ==========================================================

@dataclass(slots=True)
class EngineStatistics:
    """
    Statistics generated after processing.
    """

    candles_processed: int = 0

    candidates_found: int = 0

    candidates_rejected: int = 0

    valid_order_blocks: int = 0

    fresh_blocks: int = 0

    mitigated_blocks: int = 0

    invalid_blocks: int = 0

    average_score: float = 0.0

    highest_score: float = 0.0

    lowest_score: float = 0.0

    processing_time: float = 0.0


# ==========================================================
# ENGINE RESULT
# ==========================================================

@dataclass(slots=True)
class EngineResult:
    """
    Final object returned by detector.py.
    """

    status: str

    order_blocks: List[OrderBlock]

    statistics: EngineStatistics

    debug: List[str] = field(default_factory=list)