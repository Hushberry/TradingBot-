"""
=========================================================
KAI Smart Money AI

Swing Engine

validator.py

Swing Validation Layer

Author: Vincent Chimezirim
=========================================================
"""

from __future__ import annotations



from .models import (

    SwingPoint,

)



from .constants import (

    MIN_SWING_SCORE,

)



from .utils import (

    valid_distance,

)



# ==========================================================
# PRICE VALIDATION
# ==========================================================

def validate_price(
    swing: SwingPoint,
):
    """
    Ensure swing has valid price.
    """

    return (

        swing.price > 0

    )



# ==========================================================
# TYPE VALIDATION
# ==========================================================

def validate_type(
    swing: SwingPoint,
):
    """
    Ensure swing type exists.
    """

    return swing.swing_type in (

        "swing_high",

        "swing_low",

    )



# ==========================================================
# SCORE VALIDATION
# ==========================================================

def validate_strength(
    swing: SwingPoint,
):
    """
    Check swing quality.
    """

    return (

        swing.score >= MIN_SWING_SCORE

        or

        swing.confirmed

    )



# ==========================================================
# DUPLICATE FILTER
# ==========================================================

def remove_duplicate_swings(
    swings,
):
    """
    Remove swings too close together.
    """

    clean = []


    for swing in swings:


        duplicate = False


        for existing in clean:


            if (

                swing.swing_type

                ==

                existing.swing_type

                and

                not valid_distance(

                    swing.price,

                    existing.price,

                )

            ):

                duplicate = True

                break



        if not duplicate:

            clean.append(

                swing

            )



    return clean



# ==========================================================
# SINGLE VALIDATION
# ==========================================================

def validate_swing(
    swing: SwingPoint,
):
    """
    Validate one swing.
    """

    checks = [

        validate_price(
            swing
        ),

        validate_type(
            swing
        ),

        validate_strength(
            swing
        ),

    ]


    if all(checks):

        swing.confirmed = True


        swing.add_reason(

            "Swing validation passed"

        )


        return True



    swing.add_reason(

        "Swing validation failed"

    )


    return False



# ==========================================================
# COLLECTION VALIDATION
# ==========================================================

def validate_swings(
    swings,
):
    """
    Validate swing collection.
    """

    valid = []


    cleaned = remove_duplicate_swings(

        swings

    )



    for swing in cleaned:


        if validate_swing(

            swing

        ):

            valid.append(

                swing

            )



    return valid



# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "validate_price",

    "validate_type",

    "validate_strength",

    "remove_duplicate_swings",

    "validate_swing",

    "validate_swings",

]