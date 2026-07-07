import MetaTrader5 as mt5
from datetime import datetime

from config import LINE_WIDTH


def get_timeframe_name(timeframe):
    """
    Convert MetaTrader 5 timeframe constant to a human-readable string.
    """
    timeframe_names = {
        mt5.TIMEFRAME_M1: "1M",
        mt5.TIMEFRAME_M5: "5M",
        mt5.TIMEFRAME_M15: "15M",
        mt5.TIMEFRAME_M30: "30M",
        mt5.TIMEFRAME_H1: "1H",
        mt5.TIMEFRAME_H4: "4H",
        mt5.TIMEFRAME_D1: "1 Day",
        mt5.TIMEFRAME_W1: "1 Week",
        mt5.TIMEFRAME_MN1: "1 Month"
    }
    return timeframe_names.get(timeframe, "Unknown Timeframe")

def get_historical_candles(symbol, timeframe, count=500):
    """
    Get historical candle data from MetaTrader 5.
    """

    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, count)
    if rates is None:
        print(mt5.last_error())
        return None

    print("=" * LINE_WIDTH)
    print("      Historical Candles      ")
    print("=" * LINE_WIDTH)

    print(f"Symbol          : {symbol}")
    print(f"Timeframe       : {get_timeframe_name(timeframe)}")
    print(f"Candles         : {len(rates   )}")

    print("=" * LINE_WIDTH)

    latest = rates[-1]

    print(f"Latest rates:")
    print("-" * LINE_WIDTH)

    print(f"Time        : {datetime.fromtimestamp(latest['time'])}")
    print(f"Open        : {latest['open']:.5f}")
    print(f"High        : {latest['high']:.5f}")
    print(f"Low         : {latest['low']:.5f}")
    print(f"Close       : {latest['close']:.5f}")
    print(f"Volume      : {latest['tick_volume']:.2f}")

    print("=" * LINE_WIDTH)

    return rates
