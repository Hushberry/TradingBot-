"""
=========================================================
KAI Smart Money AI

Institutional Order Block Engine

statistics.py

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations

from typing import List

from .models import OrderBlock


# ==========================================================
# TOTAL
# ==========================================================

def total_order_blocks(
    order_blocks: List[OrderBlock],
) -> int:
    """
    Total Order Blocks.
    """

    return len(order_blocks)


# ==========================================================
# BULLISH
# ==========================================================

def bullish_order_blocks(
    order_blocks: List[OrderBlock],
) -> List[OrderBlock]:

    return [

        ob

        for ob in order_blocks

        if ob.direction == "bullish"

    ]


# ==========================================================
# BEARISH
# ==========================================================

def bearish_order_blocks(
    order_blocks: List[OrderBlock],
) -> List[OrderBlock]:

    return [

        ob

        for ob in order_blocks

        if ob.direction == "bearish"

    ]


# ==========================================================
# ACTIVE
# ==========================================================

def active_order_blocks(
    order_blocks: List[OrderBlock],
) -> List[OrderBlock]:

    return [

        ob

        for ob in order_blocks

        if not ob.invalidated

    ]


# ==========================================================
# FRESH
# ==========================================================

def fresh_order_blocks(
    order_blocks: List[OrderBlock],
) -> List[OrderBlock]:

    return [

        ob

        for ob in order_blocks

        if ob.status == "fresh"

    ]


# ==========================================================
# MITIGATED
# ==========================================================

def mitigated_order_blocks(
    order_blocks: List[OrderBlock],
) -> List[OrderBlock]:

    return [

        ob

        for ob in order_blocks

        if ob.mitigated

    ]


# ==========================================================
# INVALIDATED
# ==========================================================

def invalidated_order_blocks(
    order_blocks: List[OrderBlock],
) -> List[OrderBlock]:

    return [

        ob

        for ob in order_blocks

        if ob.invalidated

    ]


# ==========================================================
# AVERAGE SCORE
# ==========================================================

def average_score(
    order_blocks: List[OrderBlock],
) -> float:

    if not order_blocks:
        return 0.0

    return (

        sum(
            ob.score
            for ob in order_blocks
        )

        / len(order_blocks)

    )


# ==========================================================
# STRONGEST
# ==========================================================

def strongest_order_block(
    order_blocks: List[OrderBlock],
):

    if not order_blocks:
        return None

    return max(
        order_blocks,
        key=lambda x: x.score,
    )


# ==========================================================
# SUMMARY
# ==========================================================

def order_block_summary(
    order_blocks: List[OrderBlock],
) -> dict:
    """
    Institutional summary.
    """

    return {

        "total": total_order_blocks(
            order_blocks,
        ),

        "bullish": len(
            bullish_order_blocks(
                order_blocks,
            )
        ),

        "bearish": len(
            bearish_order_blocks(
                order_blocks,
            )
        ),

        "active": len(
            active_order_blocks(
                order_blocks,
            )
        ),

        "fresh": len(
            fresh_order_blocks(
                order_blocks,
            )
        ),

        "mitigated": len(
            mitigated_order_blocks(
                order_blocks,
            )
        ),

        "invalidated": len(
            invalidated_order_blocks(
                order_blocks,
            )
        ),

        "average_score": round(
            average_score(
                order_blocks,
            ),
            2,
        ),

        "strongest": strongest_order_block(
            order_blocks,
        ),

    }


# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "total_order_blocks",

    "bullish_order_blocks",

    "bearish_order_blocks",

    "active_order_blocks",

    "fresh_order_blocks",

    "mitigated_order_blocks",

    "invalidated_order_blocks",

    "average_score",

    "strongest_order_block",

    "order_block_summary",

]