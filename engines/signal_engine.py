def get_trade_bias(trend):
    """
    Decide whether KAI should BUY, SELL, or WAIT
    based on the current trend
    """

    if trend == "📈 Bull":
        return "📈 BUY"
    
    elif trend == "📉 Bear":
        return "📉 SELL"
    
    else:
        return "⏸️  WAIT"
    
    # Decide trade bias
    signal = signal_engine.get_trade_bias(trend)