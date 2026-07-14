"""
=========================================================
KAI Smart Money AI

Swing Engine

utils.py

Swing Detection Utilities

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations



from engines.common.candle_utils import (

    get_candle,

)



from .constants import (

    MIN_SWING_DISTANCE,

)



# ==========================================================
# PRICE DISTANCE
# ==========================================================

def price_distance(
    first: float,
    second: float,
):
    """
    Calculate distance between prices.
    """

    return abs(

        first - second

    )



# ==========================================================
# CHECK DISTANCE
# ==========================================================

def valid_distance(
    first: float,
    second: float,
):
    """
    Prevent duplicate swings.
    """

    return (

        price_distance(

            first,

            second,

        )

        >=

        MIN_SWING_DISTANCE

    )



# ==========================================================
# SWING HIGH CHECK
# ==========================================================

def is_swing_high(
    candles,
    index: int,
    left: int = 2,
    right: int = 2,
):
    """
    Determine if candle is swing high.
    """

    if index < left:

        return False


    if index + right >= len(candles):

        return False



    current = float(

        candles.iloc[index]["high"]

    )



    # Left side check

    for i in range(

        index - left,

        index

    ):

        if float(

            candles.iloc[i]["high"]

        ) >= current:

            return False



    # Right side check

    for i in range(

        index + 1,

        index + right + 1

    ):

        if float(

            candles.iloc[i]["high"]

        ) >= current:

            return False



    return True



# ==========================================================
# SWING LOW CHECK
# ==========================================================

def is_swing_low(
    candles,
    index: int,
    left: int = 2,
    right: int = 2,
):
    """
    Determine if candle is swing low.
    """

    if index < left:

        return False


    if index + right >= len(candles):

        return False



    current = float(

        candles.iloc[index]["low"]

    )



    # Left side check

    for i in range(

        index - left,

        index

    ):

        if float(

            candles.iloc[i]["low"]

        ) <= current:

            return False



    # Right side check

    for i in range(

        index + 1,

        index + right + 1

    ):

        if float(

            candles.iloc[i]["low"]

        ) <= current:

            return False



    return True



# ==========================================================
# CANDLE BODY SIZE
# ==========================================================

def candle_body(
    candle,
):
    """
    Return candle body size.
    """

    return abs(

        float(candle["close"])

        -

        float(candle["open"])

    )



# ==========================================================
# CANDLE RANGE
# ==========================================================

def candle_range(
    candle,
):
    """
    Return candle range.
    """

    return abs(

        float(candle["high"])

        -

        float(candle["low"])

    )



# ==========================================================
# BODY STRENGTH
# ==========================================================

def body_strength(
    candle,
):
    """
    Measure candle strength.
    """

    rng = candle_range(
        candle
    )


    if rng == 0:

        return 0



    return (

        candle_body(candle)

        /

        rng

    ) * 100



# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "price_distance",

    "valid_distance",

    "is_swing_high",

    "is_swing_low",

    "candle_body",

    "candle_range",

    "body_strength",

]