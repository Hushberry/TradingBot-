"""
======================================================
KAI Smart Money AI
Liquidity Engine V2.0

Purpose:
- Detect institutional liquidity areas
- Identify equal highs/lows
- Detect liquidity pools
- Detect liquidity sweeps

Author: Vincent Chimezirim
======================================================
"""


# ==============================
# CONFIGURATION
# ==============================

EQUAL_TOLERANCE = 0.00020
MIN_TOUCHES = 2



# ==============================
# VALIDATION
# ==============================

def validate_candles(candles):

    required = [
        "high",
        "low",
        "close"
    ]

    for column in required:

        if column not in candles.columns:

            raise ValueError(
                f"Missing candle column: {column}"
            )

    return candles



# ==============================
# PRICE DISTANCE
# ==============================

def price_distance(
        price1,
        price2
):

    return abs(
        price1 - price2
    )



# ==============================
# EQUAL HIGH DETECTION
# ==============================

def detect_equal_highs(
        swing_highs
):

    equal_highs = []


    for i in range(
        len(swing_highs)
    ):

        base = swing_highs[i]


        touches = 1


        for j in range(
            i + 1,
            len(swing_highs)
        ):

            compare = swing_highs[j]


            distance = price_distance(
                base["price"],
                compare["price"]
            )


            if distance <= EQUAL_TOLERANCE:

                touches += 1



        if touches >= MIN_TOUCHES:


            equal_highs.append(

                {
                    "price":
                        base["price"],

                    "type":
                        "equal_high",

                    "side":
                        "buy_side",

                    "touches":
                        touches,

                    "swept":
                        False

                }

            )


    return equal_highs



# ==============================
# EQUAL LOW DETECTION
# ==============================

def detect_equal_lows(
        swing_lows
):

    equal_lows = []


    for i in range(
        len(swing_lows)
    ):

        base = swing_lows[i]


        touches = 1


        for j in range(
            i + 1,
            len(swing_lows)
        ):

            compare = swing_lows[j]


            distance = price_distance(
                base["price"],
                compare["price"]
            )


            if distance <= EQUAL_TOLERANCE:

                touches += 1



        if touches >= MIN_TOUCHES:


            equal_lows.append(

                {
                    "price":
                        base["price"],

                    "type":
                        "equal_low",

                    "side":
                        "sell_side",

                    "touches":
                        touches,

                    "swept":
                        False

                }

            )


    return equal_lows


# ==============================
# BUY-SIDE LIQUIDITY
# ==============================

def detect_buy_side_liquidity(
        swing_highs
):

    liquidity = []


    for high in swing_highs:

        liquidity.append(

            {
                "price":
                    high["price"],

                "type":
                    "swing_high_liquidity",

                "side":
                    "buy_side",

                "index":
                    high["index"],

                "swept":
                    False
            }

        )


    return liquidity



# ==============================
# SELL-SIDE LIQUIDITY
# ==============================

def detect_sell_side_liquidity(
        swing_lows
):

    liquidity = []


    for low in swing_lows:

        liquidity.append(

            {
                "price":
                    low["price"],

                "type":
                    "swing_low_liquidity",

                "side":
                    "sell_side",

                "index":
                    low["index"],

                "swept":
                    False
            }

        )


    return liquidity



# ==============================
# PREVIOUS HIGH / LOW LIQUIDITY
# ==============================

def detect_previous_high_low(
        candles
):

    previous = {}


    if len(candles) < 2:

        return previous



    previous["previous_high"] = {

        "price":
            candles["high"].iloc[-2],

        "type":
            "previous_high",

        "side":
            "buy_side",

        "swept":
            False
    }



    previous["previous_low"] = {

        "price":
            candles["low"].iloc[-2],

        "type":
            "previous_low",

        "side":
            "sell_side",

        "swept":
            False
    }


    return previous



# ==============================
# LIQUIDITY STRENGTH
# ==============================

def calculate_liquidity_strength(
        liquidity
):

    score = 0


    touches = liquidity.get(
        "touches",
        1
    )


    score += touches * 20


    if liquidity.get("type") in [

        "equal_high",

        "equal_low"

    ]:

        score += 30



    return min(
        score,
        100
    )



# ==============================
# APPLY LIQUIDITY SCORE
# ==============================

def score_liquidity(
        liquidity_list
):

    scored = []


    for item in liquidity_list:


        item["strength"] = (
            calculate_liquidity_strength(
                item
            )
        )


        scored.append(item)


    return scored



# ==============================
# BUILD LIQUIDITY POOLS
# ==============================

def build_liquidity_pools(
        buy_side,
        sell_side,
        equal_highs,
        equal_lows
):

    pools = []


    pools.extend(
        buy_side
    )


    pools.extend(
        sell_side
    )


    pools.extend(
        equal_highs
    )


    pools.extend(
        equal_lows
    )



    return score_liquidity(
        pools
    )


# ==============================
# DETECT LIQUIDITY SWEEP
# ==============================

def detect_liquidity_sweep(
        candles,
        liquidity_pools
):

    sweeps = []


    for liquidity in liquidity_pools:

        price = liquidity["price"]


        for i in range(len(candles)):

            high = candles["high"].iloc[i]

            low = candles["low"].iloc[i]

            close = candles["close"].iloc[i]



            # BUY SIDE LIQUIDITY TAKEN

            if liquidity["side"] == "buy_side":

                if high > price and close < price:

                    sweep = {

                        "event":
                            "liquidity_sweep",

                        "direction":
                            "bearish",

                        "liquidity_type":
                            liquidity["type"],

                        "price":
                            price,

                        "candle_index":
                            i,

                        "reason":
                            "Buy-side liquidity taken and rejected"

                    }


                    liquidity["swept"] = True

                    sweeps.append(
                        sweep
                    )



            # SELL SIDE LIQUIDITY TAKEN

            elif liquidity["side"] == "sell_side":


                if low < price and close > price:


                    sweep = {


                        "event":
                            "liquidity_sweep",


                        "direction":
                            "bullish",


                        "liquidity_type":
                            liquidity["type"],


                        "price":
                            price,


                        "candle_index":
                            i,


                        "reason":
                            "Sell-side liquidity taken and rejected"

                    }


                    liquidity["swept"] = True


                    sweeps.append(
                        sweep
                    )


    return sweeps



# ==============================
# STOP HUNT DETECTION
# ==============================

def detect_stop_hunt(
        sweeps
):

    stop_hunts = []


    for sweep in sweeps:


        stop_hunts.append(

            {

                "event":
                    "stop_hunt",


                "direction":
                    sweep["direction"],


                "price":
                    sweep["price"],


                "reason":
                    "Liquidity sweep followed by rejection"

            }

        )


    return stop_hunts



# ==============================
# BUILD LIQUIDITY DATA
# ==============================

def build_liquidity_data(
        candles,
        swing_data
):


    swing_highs = (
        swing_data["swing_highs"]
    )


    swing_lows = (
        swing_data["swing_lows"]
    )


    equal_highs = detect_equal_highs(
        swing_highs
    )


    equal_lows = detect_equal_lows(
        swing_lows
    )


    buy_side = detect_buy_side_liquidity(
        swing_highs
    )


    sell_side = detect_sell_side_liquidity(
        swing_lows
    )


    previous = detect_previous_high_low(
        candles
    )


    pools = build_liquidity_pools(

        buy_side,

        sell_side,

        equal_highs,

        equal_lows

    )


    pools.extend(
        previous.values()
    )


    sweeps = detect_liquidity_sweep(

        candles,

        pools

    )


    stop_hunts = detect_stop_hunt(
        sweeps
    )



    return {


        "equal_highs":

            equal_highs,


        "equal_lows":

            equal_lows,


        "buy_side_liquidity":

            buy_side,


        "sell_side_liquidity":

            sell_side,


        "previous_high_low":

            previous,


        "liquidity_pools":

            pools,


        "sweeps":

            sweeps,


        "stop_hunts":

            stop_hunts

    }



# ==============================
# MAIN LIQUIDITY FUNCTION
# ==============================

def detect_liquidity(
        candles,
        swing_data
):

    candles = validate_candles(
        candles
    )


    return build_liquidity_data(

        candles,

        swing_data

    )