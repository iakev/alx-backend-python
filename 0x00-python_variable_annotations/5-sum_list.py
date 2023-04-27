#!/usr/bin/env python3
"""
Module that contains a type-annotated function that takes in a
list of floats and returns their sum as a float
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Takes in a list of floats and returns a float sum
    of the list entries
    """
    return sum(input_list)
