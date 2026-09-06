# FuncMage - Master the Ancient Arts of Functional Programming

## Overview

Welcome to FuncMage Chronicles! Set in the cyberpunk year of 2142, FuncMage explores fundamental and advanced functional programming paradigms in Python 3.10+. This subject covers anonymous functions (`lambda`), higher-order functions operating on callable entities, lexical scoping and persistent closures, specialized functional artifacts from `functools` and `operator`, and custom decorators along with static methods.

---

## Technical Requirements & Guidelines

* Language: Python 3.10+
* Code Style: Strict adherence to flake8 linter standards.
* Type Hinting: Mandatory across all function signatures and return types (mypy compliant). Use `collections.abc.Callable` for callable type hints.
* Constraints:
* External libraries are strictly forbidden (no `pip install`).
* File I/O operations and complex non-functional algorithms are forbidden.
* Built-in functions `eval()` and `exec()` are strictly forbidden.
* Global variables are forbidden; embrace functional purity and closures.
* Exception handling must protect data streams from corruption and prevent unhandled crashes.
* Package directories (`ex0/`, `ex1/`, `ex2/`, `ex3/`, `ex4/`) must contain their respective implementation files.



---

## Helper Tool

> A helper tool `data_generator.py` is included to generate realistic test data (mages, artifacts, and spells) for all exercises during development and peer review:

```bash
python3 data_generator.py

```

---

## Exercises Summary

| Part | Concept | Key Modules & Files | Description |
| --- | --- | --- | --- |
| Exercise 0: Lambda Sanctum | Anonymous Functions & Iterators | ex0/lambda_spells.py | Implements data sorting, filtering, transformation, and statistics using pure `lambda` expressions without the `def` keyword. |
| Exercise 1: Higher Realm | Higher-Order Functions & Callable Composition | ex1/higher_magic.py | Builds higher-order function wrappers to combine, amplify, conditionally execute, and sequence callable spell functions. |
| Exercise 2: Memory Depths | Lexical Scoping & Persistent Closures | ex2/scope_mysteries.py | Leverages lexical scoping and `nonlocal` state to construct counters, accumulators, dynamic factories, and private memory vaults. |
| Exercise 3: Ancient Library | Standard Library Functools & Operator | ex3/functools_artifacts.py | Utilizes `functools.reduce`, `partial`, `lru_cache`, and `singledispatch` alongside the `operator` module to process data streams. |
| Exercise 4: Master’s Tower | Advanced Decorators & Class Methods | ex4/decorator_mastery.py | Constructs execution timers, parameter validators, retry decorators (`@wraps`), and integrates `@staticmethod` within class structures. |

---

## Exercise Details

### Exercise 0: Lambda Sanctum

* Concepts: Anonymous Functions, Iterators (`map`, `filter`, `sorted`, `min`, `max`, `sum`, `round`, `len`).
* Key Mechanics:
* `artifact_sorter(artifacts: list[dict]) -> list[dict]`: Sorts artifact dictionaries by `'power'` level in descending order using `sorted()` and a lambda.
* `power_filter(mages: list[dict], min_power: int) -> list[dict]`: Filters mages with power >= `min_power` using `filter()` and a lambda.
* `spell_transformer(spells: list[str]) -> list[str]`: Encloses spell strings with `"* "` prefix and `" *"` suffix using `map()` and a lambda.
* `mage_stats(mages: list[dict]) -> dict`: Calculates max power, min power, and rounded average power using lambdas with `max()`, `min()`, and `sum()`.
* Execution & Exposure: Implemented in `ex0/lambda_spells.py`.



### Exercise 1: Higher Realm

* Concepts: First-Class Functions, Higher-Order Functions, Function Composition, `Callable`.
* Key Mechanics:
* Spell Contract: All core spell functions follow `def spell(target: str, power: int) -> str`.
* `spell_combiner(spell1: Callable, spell2: Callable) -> Callable`: Returns a callable executing both spells with identical arguments, returning a tuple of results.
* `power_amplifier(base_spell: Callable, multiplier: int) -> Callable`: Returns a new spell wrapper multiplying the `power` parameter prior to execution.
* `conditional_caster(condition: Callable, spell: Callable) -> Callable`: Executes the underlying spell only if the condition returns `True`; otherwise returns `"Spell fizzled"`.
* `spell_sequence(spells: list[Callable]) -> Callable`: Returns a function executing a list of spells in sequence, collecting their results into a list.
* Execution & Exposure: Implemented in `ex1/higher_magic.py`.



### Exercise 2: Memory Depths

* Concepts: Lexical Scoping, Closures, State Encapsulation (`nonlocal`).
* Key Mechanics:
* `mage_counter() -> Callable`: Returns an independent counting closure incrementing and returning its invocation count starting from 1.
* `spell_accumulator(initial_power: int) -> Callable`: Maintains internal power accumulation starting from `initial_power`, updating its state on each call.
* `enchantment_factory(enchantment_type: str) -> Callable`: Produces dynamic functions generating string descriptions formatted as `"enchantment_type item_name"`.
* `memory_vault() -> dict[str, Callable]`: Returns a dictionary containing `'store'` and `'recall'` functions operating over a private closed dictionary.
* Execution & Exposure: Implemented in `ex2/scope_mysteries.py`.



### Exercise 3: Ancient Library

* Concepts: Functional Reduction, Partial Application, Caching (`lru_cache`), Single Dispatch Polymorphism.
* Key Mechanics:
* `spell_reducer(spells: list[int], operation: str) -> int`: Aggregates integer lists via `functools.reduce` using `operator` functions (`add`, `mul`, etc.). Handles empty lists (returns 0) and unknown operations.
* `partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]`: Uses `functools.partial` to generate 3 specialized versions pre-filling `power=50` and target elements.
* `memoized_fibonacci(n: int) -> int`: Computes the n-th Fibonacci number using `@functools.lru_cache` for memoized optimization.
* `spell_dispatcher() -> Callable[[Any], str]`: Constructs a `@functools.singledispatch` function providing distinct spell responses for `int`, `str`, and `list` types.
* Execution & Exposure: Implemented in `ex3/functools_artifacts.py`.



### Exercise 4: Master’s Tower

* Concepts: Decorator Pattern, Parameterized Decorators, Metadata Preservation (`@functools.wraps`), Static Methods (`@staticmethod`).
* Key Mechanics:
* `spell_timer(func: Callable) -> Callable`: Execution time decorator printing start/completion metrics (rounded to 3 decimal places) while preserving metadata.
* `power_validator(min_power: int) -> Callable`: Parameterized decorator factory verifying input `power` >= `min_power` before execution; returns `"Insufficient power for this spell"` if invalid.
* `retry_spell(max_attempts: int) -> Callable`: Catches exceptions during execution, retrying up to `max_attempts` before returning `"Spell casting failed after max_attempts attempts"`.
* `MageGuild`: Class implementing `@staticmethod validate_mage_name(name: str) -> bool` and instance method `cast_spell(self, spell_name: str, power: int) -> str` decorated with `@power_validator(min_power=10)`.
* Execution & Exposure: Implemented in `ex4/decorator_mastery.py`.



---

## Testing & Quality Assurance

Verify strict compliance with formatting standards (`flake8`) and static typing (`mypy`) across all exercise modules:

```bash
# Check formatting standards across all directories
flake8 ex0/ ex1/ ex2/ ex3/ ex4/

# Check static typing compliance across functional packages
mypy ex0/ ex1/ ex2/ ex3/ ex4/

```
