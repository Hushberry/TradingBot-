"""
=========================================================
KAI Smart Money AI

Confluence Engine

engine.py

Main Institutional Confluence Interface

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations


from .analyzer import (

    analyze_confluence,

)


from .scoring import (

    score_confluence,

    score_breakdown,

)


from .filters import (

    apply_filters,

)


from .decision import (

    create_trade_decision,

)



from .models import (

    ConfluenceResult,

)



# ==========================================================
# ENGINE CLASS
# ==========================================================

class ConfluenceEngine:
    """
    Main KAI Confluence Engine.

    Combines:

    - Order Blocks
    - Fair Value Gaps
    - Liquidity
    - Market Structure
    - Volume

    into one institutional decision.
    """



    def __init__(self):

        self.name = (

            "KAI Institutional "

            "Confluence Engine"

        )


        self.version = "1.0"



    # ======================================================
    # ANALYZE
    # ======================================================

    def analyze(
        self,
        order_blocks=None,
        fvgs=None,
        liquidity=None,
        market_structure=None,
        volume_data=None,
        direction="neutral",
    ):
        """
        Build confluence result.
        """


        result = analyze_confluence(

            order_blocks,

            fvgs,

            liquidity,

            market_structure,

            volume_data,

            direction,

        )


        return result



    # ======================================================
    # SCORE
    # ======================================================

    def score(
        self,
        result: ConfluenceResult,
    ):
        """
        Calculate confidence.
        """

        return score_confluence(

            result

        )



    # ======================================================
    # VALIDATE
    # ======================================================

    def validate(
        self,
        result: ConfluenceResult,
    ):
        """
        Apply institutional filters.
        """

        return apply_filters(

            result

        )



    # ======================================================
    # SIGNAL
    # ======================================================

    def generate_signal(
        self,
        result: ConfluenceResult,
    ):
        """
        Generate final KAI decision.
        """


        return create_trade_decision(

            result

        )



    # ======================================================
    # COMPLETE PIPELINE
    # ======================================================

    def run(
        self,
        order_blocks=None,
        fvgs=None,
        liquidity=None,
        market_structure=None,
        volume_data=None,
        direction="neutral",
    ):
        """
        Full confluence pipeline.
        """


        result = self.analyze(

            order_blocks,

            fvgs,

            liquidity,

            market_structure,

            volume_data,

            direction,

        )


        self.score(

            result

        )


        valid = self.validate(

            result

        )


        signal = self.generate_signal(

            result

        )


        return {

            "valid":

                valid,


            "result":

                result,


            "score_breakdown":

                score_breakdown(

                    result

                ),


            "signal":

                signal,

        }



# ==========================================================
# EXPORT
# ==========================================================

__all__ = [

    "ConfluenceEngine",

]