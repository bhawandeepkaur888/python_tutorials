# type conversion and strings in python


# type conversion
# converting one data type to another

# implicit conversion examples
# python automatically converts types in some operations
print("implicit conversion examples :")

implicit1 = 5 + 2.5
print("int + float result :", implicit1)
print("type :", type(implicit1))

implicit2 = True + 10
print("True + 10 result :", implicit2)


# explicit conversion (type casting)
# manual conversion using built-in functions

print("\nexplicit conversion examples :")

# int() - convert to integer
print("int('25') :", int("25"))
print("int(25.99) :", int(25.99))     # truncates decimal
print("int(True) :", int(True))
print("int(False) :", int(False))

# float() - convert to float
print("\nfloat('25.5') :", float("25.5"))
print("float(25) :", float(25))
print("float('1e3') :", float("1e3"))

# str() - convert to string
print("\nstr(100) :", str(100))
print("str(3.14) :", str(3.14))
print("str(True) :", str(True))
print("str([1, 2, 3]) :", str([1, 2, 3]))

# bool() - convert to boolean
print("\nbool(1) :", bool(1))
print("bool(0) :", bool(0))
print("bool('') :", bool(""))
print("bool('hello') :", bool("hello"))
print("bool([]) :", bool([]))
print("bool([1, 2]) :", bool([1, 2]))
print("bool(None) :", bool(None))

# list(), tuple(), set() conversions
print("\nlist((1, 2, 3)) :", list((1, 2, 3)))
print("tuple([1, 2, 3]) :", tuple([1, 2, 3]))
print("set([1, 2, 2, 3]) :", set([1, 2, 2, 3]))


# strings in python

# creating different types of strings
student_name = "Bhawandeep Kaur"
course = 'python basics'
message = f"welcome to learning python"
multiline = """this is a
multi-line string"""

print("\nstring examples :")
print("double quotes string :", student_name)
print("single quotes string :", course)
print("f-string :", message)
print("multiline :", multiline)


# string methods
print("\nstring methods :")

# length
print("length of student_name :", len(student_name))

# case conversion
print("uppercase :", student_name.upper())
print("lowercase :", student_name.lower())
print("title case :", student_name.title())
print("swap case :", student_name.swapcase())

# strip whitespace
text_with_spaces = "   hello world   "
print("\noriginal with spaces :", text_with_spaces)
print("after strip() :", text_with_spaces.strip())
print("after lstrip() :", text_with_spaces.lstrip())
print("after rstrip() :", text_with_spaces.rstrip())

# find and check
print("\nfind 'Kaur' :", student_name.find("Kaur"))
print("starts with 'Bha' :", student_name.startswith("Bha"))
print("ends with 'Kaur' :", student_name.endswith("Kaur"))
print("'python' in course :", "python" in course)

# replace
print("\nreplace 'Kaur' with 'Singh' :", student_name.replace("Kaur", "Singh"))

# split and join
skills_text = "HTML,CSS,Python,Django"
skills_list = skills_text.split(",")
print("\nsplit by comma :", skills_list)
print("join with ' | ' :", " | ".join(skills_list))

# slicing strings  [start:stop:step]
print("\nstring slicing :")
word = "PythonProgramming"
print("word[0:6] :", word[0:6])
print("word[:6] :", word[:6])
print("word[6:] :", word[6:])
print("word[-11:] :", word[-11:])
print("word[::2] :", word[::2])       # every 2nd character
print("reversed :", word[::-1])       # reverse a string

# string formatting
print("\nstring formatting :")
projects_completed = 12
# f-strings (python 3.6+) - recommended
print(f"hi my name is {student_name} and i have completed {projects_completed} projects")
# .format() method
print("hi my name is {} and i completed {} projects".format(student_name, projects_completed))
# % formatting (old style)
print("hi my name is %s and i completed %d projects" % (student_name, projects_completed))

# useful string methods
text = "  hello python  "
print("\ncount 'l' in hello :", "hello".count("l"))
print("isdigit('123') :", "123".isdigit())
print("isalpha('abc') :", "abc".isalpha())
print("isalnum('abc123') :", "abc123".isalnum())
print("center 'hi' in 20 chars :", "hi".center(20, "*"))
print("zfill 42 to 6 digits :", "42".zfill(6))

print("\nall type conversion and string concepts demonstrated successfully")
