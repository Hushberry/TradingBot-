"""
entry_engine.py

Determines the best trade entry.
"""

def get_entry_price(signal, latest_candle):

    if signal == "📈 BUY":
        return latest_candle["high"]
    
    elif signal == "📉 SELL":
        return latest_candle["low"]
    
    return latest_candle["close"]