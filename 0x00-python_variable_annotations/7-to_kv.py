#!/usr/bin/env python3
"""
Module that contains a type-annotated function taking in a string
and an int and returning a tuple
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes in k: a string, v: an int then constructs a
    tuple with first element being k and seconf being square
    of v
    """
    ans = [k, v**2]
    return tuple(ans)
