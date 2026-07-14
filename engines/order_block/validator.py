"""
=========================================================
KAI Smart Money AI

Institutional Order Block Engine

validator.py

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations

from .models import OrderBlockCandidate


# ==========================================================
# BOS
# ==========================================================

def validate_structure_break(
    candidate: OrderBlockCandidate,
) -> bool:
    """
    BOS confirmation.
    """

    displacement = candidate.displacement

    if displacement is None:
        return False

    return displacement.bos_confirmed


# ==========================================================
# CHOCH
# ==========================================================

def validate_choch(
    candidate: OrderBlockCandidate,
) -> bool:
    """
    CHoCH confirmation.
    """

    displacement = candidate.displacement

    if displacement is None:
        return False

    return displacement.choch_confirmed


# ==========================================================
# LIQUIDITY
# ==========================================================

def validate_liquidity_context(
    candidate: OrderBlockCandidate,
) -> bool:
    """
    Liquidity sweep confirmation.
    """

    displacement = candidate.displacement

    if displacement is None:
        return False

    return displacement.liquidity_confirmed


# ==========================================================
# FAIR VALUE GAP
# ==========================================================

def validate_fvg(
    candidate: OrderBlockCandidate,
) -> bool:
    """
    FVG confirmation.
    """

    displacement = candidate.displacement

    if displacement is None:
        return False

    return displacement.fvg_confirmed


# ==========================================================
# DISPLACEMENT
# ==========================================================

def validate_displacement_strength(
    candidate: OrderBlockCandidate,
    minimum_score: float = 65.0,
) -> bool:
    """
    Strong institutional displacement.
    """

    displacement = candidate.displacement

    if displacement is None:
        return False

    return displacement.score >= minimum_score


# ==========================================================
# FRESH ORDER BLOCK
# ==========================================================

def validate_freshness(
    candidate: OrderBlockCandidate,
) -> bool:
    """
    Order Block must be fresh.
    """

    return not getattr(
        candidate,
        "mitigated",
        False,
    )


# ==========================================================
# MITIGATION
# ==========================================================

def validate_mitigation(
    candidate: OrderBlockCandidate,
) -> bool:
    """
    Reject mitigated Order Blocks.
    """

    return not getattr(
        candidate,
        "mitigated",
        False,
    )


# ==========================================================
# BODY QUALITY
# ==========================================================

def validate_body_quality(
    candidate: OrderBlockCandidate,
    minimum_ratio: float = 0.50,
) -> bool:
    """
    Reject weak-bodied candles.
    """

    if candidate.range <= 0:
        return False

    ratio = candidate.body / candidate.range

    return ratio >= minimum_ratio


# ==========================================================
# RANGE QUALITY
# ==========================================================

def validate_range(
    candidate: OrderBlockCandidate,
) -> bool:
    """
    Reject zero-range candles.
    """

    return candidate.range > 0


# ==========================================================
# MASTER VALIDATOR
# ==========================================================

def validate_order_block(
    candidate: OrderBlockCandidate,
) -> bool:
    """
    Institutional Order Block validation.
    """

    checks = [

        validate_range(candidate),

        validate_body_quality(candidate),

        validate_displacement_strength(candidate),

        validate_structure_break(candidate),

        validate_liquidity_context(candidate),

        validate_fvg(candidate),

        validate_mitigation(candidate),

        validate_freshness(candidate),

    ]

    candidate.valid = all(checks)

    candidate.reason = []

    if not validate_range(candidate):
        candidate.reason.append(
            "Invalid Range"
        )

    if not validate_body_quality(candidate):
        candidate.reason.append(
            "Weak Candle Body"
        )

    if not validate_displacement_strength(candidate):
        candidate.reason.append(
            "Weak Displacement"
        )

    if not validate_structure_break(candidate):
        candidate.reason.append(
            "Missing BOS"
        )

    if not validate_liquidity_context(candidate):
        candidate.reason.append(
            "No Liquidity Sweep"
        )

    if not validate_fvg(candidate):
        candidate.reason.append(
            "No Fair Value Gap"
        )

    if not validate_freshness(candidate):
        candidate.reason.append(
            "Order Block Not Fresh"
        )

    if not validate_mitigation(candidate):
        candidate.reason.append(
            "Already Mitigated"
        )

    return candidate.valid


# ==========================================================
# VALIDATE MANY
# ==========================================================

def validate_candidates(
    candidates,
):
    """
    Validate all candidates.
    """

    valid = []

    for candidate in candidates:

        if validate_order_block(
            candidate,
        ):
            valid.append(
                candidate
            )

    return valid


# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "validate_structure_break",

    "validate_choch",

    "validate_liquidity_context",

    "validate_fvg",

    "validate_displacement_strength",

    "validate_body_quality",

    "validate_range",

    "validate_freshness",

    "validate_mitigation",

    "validate_order_block",

    "validate_candidates",

]