#!/usr/bin/env python3

from functools import reduce, partial, lru_cache, singledispatch
from collections.abc import Callable
import operator
import typing


def spell_reducer(spells: list[int], operation: str) -> int:
    def more(a: int, b: int) -> int:
        return a if operator.gt(a, b) else b

    def less(a: int, b: int) -> int:
        return a if operator.lt(a, b) else b
    operations = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": more,
        "min": less
    }
    if not spells:
        return 0
    res = 0
    if operation in operations:
        res = reduce(operations[operation], spells)
    else:
        raise ValueError("Unknown spell type")
    return res


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fire_enchantment = partial(base_enchantment, power=50, element="fire")
    ice_enchantment = partial(base_enchantment, power=50, element="ice")
    lightning_enchantment = partial(base_enchantment,
                                    power=50, element="lightning")
    return {
        "fire_enchant": fire_enchantment,
        "ice_enchant": ice_enchantment,
        "lightning_enchant": lightning_enchantment
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[typing.Any], str]:
    @singledispatch
    def spell(arg: typing.Any) -> str:
        return "Unknown spell type"

    @spell.register(int)
    def _(arg: int) -> str:
        return f"Damage spell: {arg} damage"

    @spell.register(str)
    def _(arg: str) -> str:
        return f"Enchantment: {arg}"

    @spell.register(list)
    def _(arg: list) -> str:
        return f"Multi-cast: {len(arg)} spells"
    return spell


if __name__ == "__main__":
    print("Testing spell reducer...")
    arr = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(arr, 'add')}")
    print(f"Product: {spell_reducer(arr, 'multiply')}")
    print(f"Max: {spell_reducer(arr, 'max')}")
    print("Testing memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print("Testing spell dispatcher...")
    spell = spell_dispatcher()
    print(spell(42))
    print(spell("fireball"))
    print(spell([1, 2, 3]))
    print(spell(3.14))
