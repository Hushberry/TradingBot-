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
        score += 20

    elif trend == "🟡 Pullback":
        score += 10

    else:
        score += 5

    # -------------------------
    # Structure
    # -------------------------
    if market_structure  == "Higher Highs":
        score += 20

    elif market_structure == "Lower Lows":
        score += 20

    elif market_structure in [
        "Higher Lows",
        "Lower Highs",
    ]:
        score += 15

    else:
        score += 5
 

    # -------------------------
    # Candlestick Pattern
    # -------------------------

    strong_patterns = [
        "Bullish Engulfing",
        "Bearish Engulfing",
    ]

    medium_patterns = [
        "Morning Star",
        "Evening Star",
    ]

    weak_patterns = [
        "Hammer",
        "Shooting Star",
    ]

    if pattern in strong_patterns:
        score += 20

    elif pattern in medium_patterns:
        score += 18

    elif pattern in weak_patterns:
        score += 15

    elif pattern == "Doji":
        score += 5

    else:
        score += 0

    # -------------------------
    # Multi Timeframe
    # -------------------------
    if mtf_confirmation == "✅ Confirmed":
        score += 25

    # -------------------------
    # Signal
    # -------------------------
    if signal in [ "📈 BUY", "📉 SELL"]:
        score += 15

    # ----------------------------------
    # Final Confidence
    # ----------------------------------

    percent = min(score, 100)

    confidence = percent // 20

    stars = "⭐" * confidence + "☆" * (5 - confidence)

    return {
        "score": score,
        "confidence": confidence,
        "rating": stars,
        "percent": percent,
    }