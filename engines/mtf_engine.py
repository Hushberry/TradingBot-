
from engines import candle_engine
from engines import trend_engine
import config


def get_timeframe_trend(symbol, timeframe):
    rates = candle_engine.get_historical_candles(
        symbol,
        timeframe,
        config.CANDLE_COUNT
    )

    if rates is None:
        return None
    
    latest_price = rates[-1]["close"]

    fast_ma = trend_engine.calculate_ma(rates, config.FAST_MA)
    slow_ma = trend_engine.calculate_ma(rates, config.SLOW_MA)

    trend = trend_engine.analyze_trend(
        latest_price,
        fast_ma,
        slow_ma,
    )

    return trend

def compare_trends(h1_trend, h4_trend):
    """
    Compare H1 and H4 trends.
    """

    if h1_trend == h4_trend:
        return "✅ Confirmed"
    
    return "🚩 Conflict"