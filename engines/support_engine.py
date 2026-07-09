def find_support(rates, lookback=20):
    """
    Find the nearest support level.

    Parameters:
        rate (list): Historical candle data.
        lookback (int): Number of Candles to inspect.

    Returns:
        Float: Lowest low in the lookback period.
    """

    lows = []

    for candle in rates[-lookback:]:
        lows.append(candle["low"])

    support = min(lows)

    return support


def find_resistance(rates, lookback=20):
    """
    Find the nearest resistance level.

    Parameters:
        rates (list): Historical candle data.
        lookback (int): Number of candles to inspect.

    Returns:
        Float: Highest high in the lookback period.
    """

    highs = []

    for candle in rates[-lookback:]:
        highs.append(candle["high"])

    resistance = max(highs)

    return resistance
