"""
=========================================================
KAI Smart Money AI

Swing Engine

scorer.py

Swing Quality Scoring

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations



from .models import (

    SwingPoint,

)



from .constants import (

    INTERNAL,

    EXTERNAL,

)



# ==========================================================
# CLASSIFICATION SCORE
# ==========================================================

def score_classification(
    swing: SwingPoint,
):
    """
    Score based on market importance.
    """

    if swing.classification == EXTERNAL:

        return 40



    if swing.classification == INTERNAL:

        return 20



    return 0



# ==========================================================
# CONFIRMATION SCORE
# ==========================================================

def score_confirmation(
    swing: SwingPoint,
):
    """
    Confirmed swing bonus.
    """

    if swing.confirmed:

        return 20


    return 0



# ==========================================================
# LIQUIDITY SCORE
# ==========================================================

def score_liquidity(
    swing: SwingPoint,
):
    """
    Liquidity relevance.
    """

    if swing.liquidity_taken:

        return 20


    return 0



# ==========================================================
# STRUCTURE SCORE
# ==========================================================

def score_structure(
    swing: SwingPoint,
):
    """
    Structure usage bonus.
    """

    if swing.used_for_structure:

        return 20


    return 0



# ==========================================================
# TOTAL SCORE
# ==========================================================

def calculate_swing_score(
    swing: SwingPoint,
):
    """
    Calculate swing quality score.
    """

    score = (

        score_classification(

            swing

        )

        +

        score_confirmation(

            swing

        )

        +

        score_liquidity(

            swing

        )

        +

        score_structure(

            swing

        )

    )


    swing.score = min(

        score,

        100

    )


    swing.strength = swing.score


    return swing.score



# ==========================================================
# GRADE
# ==========================================================

def swing_grade(
    score,
):
    """
    Convert score to grade.
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
# SCORE ONE
# ==========================================================

def score_swing(
    swing: SwingPoint,
):
    """
    Score individual swing.
    """

    score = calculate_swing_score(

        swing

    )


    swing.grade = swing_grade(

        score

    )


    return swing



# ==========================================================
# SCORE MANY
# ==========================================================

def score_swings(
    swings,
):
    """
    Score all swings.
    """

    for swing in swings:

        score_swing(

            swing

        )



    return sorted(

        swings,

        key=lambda x: x.score,

        reverse=True

    )



# ==========================================================
# BREAKDOWN
# ==========================================================

def swing_score_breakdown(
    swing: SwingPoint,
):
    """
    Explain swing score.
    """

    return {

        "classification":

            score_classification(

                swing

            ),


        "confirmation":

            score_confirmation(

                swing

            ),


        "liquidity":

            score_liquidity(

                swing

            ),


        "structure":

            score_structure(

                swing

            ),


        "total":

            swing.score,


        "grade":

            swing.grade,

    }



# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "calculate_swing_score",

    "score_swing",

    "score_swings",

    "swing_grade",

    "swing_score_breakdown",

]