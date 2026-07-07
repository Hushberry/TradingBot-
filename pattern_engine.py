import MetaTrader5 as mt5

def is_bullish_candle(candle):
    """
    Returns True if the candle is bullish (close > open), otherwise False.
    """

    if candle['close'] > candle['open']:
        return True
    return False


def is_bearish_candle(candle):
    """
    Returns True if the candle closed lower than it opened (close < open), otherwise False.
    """
    if candle['close'] < candle['open']:
        return True
    return False


def is_doji(candle):
    """
    Returns True if the candle body is very small.
    """
    body = abs(candle['close'] - candle['open'])
    total_range = candle['high'] - candle['low']
    if total_range == 0:
        return False 
    
    if body <= total_range * 0.10:
        return True
    return False


def is_hammer(candle):
    """
    Returns True if the candle looks like a hammer (small body, long lower shadow).
    """

    body = abs(candle['close'] - candle['open'])

    upper_wick = candle['high'] - max(
        candle['close'], 
        candle['open']
    )

    lower_wick = min(
        candle['close'],
        candle['open']
    ) - candle['low']

    if body == 0:
        return False
    
    if lower_wick >= body * 2 and upper_wick <= body:
        return True
    return False


def is_shooting_star(candle):
    """
    Returns True if the candle is a shooting star (small body, long upper shadow).
    """
    
    body = abs(candle['close'] - candle['open'])

    upper_wick = candle['high'] - max(
        candle['close'], 
        candle['open']
    )

    lower_wick = min(
        candle['close'],
        candle['open']
    ) - candle['low']

    if body == 0:
        return False
    
    if upper_wick >= body * 2 and lower_wick <= body:
        return True
    return False


def is_bullish_engulfing(previous, current):
    """
    Returns True if current candle engulfs previous bearish candle.
    """

    if not is_bearish_candle(previous):
        return False
    
    if not is_bullish_candle(current):
        return False
    
    if current["open"] < previous["close"] and current["close"] > previous["open"]:
        return True
    
    return False


def is_bearish_engulfing(previous, current):
    """
    Returns True if current candle engulfs previous bullish candle.
    """

    if not is_bullish_candle(previous):
        return False
    
    if not is_bearish_candle(current):
        return False
    
    if current["open"] > previous["close"] and current["close"] < previous["open"]:
        return True
    
    return False



def analyze_patterns(rates):
    """
    Scan latest candles and identify known patterns.
    """

    latest = rates[-1]
    previous = rates[-2]

    if is_hammer(latest):
        return "Hammer"
    
    if is_shooting_star(latest):
        return "Shooting Star"
    
    if is_doji(latest):
        return "Doji"
    
    if is_bullish_engulfing(previous, latest):
        return "Bullish Engulfing"
    
    if is_bearish_engulfing(previous, latest):
        return "Bearish Engulfing"
    
    return "No Pattern"