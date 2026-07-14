"""
=========================================================
KAI Smart Money AI

Fair Value Gap Engine

statistics.py

FVG Analytics & Reporting

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations


from .models import FairValueGap



# ==========================================================
# TOTAL FVG
# ==========================================================

def total_fvgs(
    fvgs,
) -> int:
    """
    Count all FVGs.
    """

    return len(fvgs)



# ==========================================================
# BULLISH FVG
# ==========================================================

def bullish_fvgs(
    fvgs,
):
    """
    Return bullish FVGs.
    """

    return [

        fvg

        for fvg in fvgs

        if fvg.direction == "bullish"

    ]



# ==========================================================
# BEARISH FVG
# ==========================================================

def bearish_fvgs(
    fvgs,
):
    """
    Return bearish FVGs.
    """

    return [

        fvg

        for fvg in fvgs

        if fvg.direction == "bearish"

    ]



# ==========================================================
# ACTIVE
# ==========================================================

def active_fvg_count(
    fvgs,
):
    """
    Count active FVGs.
    """

    return len(

        [

            fvg

            for fvg in fvgs

            if fvg.is_active()

        ]

    )



# ==========================================================
# FRESH
# ==========================================================

def fresh_fvg_count(
    fvgs,
):
    """
    Count fresh FVGs.
    """

    return len(

        [

            fvg

            for fvg in fvgs

            if fvg.status == "fresh"

        ]

    )



# ==========================================================
# FILLED
# ==========================================================

def filled_fvg_count(
    fvgs,
):
    """
    Count filled gaps.
    """

    return len(

        [

            fvg

            for fvg in fvgs

            if fvg.filled

        ]

    )



# ==========================================================
# INVALID
# ==========================================================

def invalid_fvg_count(
    fvgs,
):
    """
    Count invalidated gaps.
    """

    return len(

        [

            fvg

            for fvg in fvgs

            if fvg.invalidated

        ]

    )



# ==========================================================
# AVERAGE SCORE
# ==========================================================

def average_fvg_score(
    fvgs,
):
    """
    Average quality score.
    """

    if not fvgs:

        return 0.0


    return round(

        sum(

            fvg.score

            for fvg in fvgs

        )

        /

        len(fvgs),

        2

    )



# ==========================================================
# STRONGEST FVG
# ==========================================================

def strongest_fvg(
    fvgs,
):
    """
    Highest quality FVG.
    """

    if not fvgs:

        return None


    return max(

        fvgs,

        key=lambda x:x.score

    )



# ==========================================================
# SUMMARY
# ==========================================================

def fvg_summary(
    fvgs,
):
    """
    Institutional FVG report.
    """

    return {

        "total":

            total_fvgs(
                fvgs
            ),


        "bullish":

            len(
                bullish_fvgs(
                    fvgs
                )
            ),


        "bearish":

            len(
                bearish_fvgs(
                    fvgs
                )
            ),


        "active":

            active_fvg_count(
                fvgs
            ),


        "fresh":

            fresh_fvg_count(
                fvgs
            ),


        "filled":

            filled_fvg_count(
                fvgs
            ),


        "invalid":

            invalid_fvg_count(
                fvgs
            ),


        "average_score":

            average_fvg_score(
                fvgs
            ),


        "strongest":

            strongest_fvg(
                fvgs
            ),

    }



# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "total_fvgs",

    "bullish_fvgs",

    "bearish_fvgs",

    "active_fvg_count",

    "fresh_fvg_count",

    "filled_fvg_count",

    "invalid_fvg_count",

    "average_fvg_score",

    "strongest_fvg",

    "fvg_summary",

]