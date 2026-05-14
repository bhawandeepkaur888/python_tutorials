# introduction and setup

# what is python
# python is a high-level, interpreted programming language
# it is known for its simple and readable syntax
# created by guido van rossum and first released in 1991

# where python is used
# 1. web development - using frameworks like django and flask
# 2. data science and machine learning - using pandas, numpy, tensorflow
# 3. automation and scripting
# 4. desktop and mobile applications
# 5. game development
# 6. DevOps and cloud automation

# how to run python
# 1. python interpreter (interactive shell / REPL)
# 2. running a .py file using: python filename.py
# 3. jupyter notebooks
# 4. online editors like repl.it or google colab

print("hello world")
print("welcome to python learning")


# variables in python
# python is dynamically typed - no need to declare variable types

# assigning values
student_name = "Bhawandeep Kaur"
print("student name :", student_name)

age = 24
print("age :", age)

is_student = True
print("is student :", is_student)

# python uses snake_case for variable names (convention)
birth_year = 2000
projects_completed = 12
print("birth year :", birth_year)
print("projects completed :", projects_completed)


# rules for naming variables
# - must start with a letter or underscore (_)
# - cannot start with a number
# - can contain letters, numbers, and underscores
# - python is case sensitive (name and Name are different)
# - cannot use reserved keywords like if, for, while, class, etc.

my_age = 24
_score = 95
price_in_dollars = 299
print("valid variable names :", my_age, _score, price_in_dollars)


# multiple assignment in python
x, y, z = 10, 20, 30
print("multiple assignment :", x, y, z)

# assign same value to multiple variables
a = b = c = 100
print("same value assignment :", a, b, c)


# constants in python
# python does not have built-in constants
# by convention, constants are written in UPPERCASE
MAX_SIZE = 100
PI = 3.14159
print("constant MAX_SIZE :", MAX_SIZE)
print("constant PI :", PI)


# checking data type using type()
print("type of student_name :", type(student_name))
print("type of age :", type(age))
print("type of is_student :", type(is_student))


# comments in python
# single line comment starts with #

"""
this is a multi-line comment
also called a docstring
used to describe modules, functions, and classes
"""

# print with multiple values
print("name:", student_name, "| age:", age, "| student:", is_student)

# print with separator and end
print("python", "is", "awesome", sep="-")
print("this line ends with a dot", end=".\n")

print("basic python introduction completed successfully")
