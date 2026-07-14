import pandas as pd

def find_support(candles, lookback=20):
    """
    Find the nearest support level.

    Parameters:
        rate (list): Historical candle data.
        lookback (int): Number of Candles to inspect.

    Returns:
        Float: Lowest low in the lookback period.
    """

    if candles is None or len(candles) < lookback:
        return None
    
    if not isinstance(candles, pd.DataFrame):
        candles = pd.DataFrame(candles)

    recent = candles.tail(lookback)

    return recent["low"].min()
    


def find_resistance(candles, lookback=20):
    """
    Find the nearest resistance level.

    Parameters:
        rates (list): Historical candle data.
        lookback (int): Number of candles to inspect.

    Returns:
        Float: Highest high in the lookback period.
    """

    if candles is None or len(candles) < lookback:
        return None
    
    if not isinstance(candles, pd.DataFrame):
        candles = pd.DataFrame(candles)

    recent = candles.tail(lookback)

    return recent["high"].max()
