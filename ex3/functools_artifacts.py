#!/usr/bin/env python3

from functools import reduce
from collections.abc import Callable
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    operations = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": lambda a, b: max(a, b),
        "min": lambda a, b: min(a, b)
    }
    if not spells:
        return 0
    res = 0
    if operation in operations:
        res = reduce(operations[operation], spells)
    else:
        raise ValueError("Unknown spell type")
    return res
