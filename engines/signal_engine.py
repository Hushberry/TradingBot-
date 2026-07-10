def get_trade_bias(trend):
    """
    Decide whether KAI should BUY, SELL, or WAIT
    based on the current trend
    """


    if trend == "🚀 Bull":
        return "✅ BUY"

    elif trend == "📉 Bear":
        return "🔴 SELL"

    return "⏯  WAIT"

