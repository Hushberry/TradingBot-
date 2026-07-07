import config
import logger
import mt5_connector
import dashboard
import MetaTrader5 as mt5
import candle_engine
import trend_engine
import pattern_engine
import support_engine
import signal_engine
import analysis_dashboard


print("=" * config.LINE_WIDTH)
print(f"Welcome to {config.BOT_NAME}")
print(f"Version: {config.VERSION}")
print(f"Author: {config.AUTHOR}")
print("=" * 50)

logger.log("KAI_Bot has started.")

mt5_connector.connect_to_mt5()
account = mt5.account_info()

dashboard.show_dashboard(account)

SYMBOLS = [
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

TIMEFRAME = mt5.TIMEFRAME_H1
CANDLE_COUNT = 500
TIMEFRAME_NAME = candle_engine.get_timeframe_name(TIMEFRAME)

for symbol in SYMBOLS:
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

for symbol in SYMBOLS:

    rates = candle_engine.get_historical_candles(
        symbol,
        TIMEFRAME,
        CANDLE_COUNT 
    )

    if rates is None:
        continue

    latest_candle = rates[-1]
    latest_price = latest_candle["close"]

    ma50 = trend_engine.calculate_ma(rates, 50)
    ma200 = trend_engine.calculate_ma(rates, 200)

    trend = trend_engine.analyze_trend(
        latest_price,
        ma50,
        ma200
    )

    market_structure = trend_engine.get_market_structure(rates)

    pattern = pattern_engine.analyze_patterns(rates)

    support = support_engine.find_support(rates)
    resistance = support_engine.find_resistance(rates)

    signal = signal_engine.get_trade_bias(trend)


    analysis_dashboard.show_analysis(
        symbol,
        candle_engine.get_timeframe_name(TIMEFRAME),
        latest_candle,
        ma50,
        ma200,
        trend,
        market_structure,
        pattern,
        support,
        resistance,
        signal,
    )
