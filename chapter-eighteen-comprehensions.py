# comprehensions in python
# comprehensions provide concise syntax to create new sequences from existing ones
# they are more readable and often faster than equivalent for loops

# ---- LIST COMPREHENSION ----
print("list comprehension :")

# basic: [expression for item in iterable]
squares = [x**2 for x in range(1, 11)]
print("squares :", squares)

# with condition: [expression for item in iterable if condition]
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print("even squares :", even_squares)

# transform strings
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print("upper words :", upper_words)

# filtering
numbers = [-4, -2, 0, 1, 3, 6, -1, 8]
positives = [n for n in numbers if n > 0]
print("positives :", positives)

# multiple conditions
filtered = [x for x in range(50) if x % 2 == 0 if x % 3 == 0]
print("divisible by 2 and 3 :", filtered)

# if-else in expression (ternary)
labels = ["even" if x % 2 == 0 else "odd" for x in range(10)]
print("even/odd labels :", labels)


# ---- NESTED LIST COMPREHENSION ----
print("\nnested list comprehension :")

# flatten a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [item for row in matrix for item in row]
print("flattened matrix :", flat)

# create multiplication table (2D)
table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
print("5x5 multiplication table :")
for row in table:
    print("  ", row)

# all pairs from two lists
pairs = [(a, b) for a in [1, 2, 3] for b in ["x", "y"]]
print("pairs :", pairs)

# pythagorean triples
triples = [(a, b, c)
           for c in range(1, 20)
           for b in range(1, c)
           for a in range(1, b)
           if a**2 + b**2 == c**2]
print("pythagorean triples :", triples)


# ---- DICT COMPREHENSION ----
print("\ndict comprehension :")

# basic: {key: value for item in iterable}
square_map = {x: x**2 for x in range(1, 6)}
print("square_map :", square_map)

# swap keys and values
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
print("swapped :", swapped)

# filter dict entries
prices = {"apple": 0.5, "banana": 0.3, "cherry": 1.5, "date": 2.0}
affordable = {fruit: price for fruit, price in prices.items() if price < 1.0}
print("affordable :", affordable)

# word length dict
words = ["python", "is", "great", "and", "powerful"]
word_lengths = {word: len(word) for word in words}
print("word lengths :", word_lengths)

# from two lists
keys = ["name", "age", "city"]
values = ["Alice", 30, "London"]
profile = {k: v for k, v in zip(keys, values)}
print("profile :", profile)


# ---- SET COMPREHENSION ----
print("\nset comprehension :")

# basic: {expression for item in iterable}
unique_lengths = {len(word) for word in ["hello", "hi", "hey", "howdy"]}
print("unique lengths :", unique_lengths)

vowels = {char for char in "hello world python" if char in "aeiou"}
print("unique vowels :", vowels)

# remove duplicates while transforming
nums = [1, 2, 2, 3, 3, 3, 4]
doubled_unique = {x * 2 for x in nums}
print("doubled unique :", doubled_unique)


# ---- GENERATOR EXPRESSIONS ----
print("\ngenerator expressions :")

# syntax like list comp but with () - lazy evaluation
gen = (x**2 for x in range(10))
print("generator object :", gen)
print("sum using gen expression :", sum(x**2 for x in range(10)))
print("max using gen expression :", max(x**3 for x in range(1, 6)))
print("any :", any(x > 3 for x in [1, 2, 5]))
print("all :", all(x > 0 for x in [1, 2, 3]))

# generator expressions are memory-efficient
# this never builds the full list in memory:
big_sum = sum(x**2 for x in range(1_000_000))
print("sum of squares 0-999999 :", big_sum)


# ---- PERFORMANCE COMPARISON ----
print("\nperformance comparison (list comp vs loop) :")
import time

# list comprehension
start = time.time()
result = [x**2 for x in range(100_000)]
comp_time = time.time() - start

# traditional loop
start = time.time()
result2 = []
for x in range(100_000):
    result2.append(x**2)
loop_time = time.time() - start

print(f"  list comprehension : {comp_time * 1000:.2f} ms")
print(f"  for loop           : {loop_time * 1000:.2f} ms")
print(f"  results equal      : {result == result2}")


# ---- COMPREHENSION SUMMARY ----
print("\ncomprehension syntax summary :")
print("  list  : [expr for x in iterable if cond]")
print("  dict  : {key: val for x in iterable if cond}")
print("  set   : {expr for x in iterable if cond}")
print("  gen   : (expr for x in iterable if cond)")

print("\nall comprehension concepts demonstrated successfully")
