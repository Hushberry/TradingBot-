"""
=========================================================
KAI Smart Money AI

Main Application

Author: Vincent Chimezirim
=========================================================
"""


import pandas as pd


from engines.integration import (

    KAIAnalysisPipeline,

    analyze_market,

    summary,

)



# ==========================================================
# LOAD DATA
# ==========================================================

def load_candles():

    """
    Load market candles.

    Replace this with:
    MT5 connector
    CSV loader
    Broker API
    """

    candles = pd.DataFrame()


    return candles



# ==========================================================
# MAIN
# ==========================================================

def main():



    candles = load_candles()



    if candles.empty:

        print(
            "No candle data available"
        )

        return



    # ----------------------------------
    # Initialize KAI
    # ----------------------------------

    kai = KAIAnalysisPipeline()



    # ----------------------------------
    # Run Analysis
    # ----------------------------------

    result = kai.run(

        candles

    )



    # ----------------------------------
    # Format Report
    # ----------------------------------

    report = analyze_market(

        result

    )



    quick = summary(

        result

    )



    # ----------------------------------
    # Output
    # ----------------------------------

    print(
        "=" * 60
    )

    print(
        "KAI SMART MONEY AI"
    )

    print(
        "=" * 60
    )


    print(
        quick
    )


    print(
        "\nAI REPORT"
    )


    print(
        report
    )



# ==========================================================
# ENTRY
# ==========================================================

if __name__ == "__main__":

    main()