#!/usr/bin/env python3
"""
Module that contains a type-annotated function with multiplier arguments
and returns a function that multiplies a float by a multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes in a float argument and returns a function
    that multiplies a float with a multiplier
    """
    def multiply(fl):
        return fl * multiplier
    return multiply
