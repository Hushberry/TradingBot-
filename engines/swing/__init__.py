"""
=========================================================
KAI Smart Money AI

Swing Engine

Package Initializer

Author: Vincent Chimezirim
=========================================================
"""


from .engine import (

    SwingEngine,

)


from .models import (

    SwingPoint,

    SwingCollection,

)


from .detector import (

    detect_swings,

    detect_swing_highs,

    detect_swing_lows,

)


from .validator import (

    validate_swing,

    validate_swings,

)


from .scorer import (

    score_swing,

    score_swings,

    calculate_swing_score,

)


from .lifecycle import (

    update_swing,

    update_swings,

    active_swings,

)


from .statistics import (

    swing_summary,

)



__all__ = [

    "SwingEngine",

    "SwingPoint",

    "SwingCollection",

    "detect_swings",

    "detect_swing_highs",

    "detect_swing_lows",

    "validate_swing",

    "validate_swings",

    "score_swing",

    "score_swings",

    "calculate_swing_score",

    "update_swing",

    "update_swings",

    "active_swings",

    "swing_summary",

]