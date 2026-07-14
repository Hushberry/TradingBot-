"""
=========================================================
KAI Smart Money AI

Institutional Order Block Engine

engine.py

Public Engine Interface

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations

import pandas as pd

from .detector import (
    detect_order_blocks,
    filter_active_blocks,
    filter_fresh_blocks,
    best_order_block,
)

from .statistics import (
    order_block_summary,
)


# ==========================================================
# ENGINE CLASS
# ==========================================================

class InstitutionalOrderBlockEngine:
    """
    Main Order Block Engine.

    This is the only class that
    external modules should use.
    """


    def __init__(
        self,
    ):

        self.name = (
            "KAI Institutional "
            "Order Block Engine"
        )

        self.version = "1.0"


    # ======================================================
    # DETECT
    # ======================================================

    def detect(
        self,
        candles: pd.DataFrame,
        market_structure=None,
        liquidity=None,
        fair_value_gaps=None,
    ):
        """
        Detect institutional
        Order Blocks.
        """

        return detect_order_blocks(

            candles,

            market_structure,

            liquidity,

            fair_value_gaps,

        )


    # ======================================================
    # BUILD FOOTPRINT
    # ======================================================

    def build_footprint(
        self,
        candles: pd.DataFrame,
        market_structure=None,
        liquidity=None,
        fair_value_gaps=None,
    ):
        """
        Compatibility wrapper.

        Used by KAI main bot.
        """

        return self.detect(

            candles,

            market_structure,

            liquidity,

            fair_value_gaps,

        )


    # ======================================================
    # ACTIVE BLOCKS
    # ======================================================

    def active_blocks(
        self,
        order_blocks,
    ):
        """
        Return active blocks.
        """

        return filter_active_blocks(
            order_blocks,
        )


    # ======================================================
    # FRESH BLOCKS
    # ======================================================

    def fresh_blocks(
        self,
        order_blocks,
    ):
        """
        Return fresh blocks.
        """

        return filter_fresh_blocks(
            order_blocks,
        )


    # ======================================================
    # BEST BLOCK
    # ======================================================

    def strongest(
        self,
        order_blocks,
    ):
        """
        Return highest quality block.
        """

        return best_order_block(
            order_blocks,
        )


    # ======================================================
    # SUMMARY
    # ======================================================

    def summary(
        self,
        order_blocks,
    ):
        """
        Return engine statistics.
        """

        return order_block_summary(
            order_blocks,
        )


    # ======================================================
    # ANALYZE
    # ======================================================

    def analyze(
        self,
        candles,
        market_structure=None,
        liquidity=None,
        fair_value_gaps=None,
    ):
        """
        Complete analysis endpoint.
        """

        blocks = self.detect(

            candles,

            market_structure,

            liquidity,

            fair_value_gaps,

        )

        return {

            "order_blocks": blocks,

            "best": self.strongest(
                blocks
            ),

            "summary": self.summary(
                blocks
            ),

        }


# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "InstitutionalOrderBlockEngine",

]