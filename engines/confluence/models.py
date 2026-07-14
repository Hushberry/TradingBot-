"""
=========================================================
KAI Smart Money AI

Confluence Engine

models.py

Institutional Confluence Data Models

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field

from typing import List, Optional



# ==========================================================
# CONFLUENCE RESULT
# ==========================================================

@dataclass
class ConfluenceResult:
    """
    Combined institutional evidence result.
    """


    # ------------------------------------------------------
    # Market Direction
    # ------------------------------------------------------

    direction: str = "neutral"



    # ------------------------------------------------------
    # Score
    # ------------------------------------------------------

    score: float = 0.0

    confidence: str = "Low"

    grade: str = "D"



    # ------------------------------------------------------
    # Component Confirmation
    # ------------------------------------------------------

    order_block_match: bool = False

    fair_value_gap_match: bool = False

    liquidity_match: bool = False

    structure_match: bool = False

    volume_match: bool = False



    # ------------------------------------------------------
    # Evidence
    # ------------------------------------------------------

    reasons: List[str] = field(
        default_factory=list
    )



    warnings: List[str] = field(
        default_factory=list
    )



    # ------------------------------------------------------
    # Trade Information
    # ------------------------------------------------------

    entry: Optional[float] = None

    stop_loss: Optional[float] = None

    take_profit: Optional[float] = None



    risk_reward: Optional[float] = None



    # ------------------------------------------------------
    # Metadata
    # ------------------------------------------------------

    timestamp: Optional[str] = None

    timeframe: Optional[str] = None



    # ======================================================
    # METHODS
    # ======================================================

    def add_reason(
        self,
        message: str,
    ):
        """
        Add positive evidence.
        """

        if message not in self.reasons:

            self.reasons.append(
                message
            )



    def add_warning(
        self,
        message: str,
    ):
        """
        Add risk warning.
        """

        if message not in self.warnings:

            self.warnings.append(
                message
            )



    def is_tradeable(
        self,
        minimum_score: float = 65,
    ):
        """
        Check if setup qualifies.
        """

        return self.score >= minimum_score



    def summary(
        self,
    ):
        """
        Return compact AI summary.
        """

        return {

            "direction":
                self.direction,


            "score":
                self.score,


            "confidence":
                self.confidence,


            "grade":
                self.grade,


            "reasons":
                self.reasons,


            "warnings":
                self.warnings,

        }