"""
=========================================================
KAI Smart Money AI

Swing Engine

models.py

Swing Data Models

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations


from dataclasses import dataclass, field


from typing import Optional, List



# ==========================================================
# SWING POINT MODEL
# ==========================================================

@dataclass
class SwingPoint:
    """
    Represents an institutional swing point.
    """


    # ------------------------------------------------------
    # Identity
    # ------------------------------------------------------

    id: Optional[str] = None


    index: int = 0


    timestamp: Optional[str] = None



    # ------------------------------------------------------
    # Price Data
    # ------------------------------------------------------

    price: float = 0.0


    swing_type: str = ""



    # ------------------------------------------------------
    # Classification
    # ------------------------------------------------------

    classification: str = "internal"


    confirmed: bool = False



    # ------------------------------------------------------
    # Strength
    # ------------------------------------------------------

    strength: float = 0.0


    score: float = 0.0


    grade: str = "D"



    # ------------------------------------------------------
    # Market Context
    # ------------------------------------------------------

    broken: bool = False


    liquidity_taken: bool = False


    used_for_structure: bool = False



    # ------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------

    active: bool = True


    age: int = 0



    # ------------------------------------------------------
    # Explanation
    # ------------------------------------------------------

    reasons: List[str] = field(

        default_factory=list

    )



    # ======================================================
    # METHODS
    # ======================================================

    def invalidate(
        self,
    ):
        """
        Disable swing point.
        """

        self.active = False



    def mark_broken(
        self,
    ):
        """
        Mark swing as broken.
        """

        self.broken = True



    def add_reason(
        self,
        reason: str,
    ):
        """
        Add explanation.
        """

        if reason not in self.reasons:

            self.reasons.append(
                reason
            )



# ==========================================================
# SWING COLLECTION MODEL
# ==========================================================

@dataclass
class SwingCollection:
    """
    Container for detected swings.
    """


    highs: List[SwingPoint] = field(

        default_factory=list

    )


    lows: List[SwingPoint] = field(

        default_factory=list

    )



    # ======================================================
    # METHODS
    # ======================================================

    def all_swings(
        self,
    ):

        return (

            self.highs

            +

            self.lows

        )



    def count(
        self,
    ):

        return len(

            self.all_swings()

        )