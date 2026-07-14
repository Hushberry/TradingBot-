"""
=========================================================
KAI Smart Money AI

Common Exceptions

Shared exceptions used across all engines.

Author: Vincent Chimezirim
=========================================================
"""


class KAIError(Exception):
    """
    Base exception for all KAI engine errors.
    """
    pass


# ==========================================================
# DATA ERRORS
# ==========================================================

class DataError(KAIError):
    """Base data exception."""
    pass


class EmptyDataError(DataError):
    """Raised when no candle data is available."""
    pass


class InvalidDataFrameError(DataError):
    """Raised when input is not a pandas DataFrame."""
    pass


class MissingColumnsError(DataError):
    """Raised when required columns are missing."""

    def __init__(self, missing_columns):
        self.missing_columns = list(missing_columns)

        message = (
            "Missing required columns: "
            + ", ".join(self.missing_columns)
        )

        super().__init__(message)


class InvalidPriceError(DataError):
    """Raised when invalid price values are found."""
    pass


class InvalidIndexError(DataError):
    """Raised when candle index is invalid."""
    pass


# ==========================================================
# VALIDATION
# ==========================================================

class ValidationError(KAIError):
    """Base validation exception."""
    pass


class InvalidDirectionError(ValidationError):
    """Raised when direction is invalid."""
    pass


class InvalidTrendError(ValidationError):
    """Raised when trend is invalid."""
    pass


class InvalidScoreError(ValidationError):
    """Raised when score is outside expected range."""
    pass


# ==========================================================
# ENGINE
# ==========================================================

class EngineError(KAIError):
    """Base engine exception."""
    pass


class ConfigurationError(EngineError):
    """Raised for invalid engine configuration."""
    pass


class ProcessingError(EngineError):
    """Raised during processing failures."""
    pass


class CalculationError(EngineError):
    """Raised when a calculation fails."""
    pass