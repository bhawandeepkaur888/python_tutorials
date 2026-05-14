# advanced python topics
# covers context managers, dataclasses, type hints, abstract classes, slots, and more

# ---- CONTEXT MANAGERS ----
print("context managers :")

# with statement ensures cleanup code always runs
# file handling is the classic example
import tempfile, os

# manual context manager via class with __enter__ / __exit__
class ManagedResource:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f"  entering context: {self.name}")
        return self                 # value bound to 'as' variable

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"  exiting context: {self.name}")
        if exc_type:
            print(f"  exception caught: {exc_val}")
            return True             # suppress exception
        return False

with ManagedResource("database connection") as res:
    print(f"  using resource: {res.name}")

# context manager that suppresses exceptions
with ManagedResource("safe block") as res:
    raise ValueError("intentional error")
print("  execution continued after suppressed error")

# contextlib.contextmanager decorator - generator-based context manager
from contextlib import contextmanager

@contextmanager
def timer():
    import time
    start = time.time()
    print("  timer started")
    yield                            # code inside 'with' block runs here
    elapsed = (time.time() - start) * 1000
    print(f"  timer stopped: {elapsed:.3f} ms")

with timer():
    total = sum(range(1_000_000))
    print(f"  sum = {total}")


# ---- DATACLASSES ----
print("\ndataclasses :")
from dataclasses import dataclass, field

@dataclass
class Point:
    x: float
    y: float

    def distance_from_origin(self):
        return (self.x**2 + self.y**2) ** 0.5

p = Point(3.0, 4.0)
print("point :", p)
print("distance :", p.distance_from_origin())
print("p == Point(3,4) :", p == Point(3.0, 4.0))   # auto __eq__


@dataclass
class Student:
    name: str
    age: int
    grades: list = field(default_factory=list)      # mutable default
    school: str = "Default School"

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0.0

s = Student("Alice", 20)
s.add_grade(90)
s.add_grade(85)
s.add_grade(92)
print("student :", s)
print("average :", s.average())


@dataclass(frozen=True)     # immutable dataclass
class Color:
    r: int
    g: int
    b: int

    def to_hex(self):
        return f"#{self.r:02X}{self.g:02X}{self.b:02X}"

red = Color(255, 0, 0)
print("red :", red)
print("hex :", red.to_hex())


# ---- TYPE HINTS ----
print("\ntype hints :")
from typing import List, Dict, Optional, Union, Tuple, Callable, TypeVar

T = TypeVar("T")

def first_element(items: List[T]) -> Optional[T]:
    return items[0] if items else None

def format_record(name: str, age: int, score: float) -> Dict[str, Union[str, int, float]]:
    return {"name": name, "age": age, "score": score}

def apply(func: Callable[[int], int], value: int) -> int:
    return func(value)

def min_max(nums: List[int]) -> Tuple[int, int]:
    return min(nums), max(nums)

print("first_element([1,2,3]) :", first_element([1, 2, 3]))
print("first_element([]) :", first_element([]))
print("format_record :", format_record("Bob", 25, 9.5))
print("apply(lambda x:x**2, 5) :", apply(lambda x: x**2, 5))
print("min_max([3,1,4,1,5,9]) :", min_max([3, 1, 4, 1, 5, 9]))


# ---- ABSTRACT BASE CLASSES ----
print("\nabstract base classes (ABC) :")
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass

    def describe(self):
        return f"{self.__class__.__name__}: area={self.area():.2f}, perimeter={self.perimeter():.2f}"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2

    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

shapes = [Rectangle(4, 6), Circle(5)]
for shape in shapes:
    print(" ", shape.describe())

# cannot instantiate abstract class
try:
    s = Shape()
except TypeError as e:
    print(f"  cannot instantiate: {e}")


# ---- __slots__ ----
print("\n__slots__ for memory optimization :")

class WithoutSlots:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class WithSlots:
    __slots__ = ("x", "y")   # restricts attributes; saves memory per instance
    def __init__(self, x, y):
        self.x = x
        self.y = y

a = WithSlots(1, 2)
print("slots a.x :", a.x)

try:
    a.z = 3                  # cannot add new attributes with __slots__
except AttributeError as e:
    print(f"  cannot add attribute: {e}")


# ---- COLLECTIONS MODULE ----
print("\ncollections module :")
from collections import defaultdict, Counter, deque, OrderedDict

# defaultdict - provides default value for missing keys
word_groups = defaultdict(list)
for word in ["apple", "ant", "banana", "blueberry", "cherry"]:
    word_groups[word[0]].append(word)
print("defaultdict :", dict(word_groups))

# Counter - counts elements
text = "abracadabra"
freq = Counter(text)
print("Counter :", freq)
print("most common 3 :", freq.most_common(3))

votes = Counter(["alice", "bob", "alice", "charlie", "alice", "bob"])
print("vote counts :", votes)

# deque - double-ended queue (O(1) appends/pops from both ends)
d = deque([1, 2, 3, 4, 5])
d.appendleft(0)
d.append(6)
d.popleft()
d.pop()
print("deque :", d)

d.rotate(2)    # rotate right by 2
print("rotated :", d)


# ---- WALRUS OPERATOR IN CONTEXT ----
print("\nwalrus operator (:=) in advanced use :")

data = [1, 4, 9, 16, 25, 36, 49]
# filter and compute simultaneously
big_roots = [root for x in data if (root := x**0.5) > 4]
print("roots > 4 :", big_roots)

print("\nall advanced topics demonstrated successfully")
