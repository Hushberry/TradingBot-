"""
=========================================================
KAI Smart Money AI

Confluence Engine

Package Initializer

Author: Vincent Chimezirim
=========================================================
"""


from .engine import (

    ConfluenceEngine,

)


from .models import (

    ConfluenceResult,

)


from .analyzer import (

    analyze_confluence,

)


from .scoring import (

    score_confluence,

    score_breakdown,

)


from .filters import (

    apply_filters,

)


from .decision import (

    create_trade_decision,

)



__all__ = [

    "ConfluenceEngine",

    "ConfluenceResult",

    "analyze_confluence",

    "score_confluence",

    "score_breakdown",

    "apply_filters",

    "create_trade_decision",

]