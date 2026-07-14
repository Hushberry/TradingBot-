"""
=========================================================
KAI Smart Money AI

Swing Engine

detector.py

Institutional Swing Detection

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations



from .models import (

    SwingPoint,

    SwingCollection,

)



from .constants import (

    SWING_LEFT,

    SWING_RIGHT,

    SWING_HIGH,

    SWING_LOW,

)



from .utils import (

    is_swing_high,

    is_swing_low,

    valid_distance,

)



# ==========================================================
# DETECT SWING HIGHS
# ==========================================================

def detect_swing_highs(
    candles,
    left: int = SWING_LEFT,
    right: int = SWING_RIGHT,
):
    """
    Detect swing high points.
    """

    swings = []



    last_price = None



    for index in range(

        left,

        len(candles) - right

    ):


        if not is_swing_high(

            candles,

            index,

            left,

            right,

        ):

            continue



        price = float(

            candles.iloc[index]["high"]

        )



        if last_price is not None:


            if not valid_distance(

                price,

                last_price,

            ):

                continue



        swing = SwingPoint(

            index=index,

            timestamp=str(

                candles.iloc[index].get(

                    "time",

                    ""

                )

            ),

            price=price,

            swing_type=SWING_HIGH,

        )


        swing.add_reason(

            "Confirmed swing high"

        )


        swings.append(

            swing

        )


        last_price = price



    return swings



# ==========================================================
# DETECT SWING LOWS
# ==========================================================

def detect_swing_lows(
    candles,
    left: int = SWING_LEFT,
    right: int = SWING_RIGHT,
):
    """
    Detect swing low points.
    """

    swings = []



    last_price = None



    for index in range(

        left,

        len(candles) - right

    ):


        if not is_swing_low(

            candles,

            index,

            left,

            right,

        ):

            continue



        price = float(

            candles.iloc[index]["low"]

        )



        if last_price is not None:


            if not valid_distance(

                price,

                last_price,

            ):

                continue



        swing = SwingPoint(

            index=index,

            timestamp=str(

                candles.iloc[index].get(

                    "time",

                    ""

                )

            ),

            price=price,

            swing_type=SWING_LOW,

        )


        swing.add_reason(

            "Confirmed swing low"

        )


        swings.append(

            swing

        )


        last_price = price



    return swings



# ==========================================================
# CLASSIFY SWINGS
# ==========================================================

def classify_swings(
    swings,
):
    """
    Separate internal and external swings.

    Latest major extremes become external.
    """

    if not swings:

        return swings



    highest = max(

        swings,

        key=lambda x: x.price

    )


    lowest = min(

        swings,

        key=lambda x: x.price

    )



    highest.classification = "external"

    lowest.classification = "external"



    for swing in swings:

        if swing not in (

            highest,

            lowest,

        ):

            swing.classification = "internal"



    return swings



# ==========================================================
# MASTER DETECTOR
# ==========================================================

def detect_swings(
    candles,
):
    """
    Detect all swing points.
    """



    highs = detect_swing_highs(

        candles

    )


    lows = detect_swing_lows(

        candles

    )



    all_swings = (

        highs

        +

        lows

    )



    classify_swings(

        all_swings

    )



    return SwingCollection(

        highs=highs,

        lows=lows,

    )



# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "detect_swing_highs",

    "detect_swing_lows",

    "detect_swings",

]