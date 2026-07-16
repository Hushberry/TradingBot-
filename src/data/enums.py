"""
=========================================================
KAI Smart Money AI

Defines all enumerations used throughout KAI.

Enums provide fixed values that improve code safety,
readability, and consistency across all modules.

Author: Vincent Chimezirim
Version: 1.0.0
=========================================================
"""

from enum import Enum

#----------------------------------------
# Market Trend
#----------------------------------------

class Trend(Enum):
    """Market trend direction."""

    BULLISH = "Bullish"
    BEARISH = "Bearish"
    RANGE = "Range"

    
#------------------------------------------------------
# Swing Type
#------------------------------------------------------
class SwingType(Enum):
    """Type of market swing."""

    HIGH = "High"
    LOW = "Low"

#------------------------------------------------------
# Structure Event
#------------------------------------------------------

class StructureEvent(Enum):
    """Market structure event."""

    BOS = "Break of Structure"
    CHOCH = "Change of Character"
    NONE = "None"


#-----------------------------------------------------
# Liquidity Type 
#-----------------------------------------------------

class LiquidityType(Enum):
    """Liquidity classification."""

    BUY_SIDE = "Buy Side"
    SELL_SIDE = "Sell Side"
    EQUAL_HIGHS = "Equal Highs"
    EQUAL_LOWS = "Equal Lows"
    PREVIOUS_DAY_HIGH = "Previous Day High"
    PREVIOUS_DAY_LOW = "Previous Day Low"
    PREVIOUS_WEEK_HIGH = "Previous Week High"
    PREVIOUS_WEEK_LOW = "Previous Week Low"


#--------------------------------------------------
# Fair Value Gap
#--------------------------------------------------

class FairValueGapType(Enum):
    """Fair Value Gap direction"""

    BULLISH = "Bullish"
    BEARISH = "Bearish"

#--------------------------------------------------
# Order Block
#--------------------------------------------------

class OrderBlockType(Enum):
    """Order Block direction."""

    BULLISH = "Bullish"
    BEARISH = "Bearish"


#---------------------------------------------------
# Premium / Discount
#---------------------------------------------------

class PriceZone(Enum):
    """Current price location."""

    PREMIUM = "Premium"
    EQUILIBRIUM = "Equilibrium"
    DISCOUNT = "Discount"


#---------------------------------------------------
# Market Session 
#---------------------------------------------------

class MarketSession(Enum):
    """Trading session."""

    ASIAN = "Asian"
    LONDON = "London"
    NEW_YORK = "New York"
    OVERLAP = "London/New York Overlap"
    CLOSED = "Closed"


#-----------------------------------------------------
# Confidence Level
#-----------------------------------------------------

class ConfidenceLevel(Enum):
    """Analysis confidence."""

    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    VERY_HIGH = "Very High"