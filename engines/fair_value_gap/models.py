"""
=========================================================
KAI Smart Money AI

Fair Value Gap Engine

models.py

Data Models

Author: Vincent Chimezirim
=========================================================
"""

from dataclasses import dataclass, field

from typing import Optional, List



@dataclass
class FairValueGap:
    """
    Institutional Fair Value Gap object.
    """


    # Identity

    id: Optional[str] = None

    created_index: int = 0

    created_time: Optional[str] = None



    # Direction

    direction: str = ""



    # Price zone

    top: float = 0.0

    bottom: float = 0.0

    midpoint: float = 0.0



    # Size

    size: float = 0.0

    size_percent: float = 0.0



    # Strength

    score: float = 0.0

    confidence: str = ""

    grade: str = ""



    # Confirmation

    displacement_score: float = 0.0

    structure_confirmed: bool = False

    volume_confirmed: bool = False



    # Lifecycle

    status: str = "fresh"

    tested: bool = False

    filled: bool = False

    invalidated: bool = False



    # Tracking

    touches: int = 0

    age: int = 0



    # Explanation

    reasons: List[str] = field(
        default_factory=list
    )



    def is_active(self):
        """
        Check if FVG is still usable.
        """

        return not self.invalidated and not self.filled



    def mark_tested(self):
        """
        Mark FVG as tested.
        """

        self.tested = True

        self.status = "tested"



    def mark_filled(self):
        """
        Mark FVG as filled.
        """

        self.filled = True

        self.status = "filled"



    def invalidate(self):
        """
        Invalidate FVG.
        """

        self.invalidated = True

        self.status = "invalid"