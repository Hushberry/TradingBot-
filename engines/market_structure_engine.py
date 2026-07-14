"""
======================================================
KAI Smart Money AI
Market Structure Engine V1.0

Purpose:
- Detect BOS
- Detect CHoCH
- Determine trend
- Analyze market structure

Author: Vincent Chimezirim
======================================================
"""


# ==============================
# CONFIGURATION
# ==============================

BOS_CONFIDENCE = 70
CHOCH_CONFIDENCE = 75



# ==============================
# VALIDATION
# ==============================

def validate_swing_data(swing_data):

    required = [
        "swing_highs",
        "swing_lows",
        "protected_highs",
        "protected_lows"
    ]

    for item in required:

        if item not in swing_data:
            raise ValueError(
                f"Missing swing data: {item}"
            )

    return swing_data



# ==============================
# GET LAST LEVEL
# ==============================

def get_last_swing(levels):

    if not levels:
        return None

    return levels[-1]



# ==============================
# STRUCTURE DIRECTION
# ==============================

def determine_trend(
        swing_data
):

    highs = swing_data["swing_highs"]

    lows = swing_data["swing_lows"]


    if len(highs) < 2 or len(lows) < 2:

        return "neutral"



    previous_high = highs[-2]["price"]

    current_high = highs[-1]["price"]


    previous_low = lows[-2]["price"]

    current_low = lows[-1]["price"]



    if (
        current_high > previous_high
        and
        current_low > previous_low
    ):

        return "bullish"



    elif (
        current_high < previous_high
        and
        current_low < previous_low
    ):

        return "bearish"



    return "range"



# ==============================
# CHECK BULLISH BOS
# ==============================

def detect_bullish_bos(
        swing_data,
        current_price
):

    protected_highs = (
        swing_data["protected_highs"]
    )


    if not protected_highs:

        return None



    level = protected_highs[-1]


    if current_price > level["price"]:

        return {

            "event": "BOS",

            "direction": "bullish",

            "structure": "external",

            "broken_level": level["price"],

            "confidence": BOS_CONFIDENCE

        }


    return None



# ==============================
# CHECK BEARISH BOS
# ==============================

def detect_bearish_bos(
        swing_data,
        current_price
):

    protected_lows = (
        swing_data["protected_lows"]
    )


    if not protected_lows:

        return None



    level = protected_lows[-1]


    if current_price < level["price"]:

        return {

            "event": "BOS",

            "direction": "bearish",

            "structure": "external",

            "broken_level": level["price"],

            "confidence": BOS_CONFIDENCE

        }


    return None

# ==============================
# DETECT BULLISH CHoCH
# ==============================

def detect_bullish_choch(
        swing_data,
        current_price
):

    trend = determine_trend(
        swing_data
    )


    protected_highs = (
        swing_data["protected_highs"]
    )


    if trend != "bearish":
        return None


    if not protected_highs:
        return None


    level = protected_highs[-1]


    if current_price > level["price"]:

        return {

            "event": "CHoCH",

            "direction": "bullish",

            "previous_trend": "bearish",

            "structure": "external",

            "broken_level": level["price"],

            "confidence": CHOCH_CONFIDENCE

        }


    return None



# ==============================
# DETECT BEARISH CHoCH
# ==============================

def detect_bearish_choch(
        swing_data,
        current_price
):

    trend = determine_trend(
        swing_data
    )


    protected_lows = (
        swing_data["protected_lows"]
    )


    if trend != "bullish":
        return None


    if not protected_lows:
        return None


    level = protected_lows[-1]


    if current_price < level["price"]:

        return {

            "event": "CHoCH",

            "direction": "bearish",

            "previous_trend": "bullish",

            "structure": "external",

            "broken_level": level["price"],

            "confidence": CHOCH_CONFIDENCE

        }


    return None



# ==============================
# INTERNAL STRUCTURE BREAK
# ==============================

def detect_internal_structure_break(
        swing_data,
        current_price
):

    internal_highs = (
        swing_data["internal_highs"]
    )

    internal_lows = (
        swing_data["internal_lows"]
    )


    events = []


    if internal_highs:

        high = internal_highs[-1]


        if current_price > high["price"]:

            events.append({

                "event": "internal_BOS",

                "direction": "bullish",

                "level": high["price"]

            })



    if internal_lows:

        low = internal_lows[-1]


        if current_price < low["price"]:

            events.append({

                "event": "internal_BOS",

                "direction": "bearish",

                "level": low["price"]

            })


    return events



# ==============================
# STRUCTURE STRENGTH
# ==============================

def calculate_structure_strength(
        swing_data
):

    score = 0


    major_highs = len(
        swing_data["major_highs"]
    )

    major_lows = len(
        swing_data["major_lows"]
    )


    protected = (
        len(
            swing_data["protected_highs"]
        )
        +
        len(
            swing_data["protected_lows"]
        )
    )


    score += min(
        major_highs * 15,
        40
    )


    score += min(
        major_lows * 15,
        40
    )


    score += protected * 10


    return min(
        score,
        100
    )



# ==============================
# BUILD MARKET STRUCTURE
# ==============================

def build_market_structure(
        swing_data,
        current_price
):

    trend = determine_trend(
        swing_data
    )


    bullish_bos = detect_bullish_bos(
        swing_data,
        current_price
    )


    bearish_bos = detect_bearish_bos(
        swing_data,
        current_price
    )


    bullish_choch = detect_bullish_choch(
        swing_data,
        current_price
    )


    bearish_choch = detect_bearish_choch(
        swing_data,
        current_price
    )


    internal_breaks = (
        detect_internal_structure_break(
            swing_data,
            current_price
        )
    )


    events = []


    for event in [
        bullish_bos,
        bearish_bos,
        bullish_choch,
        bearish_choch

    ]:

        if event:

            events.append(event)



    events.extend(
        internal_breaks
    )



    return {

        "trend": trend,

        "events": events,

        "structure_strength":
            calculate_structure_strength(
                swing_data
            )

    }



# ==============================
# MAIN FUNCTION
# ==============================

def analyze_structure(
        swing_data,
        current_price
):

    swing_data = validate_swing_data(
        swing_data
    )


    return build_market_structure(
        swing_data,
        current_price
    )