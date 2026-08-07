#!/usr/bin/env python3

from collections.abc import Callable


def mage_counter() -> Callable:
    count = 0

    def inner() -> int:
        nonlocal count
        count += 1
        return count
    return inner


def spell_accumulator(initial_power: int) -> Callable:
    total_power = initial_power

    def inner(add: int) -> int:
        nonlocal total_power
        total_power += add
        return total_power
    return inner


def enchantment_factory(enchantment_type: str) -> Callable:
    def inner(item_name: str) -> str:
        return enchantment_type + ' ' + item_name
    return inner


def memory_vault() -> dict[str, Callable]:
    memory = {}

    def store(key: str, value: int | str) -> None:
        memory[key] = value

    def recall(key: str) -> int | str:
        if key in memory.keys():
            return memory[key]
        else:
            return "Memory not found"
    return {
        "store": store,
        "recall": recall
    }


if __name__ == "__main__":
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()

    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("Testing spell accumulator...")
    accumulator = spell_accumulator(100)
    print(f"Base 100, add 20: {accumulator(20)}")
    print(f"Base 100, add 30: {accumulator(30)}")

    print("Testing enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")

    print(flaming("Sword"))
    print(frozen("Shield"))

    print("Testing memory vault...")
    vault = memory_vault()

    store = vault["store"]
    recall = vault["recall"]

    store("secret", 42)
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {recall('secret')}")
    print(f"Recall 'unknown': {recall('unknown')}")
