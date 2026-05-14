# dictionaries in python
# dictionaries store key-value pairs
# ordered (python 3.7+), mutable, no duplicate keys

# creating dictionaries
person = {
    "name": "Bhawandeep Kaur",
    "age": 22,
    "city": "Delhi",
    "is_student": True
}
print("person :", person)
print("type :", type(person))

# empty dictionary
empty_dict = {}
also_empty = dict()
print("empty dict :", empty_dict)

# creating with dict() constructor
student = dict(name="Alice", age=20, grade="A")
print("dict() constructor :", student)


# accessing values
print("\naccessing values :")
print("name :", person["name"])              # raises KeyError if not found
print("age with get() :", person.get("age")) # returns None if not found
print("missing key :", person.get("phone", "not available"))  # default value


# modifying dictionaries (mutable)
person["age"] = 23              # update existing key
person["phone"] = "9876543210"  # add new key
print("\nafter modification :", person)


# removing keys
sample = {"a": 1, "b": 2, "c": 3, "d": 4}
removed = sample.pop("b")              # remove and return value
print("\npopped 'b' :", removed)
print("after pop :", sample)

sample.popitem()                       # remove last inserted item
print("after popitem() :", sample)

del sample["a"]                        # delete by key
print("after del :", sample)

sample.clear()                         # remove all items
print("after clear() :", sample)


# dictionary methods
info = {
    "name": "Bhawan",
    "project": 12,
    "is_student": False
}

print("\nkeys() :", list(info.keys()))
print("values() :", list(info.values()))
print("items() :", list(info.items()))

# update() - merge another dict
info.update({"city": "Delhi", "project": 15})
print("after update() :", info)


# checking keys
print("\n'name' in info :", "name" in info)
print("'salary' in info :", "salary" in info)
print("'name' not in info :", "name" not in info)


# iterating over dictionaries
print("\niterating keys :")
for key in info:
    print(f"  {key}")

print("\niterating values :")
for value in info.values():
    print(f"  {value}")

print("\niterating items :")
for key, value in info.items():
    print(f"  {key}: {value}")


# nested dictionaries
school = {
    "student1": {
        "name": "Alice",
        "marks": {"math": 90, "science": 85}
    },
    "student2": {
        "name": "Bob",
        "marks": {"math": 78, "science": 92}
    }
}
print("\nnested dictionary :")
print("student1 name :", school["student1"]["name"])
print("student1 math :", school["student1"]["marks"]["math"])


# dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}
print("\ndictionary comprehension (squares) :", squares)

even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print("even squares :", even_squares)


# setdefault() - get value or set default if key not found
config = {"host": "localhost"}
port = config.setdefault("port", 8080)
print("\nsetdefault result :", port)
print("config after setdefault :", config)


# copying dictionaries
original = {"a": 1, "b": 2}
shallow_copy = original.copy()         # shallow copy
shallow_copy["c"] = 3
print("\noriginal after shallow copy modification :", original)
print("shallow copy :", shallow_copy)

import copy
nested_dict = {"a": [1, 2, 3], "b": [4, 5, 6]}
deep_copy = copy.deepcopy(nested_dict)
deep_copy["a"].append(99)
print("\noriginal after deep copy modification :", nested_dict)
print("deep copy :", deep_copy)


# merging dictionaries (python 3.9+)
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = dict1 | dict2              # merge operator
print("\nmerged dicts :", merged)

# unpacking to merge (works in all python 3.5+)
merged2 = {**dict1, **dict2}
print("merged with ** unpacking :", merged2)


# counting with dictionaries
words = ["apple", "banana", "apple", "mango", "banana", "apple"]
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print("\nword count :", word_count)

# using Counter from collections (better approach)
from collections import Counter
counter = Counter(words)
print("Counter :", counter)
print("most common :", counter.most_common(2))

print("\nall dictionary concepts demonstrated successfully")
