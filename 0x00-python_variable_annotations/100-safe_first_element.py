#!/usr/bin/env python3
"""
A module that highlights duck-typing
"""
from typing import Any, Iterable, Optional, Sequence


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Takes in a lst Sequence and returns an optional or any type
    """
    if lst:
        return lst[0]
    else:
        return None
