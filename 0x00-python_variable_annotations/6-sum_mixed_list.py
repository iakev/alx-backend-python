#!/usr/bin/env python3
"""
Module contains a type-annotated function that
takes a list of intergers and floats; returning
their sum as a float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Takes in mxd_lst (containing ints and floats mixed) and return
    the sum as a float
    """
    return sum(mxd_lst)
