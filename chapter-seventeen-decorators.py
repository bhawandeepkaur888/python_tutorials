# decorators in python
# decorators wrap a function to add functionality without modifying its code
# they use the @ syntax and are a form of higher-order functions

# ---- BASIC DECORATOR ----
print("basic decorator :")

def simple_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"  before calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"  after calling {func.__name__}")
        return result
    return wrapper

@simple_decorator
def say_hello():
    print("  Hello!")

say_hello()


# ---- DECORATOR WITH @wraps ----
# @wraps preserves the original function's metadata
print("\n@wraps preserves function metadata :")
from functools import wraps

def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"  calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"  {func.__name__} returned: {result}")
        return result
    return wrapper

@log_calls
def add(a, b):
    """Adds two numbers together."""
    return a + b

result = add(3, 5)
print("  function name preserved :", add.__name__)
print("  docstring preserved :", add.__doc__)


# ---- DECORATOR WITH ARGUMENTS ----
print("\ndecorator with arguments :")

def repeat(n):
    """Decorator factory - returns a decorator"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"  Hello, {name}!")

greet("Alice")


# ---- CHAINING DECORATORS ----
print("\nchaining multiple decorators :")

def bold(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"**{result}**"
    return wrapper

def uppercase(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@bold
@uppercase
def get_message():
    return "hello world"

# applied bottom-up: uppercase first, then bold
print("chained result :", get_message())


# ---- TIMING DECORATOR ----
print("\ntiming decorator :")
import time

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"  {func.__name__} took {(end - start) * 1000:.3f} ms")
        return result
    return wrapper

@timer
def slow_sum(n):
    return sum(range(n))

slow_sum(1_000_000)


# ---- MEMOIZATION / CACHE DECORATOR ----
print("\nmemoization decorator :")

def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("fibonacci(10) :", fibonacci(10))
print("fibonacci(30) :", fibonacci(30))

# python built-in caching decorator
from functools import lru_cache

@lru_cache(maxsize=128)
def fib_cached(n):
    if n <= 1:
        return n
    return fib_cached(n - 1) + fib_cached(n - 2)

print("lru_cache fibonacci(35) :", fib_cached(35))
print("cache info :", fib_cached.cache_info())


# ---- VALIDATION DECORATOR ----
print("\nvalidation decorator :")

def validate_positive(*arg_indices):
    """Validate that specified positional arguments are positive"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in arg_indices:
                if i < len(args) and args[i] <= 0:
                    raise ValueError(f"argument at position {i} must be positive")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_positive(0, 1)
def rectangle_area(width, height):
    return width * height

try:
    print("area(5, 3) :", rectangle_area(5, 3))
    print("area(-1, 3) :", rectangle_area(-1, 3))
except ValueError as e:
    print(f"  validation error: {e}")


# ---- CLASS-BASED DECORATOR ----
print("\nclass-based decorator :")

class CountCalls:
    """Decorator that counts how many times a function is called"""
    def __init__(self, func):
        self.func = func
        self.count = 0
        wraps(func)(self)

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"  call #{self.count} to {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def process(data):
    return f"processed: {data}"

print(process("first"))
print(process("second"))
print(process("third"))
print("total calls :", process.count)


# ---- BUILT-IN DECORATORS ----
print("\nbuilt-in python decorators :")

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        import math
        return math.pi * self._radius ** 2

    @staticmethod
    def is_valid_radius(r):
        return r > 0

    @classmethod
    def unit_circle(cls):
        return cls(1)

c = Circle.unit_circle()
print("unit circle area :", f"{c.area:.4f}")
print("is_valid_radius(-1) :", Circle.is_valid_radius(-1))
print("is_valid_radius(5) :", Circle.is_valid_radius(5))

print("\nall decorator concepts demonstrated successfully")
