# Python Tutorial - Beginner to Advanced

A complete Python tutorial series covering all core and advanced concepts, structured as 20 chapters plus an introduction. Each file is self-contained and runnable with any Python 3.10+ interpreter.

## How to Run

```bash
python3 introduction.py
python3 chapter-one-data-types.py
# ... and so on
```

## Table of Contents

| File                                                                                         | Topic                                                                                                                           |
| -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| [introduction.py](introduction.py)                                                           | What Python is, how to run it, variables, constants, `type()`, comments, and `print()` options                                  |
| [chapter-one-data-types.py](chapter-one-data-types.py)                                       | All built-in types: int, float, complex, str, bool, None, list, tuple, range, dict, set, frozenset, bytes, bytearray            |
| [chapter-two-operators.py](chapter-two-operators.py)                                         | Arithmetic, assignment, comparison, identity, logical, bitwise, membership operators, walrus `:=`, and precedence               |
| [chapter-three-type-conversion-and-strings.py](chapter-three-type-conversion-and-strings.py) | Implicit/explicit casting, string methods, f-strings, `.format()`, and `%` formatting                                           |
| [chapter-four-conditionals.py](chapter-four-conditionals.py)                                 | if/elif/else, nested conditions, ternary expressions, `match`-`case` (Python 3.10+), truthy/falsy values                        |
| [chapter-five-loops.py](chapter-five-loops.py)                                               | for, while, break, continue, pass, for-else, while-else, nested loops, `zip()`, `enumerate()`, `reversed()`, `sorted()`         |
| [chapter-six-lists.py](chapter-six-lists.py)                                                 | List creation, indexing, slicing, mutating methods, sorting, copying, 2D lists, and unpacking                                   |
| [chapter-seven-tuples.py](chapter-seven-tuples.py)                                           | Tuple creation, packing/unpacking, `namedtuple`, immutability, swapping variables, and tuple as dict key                        |
| [chapter-eight-dictionaries.py](chapter-eight-dictionaries.py)                               | Dictionary CRUD, views, nesting, comprehensions, `setdefault()`, merge with `                                                   | `, and `Counter` |
| [chapter-nine-sets.py](chapter-nine-sets.py)                                                 | Set operations (union, intersection, difference), subset/superset checks, `frozenset`, and set comprehension                    |
| [chapter-ten-functions.py](chapter-ten-functions.py)                                         | `def`, default params, `*args`/`**kwargs`, closures, `nonlocal`, lambda, recursion, type annotations, and first-class functions |
| [chapter-eleven-modules-and-packages.py](chapter-eleven-modules-and-packages.py)             | `import` / `from...import` / `as`, and tour of math, random, os, sys, datetime, json, collections, itertools                    |
| [chapter-twelve-file-handling.py](chapter-twelve-file-handling.py)                           | Reading and writing files, append mode, `seek()`/`tell()`, `pathlib.Path`, binary files, and `shutil` cleanup                   |
| [chapter-thirteen-exception-handling.py](chapter-thirteen-exception-handling.py)             | try/except/else/finally, raising exceptions, custom exception classes, exception chaining, `suppress()`, and `assert`           |
| [chapter-fourteen-oop-classes.py](chapter-fourteen-oop-classes.py)                           | `class`, `__init__`, instance vs class variables, `@property`, `@classmethod`, `@staticmethod`, and dunder methods              |
| [chapter-fifteen-inheritance.py](chapter-fifteen-inheritance.py)                             | Single/multi-level/multiple inheritance, `super()`, method overriding, MRO, mixins, `isinstance()`, `issubclass()`              |
| [chapter-sixteen-iterators-and-generators.py](chapter-sixteen-iterators-and-generators.py)   | `__iter__`/`__next__`, custom iterators, `yield`, `yield from`, generator expressions, infinite generators, `send()`            |
| [chapter-seventeen-decorators.py](chapter-seventeen-decorators.py)                           | Function decorators, `@wraps`, chaining, decorators with arguments, class-based decorators, memoization, `lru_cache`            |
| [chapter-eighteen-comprehensions.py](chapter-eighteen-comprehensions.py)                     | List, dict, set comprehensions, nested comprehensions, conditional expressions, generator expressions, performance notes        |
| [chapter-nineteen-functional-programming.py](chapter-nineteen-functional-programming.py)     | `map()`, `filter()`, `reduce()`, lambda, `sorted()` with key, `zip()`, `enumerate()`, `any()`/`all()`, `partial()`              |
| [chapter-twenty-advanced-topics.py](chapter-twenty-advanced-topics.py)                       | Context managers, `dataclasses`, type hints (`typing`), abstract base classes (`ABC`), `__slots__`, `collections` deep dive     |

## Prerequisites

- Python 3.10 or higher (for `match`-`case` in chapter four)
- No external packages required — standard library only

## Learning Path

```
introduction → ch 1-5  (core syntax and control flow)
             → ch 6-9  (data structures)
             → ch 10-13 (functions, modules, files, errors)
             → ch 14-16 (OOP and iteration)
             → ch 17-20 (advanced patterns)
```
