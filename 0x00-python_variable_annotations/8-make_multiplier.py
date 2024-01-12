#!/usr/bin/env python3
'''This function takes a float multiplier
as argument and returns a function that
multiplies a float by multiplier'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''returns a float multiplier function as an argument'''
    def float_multiplier_function(x: float) -> float:
        '''returns the multiplier'''
        return x * multiplier
    return float_multiplier_function
