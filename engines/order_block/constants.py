"""
=========================================================
KAI Smart Money AI
Institutional Order Block Engine

constants.py

Global configuration and thresholds used by the
Order Block Engine.

Author: Vincent Chimezirim
=========================================================
"""

# =========================================================
# GENERAL
# =========================================================

ENGINE_NAME = "Institutional Order Block Engine"

ENGINE_VERSION = "1.0"

DEBUG = False

# =========================================================
# DATA VALIDATION
# =========================================================

REQUIRED_COLUMNS = (
    "open",
    "high",
    "low",
    "close",
)

OPTIONAL_COLUMNS = (
    "tick_volume",
    "spread",
    "real_volume",
    "time",
)

# =========================================================
# SWING SETTINGS
# =========================================================

LOOKBACK_CANDLES = 500

LOOKAHEAD_CANDLES = 3

MIN_HISTORY = 50

# =========================================================
# DISPLACEMENT
# =========================================================

MIN_BODY_RATIO = 0.60

MIN_EXPANSION_MULTIPLIER = 1.50

MIN_DISPLACEMENT_SCORE = 70

MIN_DISPLACEMENT_DISTANCE = 1.0

# =========================================================
# ORDER BLOCK
# =========================================================

MAX_ORDER_BLOCK_SIZE = 3

MIN_ORDER_BLOCK_SIZE = 1

MAX_RETESTS = 2

MAX_ORDER_BLOCK_AGE = 300

# =========================================================
# VALIDATION
# =========================================================

REQUIRE_STRUCTURE_CONFIRMATION = True

REQUIRE_LIQUIDITY_CONFIRMATION = False

REQUIRE_DISPLACEMENT = True

REQUIRE_STRONG_BODY = True

# =========================================================
# SCORING
# =========================================================

MAX_SCORE = 100

MIN_ACCEPTED_SCORE = 75

GRADE_A = 90

GRADE_B = 80

GRADE_C = 70

GRADE_D = 60

# =========================================================
# WEIGHTS
# =========================================================

WEIGHT_DISPLACEMENT = 25

WEIGHT_STRUCTURE = 25

WEIGHT_LIQUIDITY = 20

WEIGHT_BODY = 15

WEIGHT_FRESHNESS = 10

WEIGHT_VOLUME = 5

# =========================================================
# STATUS
# =========================================================

STATUS_FRESH = "fresh"

STATUS_MITIGATED = "mitigated"

STATUS_INVALID = "invalid"

# =========================================================
# TYPES
# =========================================================

BULLISH = "bullish"

BEARISH = "bearish"

# =========================================================
# DEBUG
# =========================================================

PRINT_REJECTED = True

PRINT_ACCEPTED = True

PRINT_STATISTICS = True

PRINT_PROCESSING_TIME = True