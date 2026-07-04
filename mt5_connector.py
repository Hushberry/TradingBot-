import MetaTrader5 as mt5

def connect_to_mt5():
    print("Connecting to MetaTrader 5...")

    if not mt5.initialize():
        print("Failed to initialize MetaTrader 5. Error code:", mt5.last_error())
        return False

    print("Successfully connected to MetaTrader 5.")
    return True

def get_account_info():
    account_info = mt5.account_info()
    if account_info is None:
        print("Failed to retrieve account information. Error code:", mt5.last_error())
        return
    
    print("========= Account Information ==========")
    print(f"Login: {account_info.login}")
    print(f"Name: {account_info.name}")
    print(f"Server: {account_info.server}")
    print(f"Balance: {account_info.balance}")
    print(f"Equity: {account_info.equity}")
    print(f"Margin: {account_info.margin}")
    print(f"Leverage: {account_info.leverage}")
    print(f"Currency: {account_info.currency}")
    print("=" * 50)

def get_symbol_info(symbol):
   info = mt5.symbol_info(symbol)
   print(info)
   print(mt5.last_error())

   tick = mt5.symbol_info_tick(symbol)
   
   if tick is None:
        print(f"Unable to retrieve tick data for {symbol}. Error code:", mt5.last_error())
        return
   
   symbol_info = mt5.symbol_info(symbol)
   spread_points = (tick.ask - tick.bid) / symbol_info.point
    
   print("\n========= Market Data ==========")
   print(f"Symbol: {symbol}")
   print(f"Bid: {tick.bid}")
   print(f"Ask: {tick.ask}")
   print (f"Time: {tick.time}")
   print(f"Volume: {tick.volume}")
   print(f"Spread: {spread_points:.1f} points")
   print(f"Last: {tick.last}")
   print("===================================")    

def get_multiple_symbols(symbols):
    print("\n========= Live Market Data ==========")

    for symbol in symbols:

        info = mt5.symbol_info(symbol)

        if info is None:
            print(f"{symbol:<10} ❌ Symbol not found.")
            continue

        tick = mt5.symbol_info_tick(symbol)

        if tick is None:
            print(f"{symbol:<10} ❌ Tick Unavailable. Error code:", mt5.last_error())
            continue

        if tick.bid == 0 or tick.ask == 0:
            print(f"{symbol:<10} ❌ No live market data available.")
            continue

        spread = (tick.ask - tick.bid) / info.point

        print(
            f"{symbol:<10}"
            f"Bid: {tick.bid:<10}"
            f"Ask: {tick.ask:<10}"
            f"Spread: {spread:.1f} points"
        )

    print("===================================")