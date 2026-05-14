# loops in python

# for loop - iterate over a sequence
print("for loop with range :")
for i in range(5):
    print(f"  iteration: {i}")

# range(start, stop, step)
print("\nfor loop range(1, 10, 2) :")
for i in range(1, 10, 2):
    print(f"  {i}", end=" ")
print()

# for loop over a list
fruits = ["apple", "banana", "mango"]
print("\nfor loop over list :")
for fruit in fruits:
    print(f"  {fruit}")

# for loop with index using enumerate()
print("\nfor loop with enumerate :")
for index, fruit in enumerate(fruits):
    print(f"  index {index}: {fruit}")

# for loop over string
print("\nfor loop over string :")
for char in "Python":
    print(f"  {char}", end=" ")
print()

# for loop over dictionary
person = {"name": "Alice", "age": 25, "city": "Delhi"}
print("\nfor loop over dict keys :")
for key in person:
    print(f"  {key}: {person[key]}")

print("\nfor loop over dict items :")
for key, value in person.items():
    print(f"  {key} -> {value}")


# while loop - runs while condition is True
print("\nwhile loop :")
count = 0
while count < 5:
    print(f"  while loop: {count}")
    count += 1


# while with user-like condition
num = 10
print("\nwhile loop (num starts at 10, runs while < 15) :")
while num < 15:
    print(f"  num: {num}")
    num += 1


# do-while equivalent in python
# python has no do-while, but we can simulate it
print("\ndo-while equivalent :")
value = 10
while True:
    print(f"  value: {value}")
    value += 1
    if value >= 13:
        break


# break statement - exit the loop
print("\nbreak statement :")
for i in range(10):
    if i == 5:
        print(f"  breaking at i={i}")
        break
    print(f"  i: {i}")


# continue statement - skip current iteration
print("\ncontinue statement :")
for i in range(10):
    if i % 2 == 0:
        continue    # skip even numbers
    print(f"  odd: {i}")


# else clause on loops
# runs when loop completes without hitting break
print("\nfor-else (no break) :")
for i in range(3):
    print(f"  i: {i}")
else:
    print("  loop completed normally (else block)")

print("\nfor-else (with break) :")
for i in range(5):
    if i == 3:
        print(f"  breaking at i={i}")
        break
    print(f"  i: {i}")
else:
    print("  this won't print because break was hit")


# nested loops
print("\nnested loops (multiplication table 1-3) :")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"  {i} x {j} = {i * j}")


# looping with zip() - iterate two lists in parallel
names = ["Alice", "Bob", "Charlie"]
scores = [90, 85, 92]
print("\nzip() loop :")
for name, score in zip(names, scores):
    print(f"  {name}: {score}")


# looping with reversed()
print("\nreversed() loop :")
for item in reversed(fruits):
    print(f"  {item}")


# looping with sorted()
unsorted = [5, 1, 3, 2, 4]
print("\nsorted() loop :")
for item in sorted(unsorted):
    print(f"  {item}", end=" ")
print()


# pass statement - placeholder (does nothing)
print("\npass statement :")
for i in range(3):
    pass    # placeholder, no error

print("loop with pass ran without error")

print("\nall loops demonstrated successfully")
