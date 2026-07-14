"""
=========================================================
KAI Smart Money AI

Fair Value Gap Engine

lifecycle.py

FVG Lifecycle Management

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations


import pandas as pd


from .models import FairValueGap


from .utils import (
    price_inside_gap,
)



# ==========================================================
# CHECK TEST
# ==========================================================

def check_fvg_test(
    fvg: FairValueGap,
    candles: pd.DataFrame,
) -> bool:
    """
    Check if price returned
    into the FVG zone.
    """

    start = (
        fvg.created_index + 1
    )


    for i in range(
        start,
        len(candles)
    ):

        candle = candles.iloc[i]


        if price_inside_gap(

            float(candle["high"]),

            fvg.top,

            fvg.bottom,

        ):

            return True



        if price_inside_gap(

            float(candle["low"]),

            fvg.top,

            fvg.bottom,

        ):

            return True


    return False



# ==========================================================
# CHECK FILLED
# ==========================================================

def check_fvg_filled(
    fvg: FairValueGap,
    candles: pd.DataFrame,
) -> bool:
    """
    Determine if FVG is completely filled.
    """

    start = (
        fvg.created_index + 1
    )


    for i in range(

        start,

        len(candles)

    ):

        candle = candles.iloc[i]


        high = float(
            candle["high"]
        )

        low = float(
            candle["low"]
        )


        # Bullish FVG filled

        if fvg.direction == "bullish":

            if low <= fvg.bottom:

                return True



        # Bearish FVG filled

        else:

            if high >= fvg.top:

                return True


    return False



# ==========================================================
# INVALIDATION
# ==========================================================

def check_fvg_invalidated(
    fvg: FairValueGap,
    candles: pd.DataFrame,
) -> bool:
    """
    Check if FVG failed.
    """

    start = (
        fvg.created_index + 1
    )


    for i in range(

        start,

        len(candles)

    ):

        candle = candles.iloc[i]


        close = float(
            candle["close"]
        )


        # Bullish failure

        if fvg.direction == "bullish":

            if close < fvg.bottom:

                return True



        # Bearish failure

        else:

            if close > fvg.top:

                return True


    return False



# ==========================================================
# UPDATE SINGLE FVG
# ==========================================================

def update_fvg_status(
    fvg: FairValueGap,
    candles: pd.DataFrame,
) -> FairValueGap:
    """
    Update FVG lifecycle.
    """


    if check_fvg_invalidated(

        fvg,

        candles,

    ):

        fvg.invalidated = True

        fvg.status = "invalid"

        return fvg



    if check_fvg_filled(

        fvg,

        candles,

    ):

        fvg.filled = True

        fvg.status = "filled"

        return fvg



    if check_fvg_test(

        fvg,

        candles,

    ):

        fvg.tested = True

        fvg.status = "tested"



    return fvg



# ==========================================================
# UPDATE MANY
# ==========================================================

def update_fvgs(
    fvgs,
    candles,
):
    """
    Update lifecycle for all FVGs.
    """

    updated = []


    for fvg in fvgs:

        updated.append(

            update_fvg_status(

                fvg,

                candles,

            )

        )


    return updated



# ==========================================================
# ACTIVE FVG
# ==========================================================

def active_fvgs(
    fvgs,
):
    """
    Return usable FVGs.
    """

    return [

        fvg

        for fvg in fvgs

        if not fvg.invalidated

        and not fvg.filled

    ]



# ==========================================================
# FRESH FVG
# ==========================================================

def fresh_fvgs(
    fvgs,
):
    """
    Return untouched FVGs.
    """

    return [

        fvg

        for fvg in fvgs

        if fvg.status == "fresh"

    ]



# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "check_fvg_test",

    "check_fvg_filled",

    "check_fvg_invalidated",

    "update_fvg_status",

    "update_fvgs",

    "active_fvgs",

    "fresh_fvgs",

]