"""
=========================================================
KAI Smart Money AI

Confluence Engine

analyzer.py

Institutional Evidence Analyzer

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations


from .models import (
    ConfluenceResult,
)


from .utils import (

    normalize_direction,

    get_order_block_direction,

    get_fvg_direction,

    directions_align,

    structure_is_confirmed,

    liquidity_swept,

)



# ==========================================================
# ORDER BLOCK ANALYSIS
# ==========================================================

def analyze_order_block(
    result: ConfluenceResult,
    order_blocks,
    direction,
):
    """
    Check Order Block confirmation.
    """

    if not order_blocks:

        return


    for block in order_blocks:

        block_direction = get_order_block_direction(
            block
        )


        if directions_align(

            block_direction,

            direction,

        ):

            result.order_block_match = True


            result.add_reason(

                f"{direction} Order Block confirmed"

            )


            return



    result.add_warning(

        "No matching Order Block"

    )



# ==========================================================
# FVG ANALYSIS
# ==========================================================

def analyze_fvg(
    result: ConfluenceResult,
    fvgs,
    direction,
):
    """
    Check FVG confirmation.
    """

    if not fvgs:

        return


    for fvg in fvgs:

        fvg_direction = get_fvg_direction(
            fvg
        )


        if directions_align(

            fvg_direction,

            direction,

        ):

            result.fair_value_gap_match = True


            result.add_reason(

                f"{direction} Fair Value Gap confirmed"

            )


            return



    result.add_warning(

        "No matching Fair Value Gap"

    )



# ==========================================================
# LIQUIDITY ANALYSIS
# ==========================================================

def analyze_liquidity(
    result,
    liquidity,
    direction,
):
    """
    Check liquidity sweep.
    """

    if liquidity_swept(

        liquidity,

        direction,

    ):

        result.liquidity_match = True


        result.add_reason(

            "Liquidity sweep confirmed"

        )

    else:

        result.add_warning(

            "No liquidity sweep"

        )



# ==========================================================
# STRUCTURE ANALYSIS
# ==========================================================

def analyze_structure(
    result,
    market_structure,
    direction,
):
    """
    Check BOS/CHoCH.
    """

    if structure_is_confirmed(

        market_structure,

        direction,

    ):

        result.structure_match = True


        result.add_reason(

            "Market structure confirmed"

        )

    else:

        result.add_warning(

            "Structure not confirmed"

        )



# ==========================================================
# VOLUME ANALYSIS
# ==========================================================

def analyze_volume(
    result,
    volume_data=None,
):
    """
    Volume confirmation.
    """

    if volume_data is None:

        return


    if volume_data >= 1:

        result.volume_match = True


        result.add_reason(

            "Volume confirmation"

        )

    else:

        result.add_warning(

            "Weak volume"

        )



# ==========================================================
# MASTER ANALYZER
# ==========================================================

def analyze_confluence(
    order_blocks=None,
    fvgs=None,
    liquidity=None,
    market_structure=None,
    volume_data=None,
    direction="neutral",
):
    """
    Combine all institutional evidence.
    """

    direction = normalize_direction(
        direction
    )


    result = ConfluenceResult()


    result.direction = direction



    analyze_order_block(

        result,

        order_blocks,

        direction,

    )


    analyze_fvg(

        result,

        fvgs,

        direction,

    )


    analyze_liquidity(

        result,

        liquidity,

        direction,

    )


    analyze_structure(

        result,

        market_structure,

        direction,

    )


    analyze_volume(

        result,

        volume_data,

    )


    return result



# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "analyze_order_block",

    "analyze_fvg",

    "analyze_liquidity",

    "analyze_structure",

    "analyze_volume",

    "analyze_confluence",

]