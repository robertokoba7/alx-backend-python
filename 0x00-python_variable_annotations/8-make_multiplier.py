#!/usr/bin/env python3
'''
takes a float multiplier as argument and returns a fuction
'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return function that multiplies float by `multiplier`"""
    return lambda x: x * multiplier
