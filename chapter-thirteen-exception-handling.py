# exception handling in python
# exceptions are errors that occur during program execution
# python allows you to catch and handle exceptions gracefully

# ---- BASIC TRY / EXCEPT ----
print("basic try/except :")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("  caught ZeroDivisionError: cannot divide by zero")


# ---- CATCHING MULTIPLE EXCEPTIONS ----
print("\ncatching multiple exceptions :")

def risky_operation(value):
    try:
        number = int(value)
        result = 100 / number
        return result
    except ValueError:
        print(f"  ValueError: '{value}' is not a valid integer")
    except ZeroDivisionError:
        print("  ZeroDivisionError: cannot divide by zero")

risky_operation("abc")
risky_operation(0)
risky_operation(5)


# ---- CATCHING MULTIPLE IN ONE LINE ----
print("\ncatching multiple exceptions in one except :")
try:
    items = [1, 2, 3]
    print(items[10])
except (IndexError, TypeError) as e:
    print(f"  caught: {type(e).__name__}: {e}")


# ---- TRY / EXCEPT / ELSE / FINALLY ----
print("\ntry/except/else/finally :")
try:
    x = int("42")
except ValueError as e:
    print(f"  error: {e}")
else:
    print(f"  else block: conversion succeeded, x = {x}")
finally:
    print("  finally block: always runs regardless of exception")


# ---- ACCESSING EXCEPTION DETAILS ----
print("\naccessing exception details :")
try:
    result = "hello" + 5
except TypeError as e:
    print(f"  exception message: {e}")
    print(f"  exception type: {type(e).__name__}")
    print(f"  exception args: {e.args}")


# ---- RAISING EXCEPTIONS ----
print("\nraising exceptions :")

def validate_age(age):
    if not isinstance(age, int):
        raise TypeError("age must be an integer")
    if age < 0:
        raise ValueError("age cannot be negative")
    if age > 150:
        raise ValueError("age is unrealistically high")
    return f"valid age: {age}"

try:
    print(validate_age(25))
    print(validate_age(-5))
except ValueError as e:
    print(f"  ValueError: {e}")

try:
    print(validate_age("twenty"))
except TypeError as e:
    print(f"  TypeError: {e}")


# ---- CUSTOM EXCEPTIONS ----
print("\ncustom exceptions :")

class AppError(Exception):
    """Base exception for this application"""
    pass

class DatabaseError(AppError):
    """Raised when a database operation fails"""
    def __init__(self, message, query=None):
        super().__init__(message)
        self.query = query

class AuthenticationError(AppError):
    """Raised when authentication fails"""
    pass

def connect_to_db(host):
    if host == "":
        raise DatabaseError("empty host provided", query="CONNECT")
    return f"connected to {host}"

def login(username, password):
    if password != "secret":
        raise AuthenticationError(f"invalid password for user: {username}")
    return "login successful"

try:
    connect_to_db("")
except DatabaseError as e:
    print(f"  DatabaseError: {e}")
    print(f"  failed query: {e.query}")

try:
    login("admin", "wrongpass")
except AuthenticationError as e:
    print(f"  AuthenticationError: {e}")

try:
    login("admin", "secret")
    print("  login succeeded")
except AuthenticationError as e:
    print(f"  error: {e}")


# ---- EXCEPTION HIERARCHY ----
print("\ncommon exception hierarchy :")
print("""
  BaseException
  └── Exception
      ├── ArithmeticError
      │   └── ZeroDivisionError
      ├── LookupError
      │   ├── IndexError
      │   └── KeyError
      ├── ValueError
      ├── TypeError
      ├── NameError
      ├── IOError / OSError
      │   └── FileNotFoundError
      ├── AttributeError
      ├── ImportError
      ├── RuntimeError
      │   └── RecursionError
      └── StopIteration
""")


# ---- EXCEPTION CHAINING ----
print("exception chaining :")

try:
    try:
        data = {"key": "value"}
        print(data["missing"])
    except KeyError as original:
        raise ValueError("key not found in config") from original
except ValueError as e:
    print(f"  chained exception: {e}")
    print(f"  original cause: {e.__cause__}")


# ---- CONTEXT MANAGER FOR EXCEPTIONS ----
print("\nsuppressing exceptions with contextlib :")
from contextlib import suppress

with suppress(FileNotFoundError):
    open("nonexistent_file.txt")    # would normally raise FileNotFoundError
print("  execution continued after suppressed exception")


# ---- ASSERT STATEMENT ----
print("\nassert statement :")
def divide(a, b):
    assert b != 0, "divisor must not be zero"
    return a / b

try:
    print("divide(10, 2) :", divide(10, 2))
    divide(10, 0)
except AssertionError as e:
    print(f"  AssertionError: {e}")

print("\nall exception handling concepts demonstrated successfully")
