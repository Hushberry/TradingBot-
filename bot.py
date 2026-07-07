import config
import logger
import mt5_connector
import dashboard
import MetaTrader5 as mt5
import candle_engine
import trend_engine
import pattern_engine


print("=" * config.LINE_WIDTH)
print(f"Welcome to {config.BOT_NAME}")
print(f"Version: {config.VERSION}")
print(f"Author: {config.AUTHOR}")
print("=" * 50)

logger.log("KAI_Bot has started.")

mt5_connector.connect_to_mt5()
account = mt5.account_info()

dashboard.show_dashboard(account)

symbols = [
     "XAUUSDm",
     "EURUSDm",
     "GBPUSDm",
     "USDJPYm",
     "USDCHFm",
     "USDCADm",
     "UKOILm",
     "USOILm",
     "BTCUSDm",
     "ETHUSDm",
]

for symbol in symbols:
    info = mt5.symbol_info(symbol)
    tick = mt5.symbol_info_tick(symbol)

    if info is None or tick is None:
        continue

    spread = (tick.ask - tick.bid) / info.point

    dashboard.show_market(
        symbol,
        tick.bid,
        tick.ask,
        spread, 
        tick.volume,
    )
dashboard.finish_dashboard()

print()

for symbol in symbols:

    rates = candle_engine.get_historical_candles(
        symbol,
        mt5.TIMEFRAME_H1,
        500
    )

    if rates is None:
        continue

    latest_price = rates[-1]["close"]

    ma50 = trend_engine.calculate_ma(rates, 50)
    ma200 = trend_engine.calculate_ma(rates, 200)

    trend = trend_engine.analyze_trend(
        latest_price,
        ma50,
        ma200
    )

    market_structure = trend_engine.get_market_structure(rates)

    pattern = pattern_engine.analyze_patterns(rates)

    print()
    print("=" * config.LINE_WIDTH)
    print(f"Market Analysis : {symbol}")
    print("=" * config.LINE_WIDTH)

    print(f"Current Price      : {latest_price:.5f}")
    print(f"MA50               : {ma50:.5f}")
    print(f"MA200              : {ma200:.5f}")
    print(f"Trend              : {trend}")
    print(f"Market Structure   : {market_structure}")
    print(f"Pattern            : {pattern}")

