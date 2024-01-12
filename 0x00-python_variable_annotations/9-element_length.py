#!/usr/bin/env python3
'''This function returns the element length'''
from typing import List
from typing import Tuple
from typing import Sequence
from typing import Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''return element length'''
    return [(i, len(i)) for i in lst]
