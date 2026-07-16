"""
=========================================================
KAI Smart Money AI
File: config.py

Description:
------------
Global configuration settings for KAI.

This file stores all configurable values used
throughout the application.

Author: Vincent Chimezirim
Version: 1.0.0
=========================================================
"""

from pathlib import Path

from dotenv import load_dotenv

import os


# =========================================================
# Load Environment Variables
# =========================================================

load_dotenv()


# =========================================================
# Application
# =========================================================

APP_NAME = "KAI Smart Money AI"

VERSION = "1.0.0"

DEBUG = True


# =========================================================
# Project Directories
# =========================================================

BASE_DIR = Path(__file__).resolve().parent

LOG_DIR = BASE_DIR / "logs"

STORAGE_DIR = BASE_DIR / "storage"

CACHE_DIR = STORAGE_DIR / "cache"

HISTORY_DIR = STORAGE_DIR / "historical_data"


# =========================================================
# MetaTrader 5
# =========================================================

MT5_LOGIN = os.getenv("MT5_LOGIN")

MT5_PASSWORD = os.getenv("MT5_PASSWORD")

MT5_SERVER = os.getenv("MT5_SERVER")

MT5_TERMINAL_PATH = os.getenv("MT5_TERMINAL_PATH")


# =========================================================
# Market Settings
# =========================================================

DEFAULT_SYMBOLS = [

    "EURUSD",
    "GBPUSD",
    "USDJPY",
    "AUDUSD",
    "USDCAD",
    "USDCHF",
    "NZDUSD",
    "XAUUSD",
]

DEFAULT_TIMEFRAMES = [

    "D1",
    "H4",
    "H1",
    "M15",
]

CANDLE_HISTORY = 500


# =========================================================
# Analysis Settings
# =========================================================

SWING_LENGTH = 5

MIN_SWING_DISTANCE = 3

FVG_MIN_SIZE = 0.0


# =========================================================
# Scanner Settings
# =========================================================

SCAN_INTERVAL = 60


# =========================================================
# Logging
# =========================================================

LOG_LEVEL = "INFO"

LOG_FILE = LOG_DIR / "kai.log"