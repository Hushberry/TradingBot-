"""
=========================================================
KAI Smart Money AI

Fair Value Gap Engine

engine.py

Public FVG Engine Interface

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations


import pandas as pd


from .detector import (

    find_fair_value_gaps,

)


from .validator import (

    validate_fvgs,

)


from .scorer import (

    score_fvgs,

)


from .lifecycle import (

    update_fvgs,

    active_fvgs,

    fresh_fvgs,

)


from .statistics import (

    fvg_summary,

)



# ==========================================================
# ENGINE CLASS
# ==========================================================

class FairValueGapEngine:
    """
    Main Institutional FVG Engine.

    External modules should only
    communicate with this class.
    """


    def __init__(self):

        self.name = (

            "KAI Institutional "

            "Fair Value Gap Engine"

        )

        self.version = "1.0"



    # ======================================================
    # DETECT
    # ======================================================

    def detect(
        self,
        candles: pd.DataFrame,
    ):
        """
        Detect raw Fair Value Gaps.
        """

        return find_fair_value_gaps(

            candles

        )



    # ======================================================
    # ANALYZE
    # ======================================================

    def analyze(
        self,
        candles: pd.DataFrame,
        market_structure=None,
        displacement_map=None,
    ):
        """
        Complete FVG analysis pipeline.
        """


        # Detect

        fvgs = self.detect(

            candles

        )


        if not fvgs:

            return {

                "fvgs": [],

                "summary": {}

            }



        # Validate

        fvgs = validate_fvgs(

            fvgs,

            displacement_map,

            market_structure,

        )


        if not fvgs:

            return {

                "fvgs": [],

                "summary": {}

            }



        # Score

        fvgs = score_fvgs(

            fvgs

        )



        # Lifecycle

        fvgs = update_fvgs(

            fvgs,

            candles,

        )


        return {

            "fvgs": fvgs,

            "summary":

                fvg_summary(

                    fvgs

                )

        }



    # ======================================================
    # ACTIVE
    # ======================================================

    def active(
        self,
        fvgs,
    ):
        """
        Return active FVGs.
        """

        return active_fvgs(

            fvgs

        )



    # ======================================================
    # FRESH
    # ======================================================

    def fresh(
        self,
        fvgs,
    ):
        """
        Return fresh FVGs.
        """

        return fresh_fvgs(

            fvgs

        )



    # ======================================================
    # SUMMARY
    # ======================================================

    def summary(
        self,
        fvgs,
    ):
        """
        Generate report.
        """

        return fvg_summary(

            fvgs

        )



# ==========================================================
# EXPORT
# ==========================================================

__all__ = [

    "FairValueGapEngine",

]