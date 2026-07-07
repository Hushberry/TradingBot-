def get_trade_bias(trend):
    """
    Decide whether KAI should BUY, SELL, or WAIT
    based on the current trend
    """

    if trend == "📈 Uptrend":
        return "📈 BUY"
    
    elif trend == "📉 Downtrend":
        return "📉 SELL"
    
    else:
        return "⏸️ WAIT"