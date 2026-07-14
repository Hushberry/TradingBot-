"""
=========================================================
KAI Smart Money AI

Confluence Engine

decision.py

Trade Decision Generator

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations


from .models import (
    ConfluenceResult,
)


from .constants import (

    BUY,

    SELL,

    WAIT,

)



# ==========================================================
# DIRECTION DECISION
# ==========================================================

def determine_direction(
    result: ConfluenceResult,
):
    """
    Determine BUY / SELL direction.
    """


    if result.direction == "bullish":

        return BUY



    if result.direction == "bearish":

        return SELL



    return WAIT



# ==========================================================
# TRADE QUALITY
# ==========================================================

def trade_quality(
    result: ConfluenceResult,
):
    """
    Determine if setup quality is acceptable.
    """

    if result.score >= 90:

        return "A+"


    if result.score >= 80:

        return "A"


    if result.score >= 70:

        return "B"


    if result.score >= 60:

        return "C"


    return "D"



# ==========================================================
# AI MESSAGE
# ==========================================================

def generate_reasoning(
    result: ConfluenceResult,
):
    """
    Generate KAI explanation.
    """

    message = []


    if result.order_block_match:

        message.append(

            "Institutional Order Block detected"

        )


    if result.fair_value_gap_match:

        message.append(

            "Fair Value Gap alignment confirmed"

        )


    if result.liquidity_match:

        message.append(

            "Liquidity sweep confirmed"

        )


    if result.structure_match:

        message.append(

            "Market structure supports direction"

        )


    if result.volume_match:

        message.append(

            "Volume confirms participation"

        )


    return message



# ==========================================================
# CREATE DECISION
# ==========================================================

def create_trade_decision(
    result: ConfluenceResult,
):
    """
    Create final KAI trade output.
    """

    signal = determine_direction(
        result
    )


    result.grade = trade_quality(
        result
    )


    reasoning = generate_reasoning(
        result
    )


    return {

        "signal":

            signal,


        "direction":

            result.direction,


        "score":

            result.score,


        "confidence":

            result.confidence,


        "grade":

            result.grade,


        "entry":

            result.entry,


        "stop_loss":

            result.stop_loss,


        "take_profit":

            result.take_profit,


        "risk_reward":

            result.risk_reward,


        "reasoning":

            reasoning,


        "warnings":

            result.warnings,

    }



# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "determine_direction",

    "trade_quality",

    "generate_reasoning",

    "create_trade_decision",

]