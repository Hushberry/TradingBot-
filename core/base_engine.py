"""
======================================================
KAI Smart Money AI
Base Engine

Parent class for all KAI engines.

Author: Vincent Chimezirim
======================================================
"""

from abc import ABC, abstractmethod
from datetime import datetime
import logging
import time


class BaseEngine(ABC):
    """
    Base class for every KAI engine.
    """

    def __init__(self, name):

        self.name = name

        self.logger = logging.getLogger(name)

        self.execution_time = 0.0

    # =====================================================
    # VALIDATION
    # =====================================================

    def require(self, context, *keys):
        """
        Ensure required data exists in AnalysisContext.
        """

        missing = []

        for key in keys:

            value = context.get(key)

            if value is None:

                missing.append(key)

        if missing:

            raise ValueError(

                f"{self.name}: Missing context values: "
                f"{', '.join(missing)}"

            )

    # =====================================================
    # TIMER
    # =====================================================

    def start_timer(self):

        self._start = time.perf_counter()

    def stop_timer(self):

        self.execution_time = (

            time.perf_counter()

            - self._start

        )

        return self.execution_time

    # =====================================================
    # LOGGING
    # =====================================================

    def log(self, message):

        self.logger.info(

            f"[{self.name}] {message}"

        )

    def warning(self, message):

        self.logger.warning(

            f"[{self.name}] {message}"

        )

    def error(self, message):

        self.logger.error(

            f"[{self.name}] {message}"

        )

    # =====================================================
    # METADATA
    # =====================================================

    def update_metadata(self, context):

        metadata = context.get("metadata")

        if metadata is None:

            metadata = {}

        metadata[self.name] = {

            "completed": True,

            "execution_time": round(
                self.execution_time,
                6
            ),

            "timestamp": datetime.utcnow().isoformat()

        }

        context.set(

            "metadata",

            metadata

        )

    # =====================================================
    # ENGINE EXECUTION
    # =====================================================

    def execute(self, context):

        self.start_timer()

        result = self.process(context)

        self.stop_timer()

        self.update_metadata(result)

        return result

    # =====================================================
    # EVERY ENGINE MUST IMPLEMENT
    # =====================================================

    @abstractmethod
    def process(self, context):
        pass