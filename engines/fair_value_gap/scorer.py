"""
=========================================================
KAI Smart Money AI

Fair Value Gap Engine

scorer.py

Institutional FVG Scoring

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations


from .models import FairValueGap


from .constants import (

    DISPLACEMENT_WEIGHT,

    GAP_SIZE_WEIGHT,

    STRUCTURE_WEIGHT,

    VOLUME_WEIGHT,

    FRESHNESS_WEIGHT,

)



# ==========================================================
# DISPLACEMENT SCORE
# ==========================================================

def score_displacement(
    fvg: FairValueGap,
) -> float:
    """
    Maximum: 30
    """

    value = fvg.displacement_score


    return min(

        (

            value / 100

        )

        *

        DISPLACEMENT_WEIGHT,

        DISPLACEMENT_WEIGHT,

    )



# ==========================================================
# GAP SIZE SCORE
# ==========================================================

def score_gap_size(
    fvg: FairValueGap,
) -> float:
    """
    Maximum: 25
    """

    value = min(

        fvg.size_percent * 100000,

        100,

    )


    return (

        value / 100

    ) * GAP_SIZE_WEIGHT



# ==========================================================
# STRUCTURE SCORE
# ==========================================================

def score_structure(
    fvg: FairValueGap,
) -> float:
    """
    Maximum: 20
    """

    if fvg.structure_confirmed:

        return STRUCTURE_WEIGHT


    return 0.0



# ==========================================================
# VOLUME SCORE
# ==========================================================

def score_volume(
    fvg: FairValueGap,
) -> float:
    """
    Maximum: 15
    """

    if fvg.volume_confirmed:

        return VOLUME_WEIGHT


    return 0.0



# ==========================================================
# FRESHNESS SCORE
# ==========================================================

def score_freshness(
    fvg: FairValueGap,
) -> float:
    """
    Maximum: 10
    """

    if not fvg.filled:

        return FRESHNESS_WEIGHT


    return 0.0



# ==========================================================
# TOTAL SCORE
# ==========================================================

def calculate_fvg_score(
    fvg: FairValueGap,
) -> float:
    """
    Calculate final FVG score.
    """

    score = (

        score_displacement(fvg)

        +

        score_gap_size(fvg)

        +

        score_structure(fvg)

        +

        score_volume(fvg)

        +

        score_freshness(fvg)

    )


    fvg.score = round(

        min(score,100),

        2

    )


    return fvg.score



# ==========================================================
# GRADE
# ==========================================================

def fvg_grade(
    score: float,
) -> str:
    """
    Institutional grade.
    """

    if score >= 90:

        return "A+"


    if score >= 80:

        return "A"


    if score >= 70:

        return "B"


    if score >= 60:

        return "C"


    return "D"



# ==========================================================
# CONFIDENCE
# ==========================================================

def fvg_confidence(
    score: float,
) -> str:

    if score >= 85:

        return "Very High"


    if score >= 70:

        return "High"


    if score >= 60:

        return "Medium"


    return "Low"



# ==========================================================
# EXPLANATION
# ==========================================================

def explain_fvg_score(
    fvg: FairValueGap,
) -> dict:
    """
    Score breakdown.
    """

    return {

        "displacement":

            score_displacement(fvg),


        "gap_size":

            score_gap_size(fvg),


        "structure":

            score_structure(fvg),


        "volume":

            score_volume(fvg),


        "freshness":

            score_freshness(fvg),


        "total":

            fvg.score,


        "grade":

            fvg_grade(fvg.score),


        "confidence":

            fvg_confidence(fvg.score),

    }



# ==========================================================
# SCORE MANY
# ==========================================================

def score_fvgs(
    fvgs,
):
    """
    Score all FVGs.
    """

    for fvg in fvgs:

        calculate_fvg_score(
            fvg
        )


        fvg.grade = fvg_grade(
            fvg.score
        )


        fvg.confidence = fvg_confidence(
            fvg.score
        )


    return sorted(

        fvgs,

        key=lambda x:x.score,

        reverse=True

    )



# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "calculate_fvg_score",

    "score_fvgs",

    "fvg_grade",

    "fvg_confidence",

    "explain_fvg_score",

]