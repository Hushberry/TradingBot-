"""
=====================================================
KAI SMART MONEY AI
Core Scoring Engine
Author : Vincent Chimezirim
Version : 3.0
=====================================================

Purpose
-------
This module combines every analysis engine into
one institutional confidence score.

Every future Smart Money module (Order Blocks,
Liquidity Sweeps, Fair Value Gaps, BOS, CHoCH,
Premium/Discount Zones, etc.) will feed into
this scoring engine.
"""
"""
=====================================================
KAI SMART MONEY AI
Core Scoring Engine
Author : Vincent Chimezirim
Version : 3.0
=====================================================
"""
TREND_WEIGHT = 20
PATTERN_WEIGHT = 20
STRUCTURE_WEIGHT = 15
MTF_WEIGHT = 15
EMA_WEIGHT = 15


def calculate_score(
    trend,
    pattern,
    structure,
    mtf_confirmation,
    ma50,
    ma200,
    price,
):

    score = 0

    # ===============================
    # Trend
    # ===============================

    if trend == "🚀 Bull":
        score += TREND_WEIGHT

    elif trend == "📉 Bear":
        score += TREND_WEIGHT

    elif trend == "↕️ Pullback":
        score += 10

    elif trend == "↔️ Sideways":
        score += 5

    # ===============================
    # Candlestick Pattern
    # ===============================

    if pattern == "Bullish Engulfing":
        score += PATTERN_WEIGHT

    elif pattern == "Bearish Engulfing":
        score += PATTERN_WEIGHT

    elif pattern == "Hammer":
        score += 15

    elif pattern == "Shooting Star":
        score += 15

    elif pattern == "Morning Star":
        score += 18

    elif pattern == "Evening Star":
        score += 18

    elif pattern == "Doji":
        score += 5

    # ===============================
    # Market Structure
    # ===============================

    if structure == "Higher Highs":
        score += STRUCTURE_WEIGHT

    elif structure == "Lower Lows":
        score += STRUCTURE_WEIGHT

    elif structure == "Higher Lows":
        score += 10

    elif structure == "Lower Highs":
        score += 10

    elif structure == "↔️ Sideways":
        score += 5

    # ===============================
    # Multi-Timeframe Confirmation
    # ===============================

    if mtf_confirmation == "✅ Confirmed":
        score += MTF_WEIGHT

    # ===============================
    # EMA / MA Alignment
    # ===============================

    if trend == "🚀 Bull":

        if price > ma50 > ma200:
            score += EMA_WEIGHT

        elif price > ma50:
            score += 8

    elif trend == "📉 Bear":

        if price < ma50 < ma200:
            score += EMA_WEIGHT

        elif price < ma50:
            score += 8

    # ===============================
    # Normalize Score
    # ===============================

    MAX_SCORE = 85

    percent = round((score / MAX_SCORE) * 100)
    percent = min(percent, 100)

    return {
        "score": score,
        "percent": percent,
        "grade": get_grade(percent),
    }


def get_grade(score):

    if score >= 90:
        return "A+"

    elif score >= 80:
        return "A"

    elif score >= 70:
        return "B+"

    elif score >= 60:
        return "B"

    elif score >= 50:
        return "C+"

    elif score >= 40:
        return "C"

    elif score >= 30:
        return "D"

    return "F"