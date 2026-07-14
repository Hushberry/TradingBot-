"""
=========================================================
KAI Smart Money AI

Swing Engine

lifecycle.py

Swing Lifecycle Management

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations



from .models import (

    SwingPoint,

)



# ==========================================================
# UPDATE AGE
# ==========================================================

def update_swing_age(
    swing: SwingPoint,
    current_index: int,
):
    """
    Calculate swing age.
    """

    swing.age = (

        current_index

        -

        swing.index

    )


    return swing



# ==========================================================
# CHECK BROKEN HIGH
# ==========================================================

def check_swing_high_broken(
    swing: SwingPoint,
    candles,
):
    """
    Check if a swing high was broken.
    """

    if swing.swing_type != "swing_high":

        return False



    for i in range(

        swing.index + 1,

        len(candles)

    ):

        high = float(

            candles.iloc[i]["high"]

        )


        if high > swing.price:

            swing.mark_broken()


            swing.add_reason(

                "Swing high liquidity broken"

            )


            return True



    return False



# ==========================================================
# CHECK BROKEN LOW
# ==========================================================

def check_swing_low_broken(
    swing: SwingPoint,
    candles,
):
    """
    Check if a swing low was broken.
    """

    if swing.swing_type != "swing_low":

        return False



    for i in range(

        swing.index + 1,

        len(candles)

    ):

        low = float(

            candles.iloc[i]["low"]

        )


        if low < swing.price:

            swing.mark_broken()


            swing.add_reason(

                "Swing low liquidity broken"

            )


            return True



    return False



# ==========================================================
# LIQUIDITY CHECK
# ==========================================================

def detect_liquidity_taken(
    swing: SwingPoint,
    candles,
):
    """
    Detect liquidity sweep.
    """

    broken = False



    if swing.swing_type == "swing_high":

        broken = check_swing_high_broken(

            swing,

            candles

        )



    elif swing.swing_type == "swing_low":

        broken = check_swing_low_broken(

            swing,

            candles

        )



    if broken:

        swing.liquidity_taken = True



    return swing



# ==========================================================
# UPDATE SINGLE SWING
# ==========================================================

def update_swing(
    swing: SwingPoint,
    candles,
):
    """
    Update lifecycle state.
    """

    update_swing_age(

        swing,

        len(candles)-1

    )


    detect_liquidity_taken(

        swing,

        candles

    )


    return swing



# ==========================================================
# UPDATE MANY
# ==========================================================

def update_swings(
    swings,
    candles,
):
    """
    Update all swings.
    """

    updated = []


    for swing in swings:

        updated.append(

            update_swing(

                swing,

                candles

            )

        )


    return updated



# ==========================================================
# ACTIVE SWINGS
# ==========================================================

def active_swings(
    swings,
):
    """
    Return valid active swings.
    """

    return [

        swing

        for swing in swings

        if swing.active

        and not swing.broken

    ]



# ==========================================================
# BROKEN SWINGS
# ==========================================================

def broken_swings(
    swings,
):
    """
    Return broken swings.
    """

    return [

        swing

        for swing in swings

        if swing.broken

    ]



# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "update_swing",

    "update_swings",

    "detect_liquidity_taken",

    "active_swings",

    "broken_swings",

]