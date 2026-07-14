"""
=========================================================
KAI Smart Money AI

Fair Value Gap Engine

validator.py

Institutional FVG Validation

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations


from .models import FairValueGap


from .constants import (

    MIN_GAP_PERCENT,

    MIN_DISPLACEMENT_SCORE,

)



# ==========================================================
# GAP SIZE VALIDATION
# ==========================================================

def validate_gap_size(
    fvg: FairValueGap,
) -> bool:
    """
    Ensure FVG is large enough.
    """

    return (

        fvg.size_percent

        >=

        MIN_GAP_PERCENT

    )



# ==========================================================
# DISPLACEMENT VALIDATION
# ==========================================================

def validate_displacement(
    fvg: FairValueGap,
    displacement=None,
) -> bool:
    """
    Confirm institutional displacement.
    """

    if displacement is None:

        return True


    fvg.displacement_score = (
        displacement.score
    )


    return (

        displacement.score

        >=

        MIN_DISPLACEMENT_SCORE

    )



# ==========================================================
# STRUCTURE VALIDATION
# ==========================================================

def validate_structure(
    fvg: FairValueGap,
    market_structure=None,
) -> bool:
    """
    Validate market structure context.
    """

    if market_structure is None:

        return True


    events = market_structure.get(
        "events",
        []
    )


    for event in events:

        if event.get("event") in (

            "BOS",

            "CHoCH",

        ):

            fvg.structure_confirmed = True

            return True


    return False



# ==========================================================
# VOLUME VALIDATION
# ==========================================================

def validate_volume(
    fvg: FairValueGap,
    volume_ratio: float = 1.0,
) -> bool:
    """
    Confirm volume participation.
    """

    if volume_ratio >= 1.0:

        fvg.volume_confirmed = True

        return True


    return False



# ==========================================================
# FRESHNESS
# ==========================================================

def validate_freshness(
    fvg: FairValueGap,
) -> bool:
    """
    Fresh unused FVG.
    """

    return not fvg.filled



# ==========================================================
# MASTER VALIDATOR
# ==========================================================

def validate_fvg(
    fvg: FairValueGap,
    displacement=None,
    market_structure=None,
    volume_ratio=1.0,
) -> bool:
    """
    Complete FVG validation.
    """

    checks = [

        validate_gap_size(
            fvg
        ),

        validate_displacement(
            fvg,
            displacement
        ),

        validate_structure(
            fvg,
            market_structure
        ),

        validate_volume(
            fvg,
            volume_ratio
        ),

        validate_freshness(
            fvg
        ),

    ]


    fvg.reasons = []


    if not checks[0]:

        fvg.reasons.append(
            "Gap too small"
        )


    if not checks[1]:

        fvg.reasons.append(
            "Weak displacement"
        )


    if not checks[2]:

        fvg.reasons.append(
            "No structure confirmation"
        )


    if not checks[3]:

        fvg.reasons.append(
            "Weak volume"
        )


    if not checks[4]:

        fvg.reasons.append(
            "Already filled"
        )


    return all(checks)



# ==========================================================
# VALIDATE MANY
# ==========================================================

def validate_fvgs(
    fvgs,
    displacement_map=None,
    market_structure=None,
):
    """
    Validate multiple FVGs.
    """

    valid = []


    for fvg in fvgs:

        displacement = None


        if displacement_map:

            displacement = displacement_map.get(
                fvg.created_index
            )


        if validate_fvg(

            fvg,

            displacement,

            market_structure,

        ):

            valid.append(
                fvg
            )


    return valid



# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "validate_gap_size",

    "validate_displacement",

    "validate_structure",

    "validate_volume",

    "validate_freshness",

    "validate_fvg",

    "validate_fvgs",

]