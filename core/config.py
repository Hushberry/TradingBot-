# ==================================
# TradingBot Configuration File
# ==================================
import MetaTrader5 as mt5

# ======================================================
# KAI SMART MONEY AI
# ======================================================

BOT_NAME = "KAI Smart Money AI"

BOT_SUBTITLE = "Institutional Trading Intelligence"

VERSION = "3.0"

AUTHOR = "Vincent Chimezirim"

TAGLINE = "Powered by Smart Money Concepts + AI"

RELEASE = "Core Engine"

SYMBOLS = ["XAUUSDm", "EURUSDm", "GBPUSDm"]
TIMEFRAMES = ["M1", "M5", "M15", "H1", "H4", "D1"]
RISK_PER_TRADE = 0.07

LINE_WIDTH = 100
LABEL_WIDTH = 18

TIMEFRAME = mt5.TIMEFRAME_H1
HIGHER_TIMEFRAME = mt5.TIMEFRAME_H4
CANDLE_COUNT = 500

FAST_MA = 50
SLOW_MA = 200

