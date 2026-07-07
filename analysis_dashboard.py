import config
from datetime import datetime

def show_analysis(
    symbol,
    timeframe,
    latest_candle,
    ma50,
    ma200,
    trend,
    market_structure,
    pattern,
    support,
    resistance,
    signal,
):
    
    print("=" * config.LINE_WIDTH)
    print(f"Market Analysis : {symbol}")
    print("=" * config.LINE_WIDTH)

    print(f"Timeframe         : {timeframe}")
    print(f"Time              : {datetime.fromtimestamp(latest_candle['time'])}")
    print(f"Open              : {latest_candle['open']:.5f}")
    print(f"High              : {latest_candle['high']:.5f}")
    print(f"Low               : {latest_candle['low']:.5f}")
    print(f"Close             : {latest_candle['close']:.5f}")
    print(f"Volume            : {latest_candle['tick_volume']:.2f}")

    print("-" * config.LINE_WIDTH)

    print(f"MA50              : {ma50:.5f}")
    print(f"MA200             : {ma200:.5f}")
    print(f"Trend             : {trend}")
    print(f"Market Structure  : {market_structure}")
    print(f"Pattern           : {pattern}")

    print("-" * config.LINE_WIDTH)

    print(f"Support           : {support:.5f}")
    print(f"Resistance        : {resistance:.5f}")

    print("-" * config.LINE_WIDTH)

    print(f"Trade Decision    : {signal}")

    print("=" * config.LINE_WIDTH)
    print()