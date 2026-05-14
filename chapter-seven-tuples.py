# tuples in python
# tuples are ordered, immutable, and allow duplicate values
# use tuples for data that should not change

# creating tuples
coordinates = (10.5, 20.3)
colors = ("red", "green", "blue")
single_item = (42,)        # must have trailing comma for single item
empty_tuple = ()
mixed_tuple = (1, "hello", True, 3.14)

print("coordinates :", coordinates)
print("colors :", colors)
print("single item tuple :", single_item)
print("empty tuple :", empty_tuple)
print("type :", type(coordinates))

# tuple without parentheses (tuple packing)
packed = 1, 2, 3
print("\npacked tuple (no parens) :", packed)
print("type :", type(packed))


# accessing tuple elements
fruits = ("apple", "banana", "mango", "orange")
print("\nfirst element [0] :", fruits[0])
print("last element [-1] :", fruits[-1])


# tuple slicing
print("\ntuple slicing :")
print("fruits[1:3] :", fruits[1:3])
print("fruits[:2] :", fruits[:2])
print("fruits[2:] :", fruits[2:])
print("fruits[::-1] :", fruits[::-1])


# tuples are immutable - cannot modify after creation
# fruits[0] = "grape"  # this will raise TypeError


# tuple methods
numbers_tuple = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5)
print("\ncount of 5 :", numbers_tuple.count(5))
print("index of 9 :", numbers_tuple.index(9))
print("length :", len(numbers_tuple))
print("min :", min(numbers_tuple))
print("max :", max(numbers_tuple))
print("sum :", sum(numbers_tuple))


# tuple unpacking
point = (10, 20, 30)
x, y, z = point
print("\ntuple unpacking :")
print("x:", x, "y:", y, "z:", z)

# extended unpacking
first, *middle, last = (1, 2, 3, 4, 5)
print("first:", first, "| middle:", middle, "| last:", last)

# swap variables using tuple unpacking
a, b = 10, 20
print(f"\nbefore swap: a={a}, b={b}")
a, b = b, a
print(f"after swap: a={a}, b={b}")


# nested tuples
nested = ((1, 2), (3, 4), (5, 6))
print("\nnested tuple :", nested)
print("nested[1][0] :", nested[1][0])


# converting between list and tuple
my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
back_to_list = list(my_tuple)
print("\nlist to tuple :", my_tuple)
print("tuple to list :", back_to_list)


# tuples as dictionary keys (lists cannot be dict keys)
locations = {
    (40.7128, -74.0060): "New York",
    (51.5074, -0.1278): "London",
    (28.6139, 77.2090): "New Delhi"
}
print("\ntuples as dict keys :")
for coords, city in locations.items():
    print(f"  {coords} -> {city}")


# named tuples - more readable tuples (from collections module)
from collections import namedtuple

Student = namedtuple("Student", ["name", "age", "grade"])
student1 = Student(name="Bhawandeep Kaur", age=22, grade="A")

print("\nnamed tuple :")
print("student :", student1)
print("name :", student1.name)
print("age :", student1.age)
print("grade :", student1.grade)
print("access by index :", student1[0])


# tuple vs list - when to use which
# use tuple when: data should not change, using as dict key, returning multiple values
# use list when: data needs to be modified, order matters, duplicates needed

# function returning multiple values (automatically a tuple)
def get_dimensions():
    return 1920, 1080  # returns a tuple

width, height = get_dimensions()
print(f"\nscreen dimensions: {width} x {height}")


# checking membership
print("\nmembership check :")
print("'apple' in fruits :", "apple" in fruits)
print("'grape' in fruits :", "grape" in fruits)


# iterating over tuples
print("\niterating over tuple :")
for color in colors:
    print(f"  {color}")

print("\nall tuple concepts demonstrated successfully")
