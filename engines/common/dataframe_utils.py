"""
=========================================================
KAI Smart Money AI

Common DataFrame Utilities

Shared pandas DataFrame helper functions.

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations

from typing import Iterable, Optional

import pandas as pd

from .exceptions import (
    EmptyDataError,
    InvalidDataFrameError,
    MissingColumnsError,
)

# ==========================================================
# REQUIRED COLUMNS
# ==========================================================

OHLC_COLUMNS = (
    "open",
    "high",
    "low",
    "close",
)

OPTIONAL_COLUMNS = (
    "time",
    "tick_volume",
    "real_volume",
    "spread",
)


# ==========================================================
# VALIDATION
# ==========================================================

def is_dataframe(data) -> bool:
    """
    Return True if object is a pandas DataFrame.
    """
    return isinstance(data, pd.DataFrame)


def validate_dataframe(
    df: pd.DataFrame,
    required_columns: Optional[Iterable[str]] = None,
) -> None:
    """
    Validate DataFrame structure.
    """

    if not isinstance(df, pd.DataFrame):
        raise InvalidDataFrameError(
            "Expected pandas DataFrame."
        )

    if df.empty:
        raise EmptyDataError(
            "DataFrame is empty."
        )

    required = tuple(required_columns or OHLC_COLUMNS)

    missing = [
        column
        for column in required
        if column not in df.columns
    ]

    if missing:
        raise MissingColumnsError(missing)


# ==========================================================
# INFORMATION
# ==========================================================

def row_count(df: pd.DataFrame) -> int:
    return len(df)


def column_count(df: pd.DataFrame) -> int:
    return len(df.columns)


def has_column(
    df: pd.DataFrame,
    column: str,
) -> bool:
    return column in df.columns


# ==========================================================
# SORTING
# ==========================================================

def ensure_sorted(
    df: pd.DataFrame,
    column: str = "time",
) -> pd.DataFrame:
    """
    Return DataFrame sorted by column.
    """

    if column not in df.columns:
        return df.reset_index(drop=True)

    return (
        df.sort_values(column)
        .reset_index(drop=True)
    )


# ==========================================================
# TIME
# ==========================================================

def ensure_datetime(
    df: pd.DataFrame,
    column: str = "time",
) -> pd.DataFrame:
    """
    Convert time column to datetime.
    """

    if column in df.columns:
        df = df.copy()
        df[column] = pd.to_datetime(df[column])

    return df


# ==========================================================
# INDEX
# ==========================================================

def reset_dataframe(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Reset DataFrame index.
    """

    return df.reset_index(drop=True)


# ==========================================================
# ROW ACCESS
# ==========================================================

def safe_get_row(
    df: pd.DataFrame,
    index: int,
):
    """
    Safely return one row.
    """

    if index < 0:
        return None

    if index >= len(df):
        return None

    return df.iloc[index]


def first_row(df: pd.DataFrame):
    return df.iloc[0]


def last_row(df: pd.DataFrame):
    return df.iloc[-1]


# ==========================================================
# SLICING
# ==========================================================

def previous_rows(
    df: pd.DataFrame,
    index: int,
    count: int,
) -> pd.DataFrame:
    """
    Return previous rows.
    """

    start = max(0, index - count)

    return df.iloc[start:index]


def next_rows(
    df: pd.DataFrame,
    index: int,
    count: int,
) -> pd.DataFrame:
    """
    Return future rows.
    """

    end = min(len(df), index + count + 1)

    return df.iloc[index + 1:end]


# ==========================================================
# COPY
# ==========================================================

def clone_dataframe(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Deep copy DataFrame.
    """

    return df.copy(deep=True)


# ==========================================================
# CLEANING
# ==========================================================

def remove_nan(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Remove rows containing NaN.
    """

    return (
        df
        .dropna()
        .reset_index(drop=True)
    )


def normalize_columns(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Normalize column names.
    """

    df = df.copy()

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
    )

    return df


# ==========================================================
# SEARCH
# ==========================================================

def find_column(
    df: pd.DataFrame,
    column: str,
) -> bool:
    """
    Check whether column exists.
    """

    return column in df.columns


# ==========================================================
# SUMMARY
# ==========================================================

def dataframe_summary(
    df: pd.DataFrame,
) -> dict:
    """
    Return DataFrame summary.
    """

    return {
        "rows": len(df),
        "columns": list(df.columns),
        "shape": df.shape,
        "memory_bytes": int(
            df.memory_usage(deep=True).sum()
        ),
    }