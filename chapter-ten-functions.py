# functions in python
# functions allow you to define reusable blocks of code
# defined with def keyword

# basic function
def greet():
    print("Hello, World!")

greet()


# function with parameters
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Bhawandeep")
greet_user("Alice")


# function with return value
def add(a, b):
    return a + b

result = add(5, 3)
print("\nadd(5, 3) :", result)


# default parameter values
def greet_with_message(name, message="Welcome!"):
    print(f"{name}: {message}")

greet_with_message("Alice")
greet_with_message("Bob", "Good morning!")


# keyword arguments (can pass in any order)
def describe_person(name, age, city):
    print(f"{name} is {age} years old from {city}")

describe_person(age=22, city="Delhi", name="Bhawan")


# returning multiple values (returns a tuple)
def get_min_max(numbers):
    return min(numbers), max(numbers)

low, high = get_min_max([5, 1, 9, 3, 7])
print("\nmin and max :", low, high)


# *args - variable number of positional arguments
def total(*args):
    print(f"args received: {args}")
    return sum(args)

print("\ntotal(1,2,3) :", total(1, 2, 3))
print("total(1,2,3,4,5) :", total(1, 2, 3, 4, 5))


# **kwargs - variable number of keyword arguments
def show_info(**kwargs):
    print("kwargs received :")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

show_info(name="Alice", age=20, city="Paris")


# combining all parameter types
def all_params(required, default="hello", *args, **kwargs):
    print(f"\nrequired: {required}")
    print(f"default: {default}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

all_params("must", "world", 1, 2, 3, color="blue", size=10)


# lambda functions - anonymous single-expression functions
square = lambda x: x ** 2
multiply = lambda x, y: x * y

print("\nlambda square(4) :", square(4))
print("lambda multiply(3, 5) :", multiply(3, 5))

# lambdas are useful with map(), filter(), sorted()
nums = [5, 2, 8, 1, 9, 3]
sorted_nums = sorted(nums, key=lambda x: x)
print("sorted :", sorted_nums)

pairs = [(1, "b"), (3, "a"), (2, "c")]
sorted_by_second = sorted(pairs, key=lambda pair: pair[1])
print("sorted by second :", sorted_by_second)


# nested functions (inner functions)
def outer(x):
    def inner(y):
        return x + y       # inner accesses outer variable (closure)
    return inner

add_five = outer(5)
print("\nclosure add_five(3) :", add_five(3))
print("closure add_five(10) :", add_five(10))


# closures explained
def make_counter():
    count = 0
    def counter():
        nonlocal count          # allows modifying outer variable
        count += 1
        return count
    return counter

counter1 = make_counter()
counter2 = make_counter()
print("\ncounter1:", counter1(), counter1(), counter1())
print("counter2:", counter2(), counter2())      # independent state


# docstrings - document your functions
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The area of the rectangle.
    """
    return length * width

print("\ncalculate_area(5, 3) :", calculate_area(5, 3))
print("docstring :", calculate_area.__doc__)


# recursive functions - function calling itself
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print("\nfactorial(5) :", factorial(5))
print("factorial(10) :", factorial(10))


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("fibonacci(10) :", fibonacci(10))


# functions as first-class objects (pass as arguments)
def apply(func, value):
    return func(value)

def double(x):
    return x * 2

print("\napply(double, 5) :", apply(double, 5))
print("apply(square, 4) :", apply(square, 4))


# function annotations (type hints)
def add_numbers(a: int, b: int) -> int:
    return a + b

print("\nadd_numbers(3, 4) :", add_numbers(3, 4))
print("annotations :", add_numbers.__annotations__)

print("\nall function concepts demonstrated successfully")
