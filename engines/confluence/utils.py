"""
=========================================================
KAI Smart Money AI

Confluence Engine

utils.py

Confluence Helper Functions

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations



# ==========================================================
# DIRECTION NORMALIZER
# ==========================================================

def normalize_direction(
    direction,
):
    """
    Convert different direction formats
    into standard values.
    """

    if direction is None:
        return "neutral"


    direction = str(
        direction
    ).lower()


    if direction in (
        "bull",
        "bullish",
        "buy",
        "long",
    ):

        return "bullish"



    if direction in (
        "bear",
        "bearish",
        "sell",
        "short",
    ):

        return "bearish"



    return "neutral"



# ==========================================================
# EXTRACT ORDER BLOCK DIRECTION
# ==========================================================

def get_order_block_direction(
    order_block,
):
    """
    Extract OB direction.
    """

    if order_block is None:

        return "neutral"


    return normalize_direction(

        getattr(

            order_block,

            "direction",

            None,

        )

    )



# ==========================================================
# EXTRACT FVG DIRECTION
# ==========================================================

def get_fvg_direction(
    fvg,
):
    """
    Extract FVG direction.
    """

    if fvg is None:

        return "neutral"


    return normalize_direction(

        getattr(

            fvg,

            "direction",

            None,

        )

    )



# ==========================================================
# CHECK DIRECTION ALIGNMENT
# ==========================================================

def directions_align(
    first,
    second,
):
    """
    Check if two signals agree.
    """

    first = normalize_direction(
        first
    )


    second = normalize_direction(
        second
    )


    return (

        first != "neutral"

        and

        first == second

    )



# ==========================================================
# MARKET STRUCTURE CONFIRMATION
# ==========================================================

def structure_is_confirmed(
    market_structure,
    direction,
):
    """
    Check BOS/CHoCH alignment.
    """

    if not market_structure:

        return False



    direction = normalize_direction(
        direction
    )


    events = market_structure.get(
        "events",
        []
    )


    for event in events:

        event_direction = normalize_direction(

            event.get(
                "direction"
            )

        )


        if event.get("event") in (

            "BOS",

            "CHoCH",

        ):

            if event_direction == direction:

                return True



    return False



# ==========================================================
# LIQUIDITY CONFIRMATION
# ==========================================================

def liquidity_swept(
    liquidity,
    direction,
):
    """
    Check liquidity sweep.
    """

    if not liquidity:

        return False



    direction = normalize_direction(
        direction
    )


    if isinstance(
        liquidity,
        dict
    ):

        sweeps = liquidity.get(
            "sweeps",
            []
        )


    else:

        sweeps = getattr(

            liquidity,

            "sweeps",

            []

        )



    for sweep in sweeps:

        sweep_direction = normalize_direction(

            sweep.get(
                "direction",
                ""
            )

        )


        if sweep_direction == direction:

            return True



    return False



# ==========================================================
# CHECK OBJECT EXISTS
# ==========================================================

def exists(
    value,
):
    """
    Safe existence check.
    """

    return value is not None



# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "normalize_direction",

    "get_order_block_direction",

    "get_fvg_direction",

    "directions_align",

    "structure_is_confirmed",

    "liquidity_swept",

    "exists",

]