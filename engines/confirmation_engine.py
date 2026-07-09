"""
confirmation_engine.py
Confirms trade setups using multiple indicators.
"""

def calculate_trade_score(
    trend,
    pattern,
    market_structure,
    mtf_confirmation,
    signal,
):

    score = 0

    # -------------------------
    # Trend
    # -------------------------
    if trend in ["📈 Uptrend", "📉 Downtrend"]:
        score += 1

    # -------------------------
    # Structure
    # -------------------------
    if market_structure in [
        "Higher Highs",
        "Lower Highs",
    ]:
        score += 1

    # -------------------------
    # Candlestick Pattern
    # -------------------------
    bullish = [
        "Hammer",
        "Bullish Engulfing",
    ]

    bearish = [
        "Shooting Star",
        "Bearish Engulfing",
    ]

    if pattern in bullish + bearish:
        score += 1

    # -------------------------
    # Multi Timeframe
    # -------------------------
    if mtf_confirmation == "✅ Confirmed":
        score += 1

    # -------------------------
    # Signal
    # -------------------------
    if signal in [
        "📈 BUY",
        "📉 SELL",
    ]:
        score += 1

    # ----------------------------------
    # Final Confidence
    # ----------------------------------

    confidence = score

    # Never exceed 5 stars
    if confidence > 5:
        confidence = 5

    stars = "⭐" * confidence + "☆" * (5 - confidence)

    percent = confidence * 20

    return {
        "score": score,
        "confidence": confidence,
        "rating": stars,
        "percent": percent,
    }