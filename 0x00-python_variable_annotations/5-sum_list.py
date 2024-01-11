#!/usr/bin/env python3
'''Take in a list of floats
as an argument. Then return their sum'''
from typing import List

input_list: List[float]


def sum_list(input_list) -> float:
    '''takes in a list of floats and returns
    their sum as a float'''
    return sum(input_list)
