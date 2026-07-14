"""
======================================================
KAI Smart Money AI
Analysis Context

Central data store shared by every engine.

Author: Vincent Chimezirim
======================================================
"""

from copy import deepcopy


class AnalysisContext:

    def __init__(self, candles):
        self.data = {
            "candles": candles,

            "swings": None,

            "market_structure": None,

            "liquidity": None,

           "order_blocks": None,

           "fair_value_gaps": None,

           "premium_discount": None,

           "sessions": None,

           "volume": None,

           "sentiment": None,

           "economic_events": None,

           "ai_reasoning": None,

           "trade_setup": None,

           "execution": None,

           "metadata": {}
        }


    def get(self, key, default=None):
        return self.data.get(key, default)

    def set(self, key, value):
        self.data[key] = value

    def update(self, values):
        self.data.update(values)

    def exists(self, key):
        return key in self.data

    def export(self):
        return deepcopy(self.data)

    def clear(self):
        for key in self.data:
            if key != "candles":
                self.data[key] = None