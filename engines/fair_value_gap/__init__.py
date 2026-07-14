"""
=========================================================
KAI Smart Money AI

Fair Value Gap Engine

Package Initializer

Author: Vincent Chimezirim
=========================================================
"""


from .engine import (

    FairValueGapEngine,

)


from .models import (

    FairValueGap,

)


from .detector import (

    find_fair_value_gaps,

    detect_bullish_fvg,

    detect_bearish_fvg,

)


from .validator import (

    validate_fvg,

    validate_fvgs,

)


from .scorer import (

    calculate_fvg_score,

    score_fvgs,

)


from .lifecycle import (

    update_fvg_status,

    update_fvgs,

)


from .statistics import (

    fvg_summary,

)



__all__ = [

    "FairValueGapEngine",

    "FairValueGap",

    "find_fair_value_gaps",

    "detect_bullish_fvg",

    "detect_bearish_fvg",

    "validate_fvg",

    "validate_fvgs",

    "calculate_fvg_score",

    "score_fvgs",

    "update_fvg_status",

    "update_fvgs",

    "fvg_summary",

]