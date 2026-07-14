"""
=========================================================
KAI Smart Money AI

Logger

Shared logging utility.

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations

import logging
import time


class EngineLogger:

    def __init__(
        self,
        name: str,
        level=logging.INFO,
    ):

        self.logger = logging.getLogger(name)

        self.logger.setLevel(level)

        if not self.logger.handlers:

            handler = logging.StreamHandler()

            formatter = logging.Formatter(

                "[%(asctime)s] "
                "[%(levelname)s] "
                "%(name)s : %(message)s",

                "%H:%M:%S",

            )

            handler.setFormatter(formatter)

            self.logger.addHandler(handler)

        self.start_time = None

    # ------------------------------------------------------

    def start(self):

        self.start_time = time.perf_counter()

        self.logger.info("Engine started.")

    # ------------------------------------------------------

    def finish(self):

        if self.start_time is None:

            self.logger.info("Engine finished.")

            return

        elapsed = time.perf_counter() - self.start_time

        self.logger.info(
            f"Engine finished ({elapsed:.4f} sec)"
        )

    # ------------------------------------------------------

    def info(
        self,
        message: str,
    ):
        self.logger.info(message)

    # ------------------------------------------------------

    def warning(
        self,
        message: str,
    ):
        self.logger.warning(message)

    # ------------------------------------------------------

    def error(
        self,
        message: str,
    ):
        self.logger.error(message)

    # ------------------------------------------------------

    def debug(
        self,
        message: str,
    ):
        self.logger.debug(message)