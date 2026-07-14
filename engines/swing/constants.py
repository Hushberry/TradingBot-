"""
=========================================================
KAI Smart Money AI

Swing Engine

constants.py

Swing Detection Parameters

Author: Vincent Chimezirim
=========================================================
"""


# ==========================================================
# SWING SETTINGS
# ==========================================================

# Number of candles required
# on both sides of a swing

SWING_LEFT = 2

SWING_RIGHT = 2



# Minimum distance between swings

MIN_SWING_DISTANCE = 0.00020



# Maximum historical swings

MAX_SWINGS = 500



# ==========================================================
# SWING TYPES
# ==========================================================

SWING_HIGH = "swing_high"

SWING_LOW = "swing_low"



# ==========================================================
# CLASSIFICATION
# ==========================================================

INTERNAL = "internal"

EXTERNAL = "external"



# ==========================================================
# VALIDATION
# ==========================================================

MIN_SWING_SCORE = 60