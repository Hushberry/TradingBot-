"""
=========================================================
KAI Smart Money AI

Institutional Order Block Engine

scorer.py

Institutional Order Block Scoring

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations

from .models import OrderBlockCandidate


# ==========================================================
# DISPLACEMENT
# ==========================================================

def score_displacement(
    candidate: OrderBlockCandidate,
) -> float:
    """
    Maximum: 30
    """

    displacement = candidate.displacement

    if displacement is None:
        return 0.0

    return min(
        displacement.score * 0.30,
        30.0,
    )


# ==========================================================
# BOS
# ==========================================================

def score_structure(
    candidate: OrderBlockCandidate,
) -> float:
    """
    Maximum: 20
    """

    displacement = candidate.displacement

    if displacement is None:
        return 0.0

    return (
        20.0
        if displacement.bos_confirmed
        else 0.0
    )


# ==========================================================
# LIQUIDITY
# ==========================================================

def score_liquidity(
    candidate: OrderBlockCandidate,
) -> float:
    """
    Maximum: 15
    """

    displacement = candidate.displacement

    if displacement is None:
        return 0.0

    return (
        15.0
        if displacement.liquidity_confirmed
        else 0.0
    )


# ==========================================================
# FAIR VALUE GAP
# ==========================================================

def score_fvg(
    candidate: OrderBlockCandidate,
) -> float:
    """
    Maximum: 10
    """

    displacement = candidate.displacement

    if displacement is None:
        return 0.0

    return (
        10.0
        if displacement.fvg_confirmed
        else 0.0
    )


# ==========================================================
# BODY QUALITY
# ==========================================================

def score_body(
    candidate: OrderBlockCandidate,
) -> float:
    """
    Maximum: 10
    """

    if candidate.range <= 0:
        return 0.0

    ratio = candidate.body / candidate.range

    return min(
        ratio * 10.0,
        10.0,
    )


# ==========================================================
# FRESHNESS
# ==========================================================

def score_freshness(
    candidate: OrderBlockCandidate,
) -> float:
    """
    Maximum: 5
    """

    return 0.0 if getattr(candidate, "mitigated", False) else 5.0


# ==========================================================
# ATR
# ==========================================================

def score_atr(
    candidate: OrderBlockCandidate,
) -> float:
    """
    Maximum: 5
    """

    displacement = candidate.displacement

    if displacement is None:
        return 0.0

    ratio = min(
        displacement.atr_ratio,
        2.0,
    )

    return (ratio / 2.0) * 5.0


# ==========================================================
# VOLUME
# ==========================================================

def score_volume(
    candidate: OrderBlockCandidate,
) -> float:
    """
    Maximum: 5
    """

    displacement = candidate.displacement

    if displacement is None:
        return 0.0

    ratio = min(
        displacement.volume_ratio,
        2.0,
    )

    return (ratio / 2.0) * 5.0


# ==========================================================
# TOTAL SCORE
# ==========================================================

def calculate_order_block_score(
    candidate: OrderBlockCandidate,
) -> float:
    """
    Calculate institutional score (0–100).
    """

    score = (

        score_displacement(candidate)

        + score_structure(candidate)

        + score_liquidity(candidate)

        + score_fvg(candidate)

        + score_body(candidate)

        + score_freshness(candidate)

        + score_atr(candidate)

        + score_volume(candidate)

    )

    candidate.score = round(
        min(score, 100.0),
        2,
    )

    return candidate.score


# ==========================================================
# CONFIDENCE
# ==========================================================

def confidence_level(
    score: float,
) -> str:

    if score >= 90:
        return "Very High"

    if score >= 80:
        return "High"

    if score >= 65:
        return "Medium"

    if score >= 50:
        return "Low"

    return "Very Low"


# ==========================================================
# GRADE
# ==========================================================

def score_grade(
    score: float,
) -> str:

    if score >= 95:
        return "A+"

    if score >= 90:
        return "A"

    if score >= 85:
        return "B+"

    if score >= 75:
        return "B"

    if score >= 65:
        return "C"

    if score >= 50:
        return "D"

    return "F"


# ==========================================================
# EXPLANATION
# ==========================================================

def explain_score(
    candidate: OrderBlockCandidate,
) -> dict:
    """
    Explain score breakdown.
    """

    return {

        "displacement": score_displacement(candidate),

        "structure": score_structure(candidate),

        "liquidity": score_liquidity(candidate),

        "fair_value_gap": score_fvg(candidate),

        "body": score_body(candidate),

        "freshness": score_freshness(candidate),

        "atr": score_atr(candidate),

        "volume": score_volume(candidate),

        "total": candidate.score,

        "grade": score_grade(candidate.score),

        "confidence": confidence_level(candidate.score),

    }


# ==========================================================
# SCORE MANY
# ==========================================================

def score_candidates(
    candidates,
):
    """
    Score all validated candidates.
    """

    for candidate in candidates:

        calculate_order_block_score(
            candidate,
        )

    return sorted(

        candidates,

        key=lambda c: c.score,

        reverse=True,

    )


# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "calculate_order_block_score",

    "score_candidates",

    "confidence_level",

    "score_grade",

    "explain_score",

]