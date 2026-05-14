# operators in python

# arithmetic operators
# used for basic mathematical calculations

a = 20
b = 5

print("addition :", a + b)
print("subtraction :", a - b)
print("multiplication :", a * b)
print("division :", a / b)             # returns float
print("floor division :", a // b)      # returns int (rounds down)
print("modulus (remainder) :", a % b)
print("exponentiation :", a ** b)


# assignment operators
# used to assign and update values in variables

x = 10
print("\nsimple assignment x :", x)

x += 5
print("after x += 5 :", x)

x -= 3
print("after x -= 3 :", x)

x *= 2
print("after x *= 2 :", x)

x //= 4
print("after x //= 4 :", x)

x **= 2
print("after x **= 2 :", x)

x %= 3
print("after x %= 3 :", x)


# comparison operators
# used to compare two values and return True or False

p = 10
q = "10"
r = 5

print("\nequal (==) :", p == int(q))
print("not equal (!=) :", p != r)
print("greater than (>) :", p > r)
print("less than (<) :", r < p)
print("greater than or equal (>=) :", p >= 10)
print("less than or equal (<=) :", r <= 5)

# identity operators - check if same object in memory
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print("\nidentity operator (is) :", list1 is list3)
print("identity operator (is not) :", list1 is not list2)


# logical operators
# used to combine multiple conditions

is_student = True
has_completed_projects = True
loves_programming = False

print("\nand operator (and) :", is_student and has_completed_projects)
print("or operator (or) :", is_student or loves_programming)
print("not operator (not) :", not loves_programming)


# practical example using logical operators
age = 22
has_certificate = True

if age >= 18 and has_certificate:
    print("eligible for job")
else:
    print("not eligible")


# bitwise operators
# operate on binary representations of integers

num1 = 12  # binary: 1100
num2 = 10  # binary: 1010

print("\nbitwise AND (&) :", num1 & num2)    # 1000 = 8
print("bitwise OR (|) :", num1 | num2)       # 1110 = 14
print("bitwise XOR (^) :", num1 ^ num2)      # 0110 = 6
print("bitwise NOT (~) :", ~num1)            # -13
print("left shift (<<) :", num1 << 1)        # 11000 = 24
print("right shift (>>) :", num1 >> 1)       # 0110 = 6


# membership operators
# check if value exists in a sequence

fruits = ["apple", "banana", "mango"]
print("\nmembership (in) :", "apple" in fruits)
print("membership (not in) :", "grape" not in fruits)

text = "hello python"
print("substring check (in) :", "python" in text)


# walrus operator (python 3.8+)
# assigns value and evaluates in same expression

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
if (n := len(numbers)) > 5:
    print(f"\nwalrus operator: list has {n} elements, which is greater than 5")


# operator precedence (high to low)
# () > ** > ~,+,- (unary) > *,/,//,% > +,- > <<,>> > & > ^ > | > comparisons > not > and > or

result = 2 + 3 * 4 ** 2
print("\noperator precedence (2 + 3 * 4 ** 2) :", result)

result_with_parens = (2 + 3) * 4 ** 2
print("with parentheses ((2 + 3) * 4 ** 2) :", result_with_parens)


# typeof equivalent - type() and isinstance()
print("\ntype() examples :")
print("type of string :", type("Bhawandeep Kaur"))
print("type of number :", type(12))
print("type of boolean :", type(True))
print("type of list :", type([1, 2, 3]))
print("type of dict :", type({"key": "value"}))

print("\nall operators demonstrated successfully")
