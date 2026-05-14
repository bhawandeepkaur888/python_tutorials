# functional programming in python
# functional programming treats computation as evaluation of mathematical functions
# key concepts: map, filter, reduce, lambdas, pure functions, immutability

# ---- LAMBDA FUNCTIONS ----
print("lambda functions :")

# lambda: anonymous one-line function
# syntax: lambda args: expression
double = lambda x: x * 2
add = lambda x, y: x + y
square = lambda x: x ** 2

print("double(5) :", double(5))
print("add(3, 4) :", add(3, 4))
print("square(6) :", square(6))

# lambda with conditional expression
is_even = lambda n: "even" if n % 2 == 0 else "odd"
print("is_even(7) :", is_even(7))
print("is_even(10) :", is_even(10))


# ---- MAP ----
print("\nmap() :")
# map(function, iterable) - applies function to every element, returns iterator

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared = list(map(lambda x: x**2, numbers))
print("map squares :", squared)

strings = list(map(str, numbers))
print("map to strings :", strings)

names = ["alice", "bob", "charlie"]
capitalized = list(map(str.capitalize, names))
print("map capitalize :", capitalized)

# map over two iterables
a = [1, 2, 3, 4]
b = [10, 20, 30, 40]
sums = list(map(lambda x, y: x + y, a, b))
print("map two lists :", sums)

# equivalent list comprehension
squared_comp = [x**2 for x in numbers]
print("equivalent comp :", squared_comp)


# ---- FILTER ----
print("\nfilter() :")
# filter(function, iterable) - returns elements where function returns True

evens = list(filter(lambda x: x % 2 == 0, numbers))
print("filter evens :", evens)

long_words = list(filter(lambda w: len(w) > 4, ["hi", "hello", "python", "world"]))
print("filter long words :", long_words)

# filter None values
mixed = [0, 1, None, 2, "", "hello", False, True]
truthy = list(filter(None, mixed))    # None as predicate filters falsy values
print("filter truthy :", truthy)

# combined map + filter
result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, range(10))))
print("squares of even numbers :", result)


# ---- REDUCE ----
print("\nreduce() :")
from functools import reduce

# reduce(function, iterable) - accumulates result

total = reduce(lambda acc, x: acc + x, numbers)
print("reduce sum :", total)

product = reduce(lambda acc, x: acc * x, [1, 2, 3, 4, 5])
print("reduce product :", product)

maximum = reduce(lambda a, b: a if a > b else b, numbers)
print("reduce max :", maximum)

# with initial value
total_from_100 = reduce(lambda acc, x: acc + x, numbers, 100)
print("reduce sum from 100 :", total_from_100)

# build string from list
words = ["Python", "is", "awesome"]
sentence = reduce(lambda a, b: a + " " + b, words)
print("reduce sentence :", sentence)


# ---- sorted() WITH KEY ----
print("\nsorted() with key :")

fruits = ["banana", "apple", "cherry", "date", "elderberry"]
print("sorted by name :", sorted(fruits))
print("sorted by length :", sorted(fruits, key=len))
print("sorted by last char :", sorted(fruits, key=lambda w: w[-1]))
print("sorted reverse :", sorted(fruits, reverse=True))

# sort list of dicts
people = [
    {"name": "Charlie", "age": 35},
    {"name": "Alice",   "age": 25},
    {"name": "Bob",     "age": 30},
]
by_age  = sorted(people, key=lambda p: p["age"])
by_name = sorted(people, key=lambda p: p["name"])
print("sort by age :", [p["name"] for p in by_age])
print("sort by name :", [p["name"] for p in by_name])


# ---- zip() AND enumerate() ----
print("\nzip() and enumerate() :")

keys   = ["a", "b", "c", "d"]
values = [1, 2, 3, 4]
zipped = list(zip(keys, values))
print("zip :", zipped)

combined_dict = dict(zip(keys, values))
print("zip to dict :", combined_dict)

# unzip
k, v = zip(*zipped)
print("unzip keys :", k)
print("unzip values :", v)

# zip with multiple iterables
names  = ["Alice", "Bob", "Charlie"]
ages   = [25, 30, 35]
cities = ["London", "Paris", "Tokyo"]
for name, age, city in zip(names, ages, cities):
    print(f"  {name}, {age}, {city}")

print("\nenumerate :")
for i, fruit in enumerate(["apple", "banana", "cherry"], start=1):
    print(f"  {i}. {fruit}")


# ---- any() AND all() ----
print("\nany() and all() :")

nums = [2, 4, 6, 8, 10]
print("all even :", all(x % 2 == 0 for x in nums))
print("any > 5 :", any(x > 5 for x in nums))
print("any negative :", any(x < 0 for x in nums))

checks = [True, True, False, True]
print("all(checks) :", all(checks))
print("any(checks) :", any(checks))


# ---- functools.partial ----
print("\nfunctools.partial :")
from functools import partial

def power(base, exp):
    return base ** exp

square  = partial(power, exp=2)
cube    = partial(power, exp=3)
square5 = partial(power, 5)    # fix first argument

print("square(4) :", square(4))
print("cube(3) :", cube(3))
print("square5(2) :", square5(2))

# partial with built-ins
from functools import partial
int_from_bin = partial(int, base=2)
print("int_from_bin('1010') :", int_from_bin("1010"))


# ---- PURE FUNCTIONS ----
print("\npure functions (no side effects) :")

# pure - same input always gives same output
def pure_add(a, b):
    return a + b

# function composition
def compose(f, g):
    return lambda x: f(g(x))

add1      = lambda x: x + 1
double    = lambda x: x * 2
add1_then_double = compose(double, add1)   # double(add1(x))

print("compose double(add1(5)) :", add1_then_double(5))

# chain of transformations in functional style
data = range(1, 11)
result = list(
    map(lambda x: x**2,
        filter(lambda x: x % 2 == 0, data))
)
print("squares of evens 1-10 :", result)

print("\nall functional programming concepts demonstrated successfully")
