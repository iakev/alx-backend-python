#!/usr/bin/env python3
"""
A module that annotated a function correctly with
an iterable
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes in an iterable and returns a tuple
    """
    return [(i, len(i)) for i in lst]
