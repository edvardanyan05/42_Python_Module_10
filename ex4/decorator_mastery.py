#!/usr/bin/env python3

from functools import wraps
from collections.abc import Callable
from typing import Any
import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {round(end - start, 3)} seconds")
        return res
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if "power" in kwargs:
                power = kwargs["power"]
            elif args:
                power = args[-1]
            else:
                power = 0

            if power >= min_power:
                return func(*args, **kwargs)

            return "Insufficient power for this spell"

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for n in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if n != max_attempts:
                        print(f"Spell failed, retrying... "
                              f"(attempt {n}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) >= 3 and all(c.isalpha() or c == ' ' for c in name):
            return True
        return False

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.101)
        return "Fireball cast!"
    print(f"Result: {fireball()}")

    print("Testing retrying spell...")

    @retry_spell(max_attempts=3)
    def failing_spell() -> str:
        raise ValueError("Spell failed!")
    print(failing_spell())

    @retry_spell(max_attempts=3)
    def passing_spell() -> str:
        return "Waaaaaaagh spelled !"
    print(passing_spell())

    print("Testing MageGuild...")
    print(MageGuild.validate_mage_name("abc def"))
    print(MageGuild.validate_mage_name("abc def!"))
    obj = MageGuild()
    print(obj.cast_spell("Lightning", power=15))
    print(obj.cast_spell("Lightning", power=5))
