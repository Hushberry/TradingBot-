from __future__ import annotations

from dataclasses import dataclass, field
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass(slots=True)
class AnalysisResult(Generic[T]):
    """
    Standard result returned by every KAI engine.
    """

    success: bool
    engine: str
    execution_time: float

    data: T | None = None

    warnings: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)

    message: str = ""