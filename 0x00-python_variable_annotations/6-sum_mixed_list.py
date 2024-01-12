#!/usr/bin/env python3
'''This function sums the elements of a list
(integer and floats) and returns a float'''
from typing import List
from typing import Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''returns the sum as a flaot type'''
    return sum(mxd_lst)
