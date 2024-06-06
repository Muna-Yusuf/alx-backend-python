#!/usr/bin/env python3
""" DOC """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    ''' Outputs function that multiplies float by `multiplier`. '''
    return lambda x: x * multiplier
