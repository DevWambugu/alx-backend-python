#!/usr/bin/env python3
'''This function  takes a string k
and an int OR float v as arguments
and returns a tuple'''
from typing import Union
from typing import Tuple


def to_kv(k: str, v: Union[float, str]) -> Tuple[int, float]:
    '''Return a tuple
    The first element of the tuple
    is the string k. The second element
    is the square of the int/float v
    and should be annotated as a float'''
    v: float = v
    square: float = v * v
    return (k, square)
