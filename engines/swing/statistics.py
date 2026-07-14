"""
=========================================================
KAI Smart Money AI

Swing Engine

statistics.py

Swing Analytics & Reporting

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations



from .constants import (

    SWING_HIGH,

    SWING_LOW,

    INTERNAL,

    EXTERNAL,

)



# ==========================================================
# TOTAL SWINGS
# ==========================================================

def total_swings(
    swings,
):
    """
    Count all swings.
    """

    return len(swings)



# ==========================================================
# SWING HIGHS
# ==========================================================

def swing_high_count(
    swings,
):
    """
    Count swing highs.
    """

    return len(

        [

            s

            for s in swings

            if s.swing_type == SWING_HIGH

        ]

    )



# ==========================================================
# SWING LOWS
# ==========================================================

def swing_low_count(
    swings,
):
    """
    Count swing lows.
    """

    return len(

        [

            s

            for s in swings

            if s.swing_type == SWING_LOW

        ]

    )



# ==========================================================
# INTERNAL SWINGS
# ==========================================================

def internal_count(
    swings,
):
    """
    Count internal swings.
    """

    return len(

        [

            s

            for s in swings

            if s.classification == INTERNAL

        ]

    )



# ==========================================================
# EXTERNAL SWINGS
# ==========================================================

def external_count(
    swings,
):
    """
    Count external swings.
    """

    return len(

        [

            s

            for s in swings

            if s.classification == EXTERNAL

        ]

    )



# ==========================================================
# LIQUIDITY EVENTS
# ==========================================================

def liquidity_taken_count(
    swings,
):
    """
    Count swept swings.
    """

    return len(

        [

            s

            for s in swings

            if s.liquidity_taken

        ]

    )



# ==========================================================
# BROKEN SWINGS
# ==========================================================

def broken_count(
    swings,
):
    """
    Count broken swings.
    """

    return len(

        [

            s

            for s in swings

            if s.broken

        ]

    )



# ==========================================================
# AVERAGE SCORE
# ==========================================================

def average_score(
    swings,
):
    """
    Average swing score.
    """

    if not swings:

        return 0


    return round(

        sum(

            s.score

            for s in swings

        )

        /

        len(swings),

        2

    )



# ==========================================================
# STRONGEST SWING
# ==========================================================

def strongest_swing(
    swings,
):
    """
    Return highest quality swing.
    """

    if not swings:

        return None



    return max(

        swings,

        key=lambda x: x.score

    )



# ==========================================================
# SUMMARY
# ==========================================================

def swing_summary(
    swings,
):
    """
    Institutional swing report.
    """

    return {


        "total":

            total_swings(

                swings

            ),



        "highs":

            swing_high_count(

                swings

            ),



        "lows":

            swing_low_count(

                swings

            ),



        "internal":

            internal_count(

                swings

            ),



        "external":

            external_count(

                swings

            ),



        "liquidity_taken":

            liquidity_taken_count(

                swings

            ),



        "broken":

            broken_count(

                swings

            ),



        "average_score":

            average_score(

                swings

            ),



        "strongest":

            strongest_swing(

                swings

            ),

    }



# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "total_swings",

    "swing_high_count",

    "swing_low_count",

    "internal_count",

    "external_count",

    "liquidity_taken_count",

    "broken_count",

    "average_score",

    "strongest_swing",

    "swing_summary",

]