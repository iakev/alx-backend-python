#!/usr/bin/env python3
"""
A module that has a type-annotated function
using a TypeVar
"""
from typing import Any, Mapping, Optional, TypeVar, Union
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Takes in a Mapping, TypeVar and returns a union of Any and TypeVar
    """
    if key in dct:
        return dct[key]
    else:
        return default
