#!/usr/bin/env python3

from collections.abc import Callable


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def enough_power(target: str, power: int) -> bool:
    return power >= 10


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def result(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return result


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def result(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return result


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def result(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return result


def spell_sequence(spells: list[Callable]) -> Callable:
    def result(target: str, power: int) -> list[str]:
        res: list[str] = []
        for s in spells:
            res.append(s(target, power))
        return res
    return result


if __name__ == "__main__":
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    print("Combined spell result: Fireball hits Dragon, Heals Dragon")

    print("Testing power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print("Original: 10, Amplified: 30")
