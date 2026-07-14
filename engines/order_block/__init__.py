"""
=========================================================
KAI Smart Money AI

Institutional Order Block Engine

Package Initializer

Author: Vincent Chimezirim
=========================================================
"""


from .engine import (
    InstitutionalOrderBlockEngine,
)


from .detector import (
    detect_order_blocks,
)


from .candidate_detector import (
    find_candidate_order_blocks,
)


from .validator import (
    validate_order_block,
)


from .scorer import (
    calculate_order_block_score,
    score_candidates,
)


from .lifecycle import (
    update_order_blocks,
)


from .statistics import (
    order_block_summary,
)


__all__ = [

    "InstitutionalOrderBlockEngine",

    "detect_order_blocks",

    "find_candidate_order_blocks",

    "validate_order_block",

    "calculate_order_block_score",

    "score_candidates",

    "update_order_blocks",

    "order_block_summary",

]