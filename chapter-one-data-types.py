# data types in python

# python has several built-in data types
# python is dynamically typed - the type is inferred automatically


# numeric types

# int - whole numbers (positive, negative, zero)
completed_projects = 12
temperature = -5
zero_value = 0
print("int (completed_projects) :", completed_projects)
print("int (temperature) :", temperature)
print("type :", type(completed_projects))

# float - decimal numbers
pi_value = 3.14159
price = 99.99
negative_float = -2.5
print("\nfloat (pi_value) :", pi_value)
print("float (price) :", price)
print("type :", type(pi_value))

# complex - numbers with real and imaginary parts
complex_num = 3 + 4j
print("\ncomplex (complex_num) :", complex_num)
print("real part :", complex_num.real)
print("imaginary part :", complex_num.imag)
print("type :", type(complex_num))


# string type

# str - sequence of characters
student_name = "Bhawandeep Kaur"
single_quote = 'python is awesome'
multiline = """this is a
multiline string"""
print("\nstring (student_name) :", student_name)
print("string (single_quote) :", single_quote)
print("multiline string :", multiline)
print("type :", type(student_name))


# boolean type

# bool - True or False (capital T and F in python)
loves_python = True
is_completed = False
print("\nbool (loves_python) :", loves_python)
print("bool (is_completed) :", is_completed)
print("type :", type(loves_python))

# booleans are actually subclass of int
print("True as int :", int(True))
print("False as int :", int(False))


# none type

# NoneType - represents absence of value (like null in other languages)
mission = None
print("\nNoneType (mission) :", mission)
print("type :", type(mission))
print("is mission None? :", mission is None)


# sequence types

# list - ordered, mutable collection
skills = ["HTML", "CSS", "Python", "Django"]
print("\nlist (skills) :", skills)
print("type :", type(skills))

# tuple - ordered, immutable collection
coordinates = (10.5, 20.3)
print("tuple (coordinates) :", coordinates)
print("type :", type(coordinates))

# range - sequence of numbers
number_range = range(1, 6)
print("range (1 to 5) :", list(number_range))
print("type :", type(number_range))


# mapping type

# dict - key-value pairs (unordered in older python, ordered from python 3.7+)
developer = {
    "name": "Bhawandeep Kaur",
    "goal": "learning python",
    "year": 2026
}
print("\ndict (developer) :", developer)
print("type :", type(developer))


# set types

# set - unordered, mutable, no duplicates
unique_numbers = {1, 2, 3, 4, 5}
print("\nset (unique_numbers) :", unique_numbers)
print("type :", type(unique_numbers))

# frozenset - unordered, immutable, no duplicates
frozen = frozenset([1, 2, 3])
print("frozenset (frozen) :", frozen)
print("type :", type(frozen))


# binary types

# bytes - immutable sequence of bytes
byte_data = b"hello"
print("\nbytes (byte_data) :", byte_data)
print("type :", type(byte_data))

# bytearray - mutable sequence of bytes
byte_arr = bytearray(5)
print("bytearray (byte_arr) :", byte_arr)
print("type :", type(byte_arr))


# checking types with isinstance()
print("\nisinstance() checks :")
print("is student_name a str? :", isinstance(student_name, str))
print("is completed_projects an int? :", isinstance(completed_projects, int))
print("is pi_value a float? :", isinstance(pi_value, float))
print("is loves_python a bool? :", isinstance(loves_python, bool))


# mutable vs immutable types
# immutable: int, float, complex, str, tuple, frozenset, bytes
# mutable:   list, dict, set, bytearray

print("\nmutable vs immutable :")
original_list = [1, 2, 3]
original_list.append(4)
print("list is mutable - after append :", original_list)

original_str = "hello"
# strings are immutable - cannot change characters in place
new_str = original_str + " world"
print("string is immutable - new string created :", new_str)

print("\nall data types demonstrated successfully")
