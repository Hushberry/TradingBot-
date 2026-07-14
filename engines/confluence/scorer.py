"""
=========================================================
KAI Smart Money AI

Confluence Engine

scoring.py

Institutional Setup Scoring

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations


from .models import (
    ConfluenceResult,
)


from .constants import (

    ORDER_BLOCK_WEIGHT,

    FAIR_VALUE_GAP_WEIGHT,

    LIQUIDITY_WEIGHT,

    STRUCTURE_WEIGHT,

    VOLUME_WEIGHT,

)



# ==========================================================
# COMPONENT SCORES
# ==========================================================

def score_order_block(
    result: ConfluenceResult,
):
    """
    Order Block contribution.
    """

    if result.order_block_match:

        return ORDER_BLOCK_WEIGHT


    return 0



def score_fvg(
    result: ConfluenceResult,
):
    """
    FVG contribution.
    """

    if result.fair_value_gap_match:

        return FAIR_VALUE_GAP_WEIGHT


    return 0



def score_liquidity(
    result: ConfluenceResult,
):
    """
    Liquidity contribution.
    """

    if result.liquidity_match:

        return LIQUIDITY_WEIGHT


    return 0



def score_structure(
    result: ConfluenceResult,
):
    """
    Structure contribution.
    """

    if result.structure_match:

        return STRUCTURE_WEIGHT


    return 0



def score_volume(
    result: ConfluenceResult,
):
    """
    Volume contribution.
    """

    if result.volume_match:

        return VOLUME_WEIGHT


    return 0



# ==========================================================
# TOTAL SCORE
# ==========================================================

def calculate_score(
    result: ConfluenceResult,
):
    """
    Calculate total confluence score.
    """


    score = (

        score_order_block(
            result
        )

        +

        score_fvg(
            result
        )

        +

        score_liquidity(
            result
        )

        +

        score_structure(
            result
        )

        +

        score_volume(
            result
        )

    )


    result.score = score


    return score



# ==========================================================
# GRADE
# ==========================================================

def calculate_grade(
    score,
):
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

def calculate_confidence(
    score,
):
    """
    Confidence classification.
    """

    if score >= 90:

        return "Very High"


    if score >= 80:

        return "High"


    if score >= 65:

        return "Medium"


    return "Low"



# ==========================================================
# APPLY SCORE
# ==========================================================

def score_confluence(
    result: ConfluenceResult,
):
    """
    Complete scoring pipeline.
    """

    score = calculate_score(
        result
    )


    result.grade = calculate_grade(
        score
    )


    result.confidence = calculate_confidence(
        score
    )


    return result



# ==========================================================
# BREAKDOWN
# ==========================================================

def score_breakdown(
    result: ConfluenceResult,
):
    """
    Explain AI score.
    """

    return {

        "order_block":

            score_order_block(
                result
            ),


        "fair_value_gap":

            score_fvg(
                result
            ),


        "liquidity":

            score_liquidity(
                result
            ),


        "structure":

            score_structure(
                result
            ),


        "volume":

            score_volume(
                result
            ),


        "total":

            result.score,


        "grade":

            result.grade,


        "confidence":

            result.confidence,

    }



# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "calculate_score",

    "score_confluence",

    "calculate_grade",

    "calculate_confidence",

    "score_breakdown",

]