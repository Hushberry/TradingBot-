"""
=========================================================
KAI Smart Money AI

Confluence Engine

filters.py

Institutional Setup Filters

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations


from .models import (
    ConfluenceResult,
)


from .constants import (
    MINIMUM_SCORE,
)



# ==========================================================
# SCORE FILTER
# ==========================================================

def minimum_score_filter(
    result: ConfluenceResult,
    minimum_score: float = MINIMUM_SCORE,
):
    """
    Reject weak setups.
    """

    if result.score >= minimum_score:

        return True


    result.add_warning(

        f"Score below minimum ({minimum_score})"

    )


    return False



# ==========================================================
# STRUCTURE FILTER
# ==========================================================

def structure_filter(
    result: ConfluenceResult,
):
    """
    Ensure market structure agrees.
    """

    if result.structure_match:

        return True


    result.add_warning(

        "Missing structure confirmation"

    )


    return False



# ==========================================================
# LIQUIDITY FILTER
# ==========================================================

def liquidity_filter(
    result: ConfluenceResult,
):
    """
    Ensure liquidity event exists.
    """

    if result.liquidity_match:

        return True


    result.add_warning(

        "No liquidity confirmation"

    )


    return False



# ==========================================================
# CONFLICT FILTER
# ==========================================================

def conflict_filter(
    result: ConfluenceResult,
):
    """
    Detect contradictory signals.
    """

    bullish = 0

    bearish = 0



    if result.order_block_match:

        if result.direction == "bullish":

            bullish += 1

        elif result.direction == "bearish":

            bearish += 1



    if result.fair_value_gap_match:

        if result.direction == "bullish":

            bullish += 1

        elif result.direction == "bearish":

            bearish += 1



    if bullish and bearish:

        result.add_warning(

            "Conflicting institutional signals"

        )


        return False



    return True



# ==========================================================
# CONFIRMATION FILTER
# ==========================================================

def confirmation_filter(
    result: ConfluenceResult,
):
    """
    Check minimum institutional evidence.
    """

    confirmations = 0



    if result.order_block_match:

        confirmations += 1



    if result.fair_value_gap_match:

        confirmations += 1



    if result.liquidity_match:

        confirmations += 1



    if result.structure_match:

        confirmations += 1



    if confirmations >= 3:

        return True



    result.add_warning(

        "Insufficient confirmations"

    )


    return False



# ==========================================================
# MASTER FILTER
# ==========================================================

def apply_filters(
    result: ConfluenceResult,
):
    """
    Run all protection filters.
    """


    checks = [

        minimum_score_filter(
            result
        ),


        structure_filter(
            result
        ),


        liquidity_filter(
            result
        ),


        conflict_filter(
            result
        ),


        confirmation_filter(
            result
        ),

    ]


    return all(
        checks
    )



# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "minimum_score_filter",

    "structure_filter",

    "liquidity_filter",

    "conflict_filter",

    "confirmation_filter",

    "apply_filters",

]