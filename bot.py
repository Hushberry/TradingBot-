import config
import logger
import mt5_connector
import dashboard
import MetaTrader5 as mt5

print("=" * 50)
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