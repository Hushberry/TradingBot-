"""
=========================================================
KAI Smart Money AI

Fair Value Gap Engine

detector.py

Institutional FVG Detection

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations

import uuid

import pandas as pd


from .models import FairValueGap


from .utils import (

    is_bullish_fvg,

    is_bearish_fvg,

    bullish_gap_zone,

    bearish_gap_zone,

    calculate_gap_size,

    calculate_gap_percent,

    gap_quality,

)



# ==========================================================
# BUILD FVG OBJECT
# ==========================================================

def build_fvg(
    candles,
    index: int,
    direction: str,
) -> FairValueGap:
    """
    Create Fair Value Gap object.
    """

    if direction == "bullish":

        zone = bullish_gap_zone(
            candles,
            index,
        )

    else:

        zone = bearish_gap_zone(
            candles,
            index,
        )


    gap_size = calculate_gap_size(

        zone["top"],

        zone["bottom"],

    )


    price = float(
        candles.iloc[index]["close"]
    )


    fvg = FairValueGap()


    fvg.id = str(
        uuid.uuid4()
    )


    fvg.created_index = index


    if "time" in candles.columns:

        fvg.created_time = str(

            candles.iloc[index]["time"]

        )


    fvg.direction = direction


    fvg.top = zone["top"]

    fvg.bottom = zone["bottom"]

    fvg.midpoint = zone["midpoint"]


    fvg.size = gap_size


    fvg.size_percent = calculate_gap_percent(

        gap_size,

        price,

    )


    fvg.score = gap_quality(

        candles,

        index,

    )


    fvg.reasons.append(

        f"{direction} FVG detected"

    )


    return fvg



# ==========================================================
# DETECT BULLISH FVG
# ==========================================================

def detect_bullish_fvg(
    candles,
    index: int,
):
    """
    Detect bullish FVG.
    """

    if not is_bullish_fvg(
        candles,
        index,
    ):

        return None


    return build_fvg(

        candles,

        index,

        "bullish",

    )



# ==========================================================
# DETECT BEARISH FVG
# ==========================================================

def detect_bearish_fvg(
    candles,
    index: int,
):
    """
    Detect bearish FVG.
    """

    if not is_bearish_fvg(
        candles,
        index,
    ):

        return None


    return build_fvg(

        candles,

        index,

        "bearish",

    )



# ==========================================================
# FIND ALL FVG
# ==========================================================

def find_fair_value_gaps(
    candles: pd.DataFrame,
):
    """
    Scan complete dataset.
    """

    gaps = []


    for index in range(

        2,

        len(candles)

    ):

        bullish = detect_bullish_fvg(

            candles,

            index,

        )


        if bullish:

            gaps.append(
                bullish
            )



        bearish = detect_bearish_fvg(

            candles,

            index,

        )


        if bearish:

            gaps.append(
                bearish
            )


    return remove_duplicates(
        gaps
    )



# ==========================================================
# REMOVE DUPLICATES
# ==========================================================

def remove_duplicates(
    gaps,
):
    """
    Remove duplicate FVG zones.
    """

    unique = {}


    for gap in gaps:

        key = (

            gap.created_index,

            gap.direction,

            gap.top,

            gap.bottom,

        )


        unique[key] = gap


    return list(
        unique.values()
    )



# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "build_fvg",

    "detect_bullish_fvg",

    "detect_bearish_fvg",

    "find_fair_value_gaps",

]