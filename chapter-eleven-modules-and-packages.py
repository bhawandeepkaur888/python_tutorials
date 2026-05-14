# modules and packages in python
# modules are .py files that contain functions, classes, and variables
# packages are directories containing modules

# importing entire module
import math
print("math.pi :", math.pi)
print("math.sqrt(16) :", math.sqrt(16))
print("math.ceil(4.2) :", math.ceil(4.2))
print("math.floor(4.9) :", math.floor(4.9))
print("math.pow(2, 10) :", math.pow(2, 10))
print("math.factorial(5) :", math.factorial(5))
print("math.log(100, 10) :", math.log(100, 10))


# importing specific names
from math import pi, e, sqrt
print("\npi :", pi)
print("e :", e)
print("sqrt(25) :", sqrt(25))


# importing with alias
import math as m
print("\nmath aliased as m :", m.sin(0))

from math import factorial as fact
print("factorial aliased as fact(6) :", fact(6))


# random module
import random
print("\nrandom module :")
print("random float [0,1) :", random.random())
print("random int [1,10] :", random.randint(1, 10))
print("random choice :", random.choice(["apple", "banana", "mango"]))

sample_list = [1, 2, 3, 4, 5]
random.shuffle(sample_list)
print("shuffled list :", sample_list)

print("random sample :", random.sample([10, 20, 30, 40, 50], 3))


# os module - interacting with operating system
import os
print("\nos module :")
print("current directory :", os.getcwd())
print("os name :", os.name)

# os.path - path utilities
print("\nos.path :")
full_path = os.path.join("folder", "subfolder", "file.txt")
print("joined path :", full_path)
print("basename :", os.path.basename(full_path))
print("dirname :", os.path.dirname(full_path))
print("split ext :", os.path.splitext("script.py"))
print("exists (cwd) :", os.path.exists(os.getcwd()))


# sys module - system-specific parameters
import sys
print("\nsys module :")
print("python version :", sys.version)
print("platform :", sys.platform)
print("executable :", sys.executable)
print("module search paths (first 2) :", sys.path[:2])


# datetime module
from datetime import datetime, date, timedelta
print("\ndatetime module :")

now = datetime.now()
print("now :", now)
print("year :", now.year)
print("month :", now.month)
print("day :", now.day)
print("hour :", now.hour)

today = date.today()
print("today :", today)

# formatting dates
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("formatted :", formatted)

# parsing date string
parsed = datetime.strptime("2024-01-15", "%Y-%m-%d")
print("parsed :", parsed)

# arithmetic with dates
future = today + timedelta(days=30)
print("30 days from today :", future)

diff = date(2025, 12, 31) - today
print("days until end of 2025 :", diff.days)


# json module
import json
print("\njson module :")

# python dict to JSON string
data = {"name": "Alice", "age": 25, "skills": ["python", "java"]}
json_string = json.dumps(data, indent=2)
print("json.dumps() :\n", json_string)

# JSON string to python dict
parsed_data = json.loads(json_string)
print("json.loads() :", parsed_data)
print("type after loads :", type(parsed_data))


# collections module
from collections import defaultdict, OrderedDict, Counter, deque, namedtuple

print("\ncollections module :")

# defaultdict - dict with default factory
word_count = defaultdict(int)
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
for word in words:
    word_count[word] += 1
print("defaultdict word count :", dict(word_count))

# Counter - count hashable objects
counter = Counter(words)
print("Counter :", counter)
print("most common :", counter.most_common(2))

# deque - efficient append/pop from both ends
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
print("deque :", dq)
dq.popleft()
print("after popleft :", dq)


# itertools module
import itertools
print("\nitertools module :")
print("count (first 5) :", list(itertools.islice(itertools.count(1), 5)))
print("cycle (first 7) :", list(itertools.islice(itertools.cycle("AB"), 7)))
print("permutations :", list(itertools.permutations([1, 2, 3], 2)))
print("combinations :", list(itertools.combinations([1, 2, 3, 4], 2)))
print("chain :", list(itertools.chain([1, 2], [3, 4], [5])))


# __name__ == "__main__" pattern
# code inside this block only runs when file is executed directly
# not when imported as a module

def main():
    print("\nmain() function running")
    print("this is the entry point")

if __name__ == "__main__":
    main()
    print("this file is being run directly, not imported")

print("\nall module concepts demonstrated successfully")
