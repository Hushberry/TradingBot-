"""
=========================================================
KAI Smart Money AI

Integration Layer

Package Initializer

Author: Vincent Chimezirim
=========================================================
"""


from integration.pipeline import (

    KAIAnalysisPipeline,

)


from integration.analyzer import (

    analyze_market,

)



__all__ = [

    "KAIAnalysisPipeline",

    "analyze_market",

]