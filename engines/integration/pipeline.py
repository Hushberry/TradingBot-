"""
=========================================================
KAI Smart Money AI

Integration Layer

pipeline.py

Main Analysis Pipeline

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations



# ==========================================================
# ENGINE IMPORTS
# ==========================================================

from engines.confluence import (

    ConfluenceEngine,

)



from engines.fair_value_gap import (

    FairValueGapEngine,

)



from engines.order_block import (

    OrderBlockEngine,

)



# Temporary imports
# These will be replaced after rebuilding
# Swing / Market Structure / Liquidity engines

try:

    from engines.market_structure import (

        MarketStructureEngine,

    )

except ImportError:

    MarketStructureEngine = None



try:

    from engines.liquidity import (

        LiquidityEngine,

    )

except ImportError:

    LiquidityEngine = None



try:

    from engines.swing import (

        SwingEngine,

    )

except ImportError:

    SwingEngine = None





# ==========================================================
# KAI PIPELINE
# ==========================================================

class KAIAnalysisPipeline:
    """
    Central KAI analysis coordinator.

    Controls communication between engines.
    """



    def __init__(self):


        self.order_block_engine = (

            OrderBlockEngine()

        )


        self.fvg_engine = (

            FairValueGapEngine()

        )


        self.confluence_engine = (

            ConfluenceEngine()

        )



        self.market_structure_engine = (

            MarketStructureEngine()

            if MarketStructureEngine

            else None

        )



        self.liquidity_engine = (

            LiquidityEngine()

            if LiquidityEngine

            else None

        )



        self.swing_engine = (

            SwingEngine()

            if SwingEngine

            else None

        )



    # ======================================================
    # RUN ANALYSIS
    # ======================================================

    def run(
        self,
        candles,
    ):
        """
        Execute complete KAI analysis.
        """



        # ----------------------------------------------
        # Swing
        # ----------------------------------------------

        swing_data = None


        if self.swing_engine:


            swing_data = self.swing_engine.analyze(

                candles

            )



        # ----------------------------------------------
        # Market Structure
        # ----------------------------------------------

        structure = None


        if self.market_structure_engine:


            structure = (

                self.market_structure_engine.analyze(

                    candles

                )

            )



        # ----------------------------------------------
        # Liquidity
        # ----------------------------------------------

        liquidity = None


        if self.liquidity_engine:


            liquidity = (

                self.liquidity_engine.analyze(

                    candles

                )

            )



        # ----------------------------------------------
        # Order Blocks
        # ----------------------------------------------

        order_blocks = (

            self.order_block_engine.detect(

                candles,

                structure,

                liquidity,

            )

        )



        # ----------------------------------------------
        # Fair Value Gaps
        # ----------------------------------------------

        fvg_result = (

            self.fvg_engine.analyze(

                candles,

                structure,

            )

        )


        fvgs = fvg_result.get(

            "fvgs",

            []

        )



        # ----------------------------------------------
        # Direction
        # ----------------------------------------------

        direction = "neutral"


        if structure:

            direction = structure.get(

                "trend",

                "neutral"

            )



        # ----------------------------------------------
        # Confluence
        # ----------------------------------------------

        confluence = (

            self.confluence_engine.run(

                order_blocks,

                fvgs,

                liquidity,

                structure,

                direction=direction,

            )

        )



        return {


            "swing":

                swing_data,


            "market_structure":

                structure,


            "liquidity":

                liquidity,


            "order_blocks":

                order_blocks,


            "fair_value_gaps":

                fvgs,


            "confluence":

                confluence,


        }



# ==========================================================
# EXPORT
# ==========================================================

__all__ = [

    "KAIAnalysisPipeline",

]