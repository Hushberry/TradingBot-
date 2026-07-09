import MetaTrader5 as mt5

def calculate_ma(rates, period):
    """

    Calculate a Simple moving average (SMA) using the closing prices.
    """

    close = []

    for candle in rates[-period:]:
        close.append(candle['close'])

    ma = sum(close) / period
    return ma


def is_bullish(price, ma50, ma200):
    """
    Return True if the marker is bullish, False otherwise.
    """
    if price > ma50 and ma50 > ma200:
        return True
    return False

def is_bearish(price, ma50, ma200):
    """
    Return True if the marker is bearish, False otherwise.
    """
    if price < ma50 and ma50 < ma200:
        return True
    return False
    
def analyze_trend(price, ma50, ma200):
   if price > ma50 and ma50 > ma200:
       return "📈 Bull"
   
   elif price < ma50 and ma50 < ma200:
       return "📉 Bear"
   
   else:
       return "🟡 Pullback"

def get_market_structure(rates):
    """
    Analyze the last few candles to determine the market structure (higher highs, lower lows, etc.).
    """

    last = rates[-2]
    previous = rates[-3]
    older = rates[-4]

    if (
        last['high'] > previous['high']
        and previous['high'] > older['high']
    ):
        return "Higher Highs"
    elif (
        last["high"] < previous["high"]
        and previous["high"] < older["high"]
    ):
        return "Lower Highs"
    return "↔️ Sideways"







# Temporary test (we'll remove this later)

# ma50 = calculate_ma(rates, 50)
# print(ma50)