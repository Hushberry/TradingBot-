"""
======================================================
KAI Smart Money AI
Swing Structure Engine V2.0

Purpose:
- Detect swing highs and lows
- Classify market structure points
- Prepare data for Market Structure Engine

Author: Vincent Chimezirim
======================================================
"""

import pandas as pd
import numpy as np


# ==============================
# CONFIGURATION
# ==============================

SWING_LOOKBACK = 2
ATR_PERIOD = 14

MAJOR_DISTANCE = 1.5
MINOR_DISTANCE = 0.8

MIN_STRENGTH = 40


# ==============================
# VALIDATION
# ==============================

def validate_candles(candles):

    required = [
        "open",
        "high",
        "low",
        "close"
    ]

    if not isinstance(candles, pd.DataFrame):
        raise TypeError("Candles must be a pandas DataFrame")

    for column in required:
        if column not in candles.columns:
            raise ValueError(
                f"Missing candle column: {column}"
            )

    return candles.reset_index(drop=True)



# ==============================
# ATR CALCULATION
# ==============================

def calculate_atr(candles, period=ATR_PERIOD):

    high = candles["high"]
    low = candles["low"]
    close = candles["close"]

    tr = pd.concat(
        [
            high - low,
            abs(high - close.shift()),
            abs(low - close.shift())
        ],
        axis=1
    ).max(axis=1)

    atr = tr.rolling(period).mean()

    return atr.fillna(0)



# ==============================
# CANDLE STRENGTH
# ==============================

def calculate_candle_strength(candle):

    body = abs(
        candle["close"] -
        candle["open"]
    )

    total = (
        candle["high"] -
        candle["low"]
    )

    if total == 0:
        return 0

    strength = (
        body / total
    ) * 100

    return round(strength,2)



# ==============================
# SWING HIGH DETECTION
# ==============================

def find_swing_highs(candles):

    swings = []

    for i in range(
        SWING_LOOKBACK,
        len(candles)-SWING_LOOKBACK
    ):

        current = candles["high"][i]

        left = candles["high"][
            i-SWING_LOOKBACK:i
        ]

        right = candles["high"][
            i+1:
            i+SWING_LOOKBACK+1
        ]

        if (
            current > left.max()
            and
            current > right.max()
        ):

            swings.append(
                {
                    "index": i,
                    "price": current,
                    "type": "swing_high"
                }
            )

    return swings



# ==============================
# SWING LOW DETECTION
# ==============================

def find_swing_lows(candles):

    swings = []

    for i in range(
        SWING_LOOKBACK,
        len(candles)-SWING_LOOKBACK
    ):

        current = candles["low"][i]

        left = candles["low"][
            i-SWING_LOOKBACK:i
        ]

        right = candles["low"][
            i+1:
            i+SWING_LOOKBACK+1
        ]


        if (
            current < left.min()
            and
            current < right.min()
        ):

            swings.append(
                {
                    "index": i,
                    "price": current,
                    "type": "swing_low"
                }
            )

    return swings



# ==============================
# SWING STRENGTH
# ==============================

def calculate_swing_strength(
        candles,
        swing,
        atr
):

    index = swing["index"]

    if index >= len(candles)-1:
        return 0


    reaction = abs(
        candles["close"][index+1]
        -
        swing["price"]
    )


    atr_value = atr[index]


    if atr_value == 0:
        return 0


    score = (
        reaction /
        atr_value
    ) * 50


    score += calculate_candle_strength(
        candles.iloc[index]
    ) / 2


    return min(
        round(score,2),
        100
    )

# ==============================
# CLASSIFY SWING TYPE
# ==============================

def classify_swing_type(
        swing,
        strength
):

    if strength >= 75:
        classification = "major"

    elif strength >= 50:
        classification = "minor"

    else:
        classification = "weak"


    swing["strength"] = strength
    swing["classification"] = classification

    return swing



# ==============================
# REMOVE DUPLICATE SWINGS
# ==============================

def remove_duplicate_swings(swings):

    unique = []
    indexes = set()

    for swing in swings:

        if swing["index"] not in indexes:

            unique.append(swing)
            indexes.add(
                swing["index"]
            )

    return unique



# ==============================
# DETECT MAJOR SWINGS
# ==============================

def detect_major_swings(swings):

    return [
        swing
        for swing in swings
        if swing["classification"] == "major"
    ]



# ==============================
# DETECT MINOR SWINGS
# ==============================

def detect_minor_swings(swings):

    return [
        swing
        for swing in swings
        if swing["classification"] == "minor"
    ]



# ==============================
# INTERNAL STRUCTURE POINTS
# ==============================

def detect_internal_structure_points(
        highs,
        lows
):

    internal_highs = []
    internal_lows = []


    for high in highs:

        if high["classification"] != "major":
            internal_highs.append(high)


    for low in lows:

        if low["classification"] != "major":
            internal_lows.append(low)


    return (
        internal_highs,
        internal_lows
    )



# ==============================
# EXTERNAL STRUCTURE POINTS
# ==============================

def detect_external_structure_points(
        highs,
        lows
):

    external_highs = []
    external_lows = []


    for high in highs:

        if high["classification"] == "major":
            external_highs.append(high)


    for low in lows:

        if low["classification"] == "major":
            external_lows.append(low)


    return (
        external_highs,
        external_lows
    )



# ==============================
# PROTECTED LEVELS
# ==============================

def detect_protected_levels(
        highs,
        lows
):

    protected_highs = []
    protected_lows = []


    # Last major swing becomes
    # structural reference

    major_highs = [
        x for x in highs
        if x["classification"] == "major"
    ]

    major_lows = [
        x for x in lows
        if x["classification"] == "major"
    ]


    if major_highs:

        high = major_highs[-1]

        high["protected"] = True

        protected_highs.append(high)


    if major_lows:

        low = major_lows[-1]

        low["protected"] = True

        protected_lows.append(low)


    return (
        protected_highs,
        protected_lows
    )



# ==============================
# BUILD SWING DATA
# ==============================

def build_swing_data(
        highs,
        lows
):

    major_highs = detect_major_swings(highs)

    major_lows = detect_major_swings(lows)


    minor_highs = detect_minor_swings(highs)

    minor_lows = detect_minor_swings(lows)


    internal_highs, internal_lows = (
        detect_internal_structure_points(
            highs,
            lows
        )
    )


    external_highs, external_lows = (
        detect_external_structure_points(
            highs,
            lows
        )
    )


    protected_highs, protected_lows = (
        detect_protected_levels(
            highs,
            lows
        )
    )


    return {

        "swing_highs": highs,

        "swing_lows": lows,


        "major_highs": major_highs,

        "major_lows": major_lows,


        "minor_highs": minor_highs,

        "minor_lows": minor_lows,


        "internal_highs": internal_highs,

        "internal_lows": internal_lows,


        "external_highs": external_highs,

        "external_lows": external_lows,


        "protected_highs": protected_highs,

        "protected_lows": protected_lows

    }



# ==============================
# MAIN SWING ENGINE
# ==============================

def detect_swings(candles):

    candles = validate_candles(
        candles
    )


    atr = calculate_atr(
        candles
    )


    highs = find_swing_highs(
        candles
    )

    lows = find_swing_lows(
        candles
    )


    processed_highs = []

    for swing in highs:

        strength = calculate_swing_strength(
            candles,
            swing,
            atr
        )

        processed_highs.append(
            classify_swing_type(
                swing,
                strength
            )
        )



    processed_lows = []

    for swing in lows:

        strength = calculate_swing_strength(
            candles,
            swing,
            atr
        )

        processed_lows.append(
            classify_swing_type(
                swing,
                strength
            )
        )



    processed_highs = remove_duplicate_swings(
        processed_highs
    )

    processed_lows = remove_duplicate_swings(
        processed_lows
    )


    return build_swing_data(
        processed_highs,
        processed_lows
    )