"""
=========================================================
KAI Smart Money AI

Fair Value Gap Engine

constants.py

Institutional FVG Parameters
=========================================================
"""


# Minimum gap size relative to price
MIN_GAP_SIZE = 0.00010


# Minimum strength score
MIN_FVG_SCORE = 60


# Maximum lifecycle age
MAX_FVG_AGE = 500


# Validation tolerance
PRICE_TOLERANCE = 0.00020


# Score weights

DISPLACEMENT_WEIGHT = 30

GAP_SIZE_WEIGHT = 25

STRUCTURE_WEIGHT = 20

VOLUME_WEIGHT = 15

FRESHNESS_WEIGHT = 10