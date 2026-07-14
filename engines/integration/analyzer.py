"""
=========================================================
KAI Smart Money AI

Integration Layer

analyzer.py

Final Analysis Formatter

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations



# ==========================================================
# MARKET BIAS
# ==========================================================

def get_market_bias(
    structure,
):
    """
    Extract market direction.
    """

    if not structure:

        return "neutral"



    if isinstance(
        structure,
        dict
    ):

        return structure.get(

            "trend",

            "neutral"

        )



    return getattr(

        structure,

        "trend",

        "neutral"

    )



# ==========================================================
# EXTRACT CONFLUENCE
# ==========================================================

def extract_confluence(
    confluence,
):
    """
    Extract final trade decision.
    """

    if not confluence:

        return {}



    if isinstance(
        confluence,
        dict
    ):

        return confluence.get(

            "signal",

            {}

        )



    return {}



# ==========================================================
# BUILD REPORT
# ==========================================================

def analyze_market(
    pipeline_result,
):
    """
    Create KAI final analysis report.
    """


    structure = pipeline_result.get(

        "market_structure"

    )


    confluence = pipeline_result.get(

        "confluence"

    )


    signal = {}


    if confluence:

        signal = confluence.get(

            "signal",

            {}

        )



    return {


        "market_bias":

            get_market_bias(

                structure

            ),



        "structure":

            structure,



        "liquidity":

            pipeline_result.get(

                "liquidity"

            ),



        "order_blocks":

            pipeline_result.get(

                "order_blocks"

            ),



        "fair_value_gaps":

            pipeline_result.get(

                "fair_value_gaps"

            ),



        "trade_setup":

            signal,



        "ai_reasoning":

            signal.get(

                "reasoning",

                []

            )

            if isinstance(signal, dict)

            else [],



        "warnings":

            signal.get(

                "warnings",

                []

            )

            if isinstance(signal, dict)

            else [],


    }



# ==========================================================
# SIMPLE SUMMARY
# ==========================================================

def summary(
    pipeline_result,
):
    """
    Compact terminal output.
    """

    report = analyze_market(

        pipeline_result

    )


    return {


        "bias":

            report["market_bias"],



        "signal":

            report["trade_setup"].get(

                "signal",

                "WAIT"

            ),



        "confidence":

            report["trade_setup"].get(

                "confidence",

                "Low"

            ),



        "grade":

            report["trade_setup"].get(

                "grade",

                "D"

            ),



    }



# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "analyze_market",

    "summary",

]