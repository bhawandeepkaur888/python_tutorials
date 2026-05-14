# sets in python
# sets are unordered, mutable, and contain no duplicate values
# sets are useful for membership testing and removing duplicates

# creating sets
fruits = {"apple", "banana", "mango", "orange"}
numbers = {1, 2, 3, 4, 5}
empty_set = set()       # cannot use {} for empty set (that creates empty dict)
from_list = set([1, 2, 2, 3, 3, 4])   # duplicates removed

print("fruits set :", fruits)
print("numbers set :", numbers)
print("empty set :", empty_set)
print("set from list (duplicates removed) :", from_list)
print("type :", type(fruits))


# sets are unordered - order is not guaranteed
print("\nnote: sets are unordered, output order may vary")


# adding elements
colors = {"red", "green", "blue"}
colors.add("yellow")                    # add single element
print("\nafter add('yellow') :", colors)

colors.update(["purple", "orange"])     # add multiple elements
print("after update() :", colors)


# removing elements
sample = {1, 2, 3, 4, 5}
sample.remove(3)                # raises KeyError if not found
print("\nafter remove(3) :", sample)

sample.discard(10)              # no error if element not found
print("after discard(10) :", sample)

popped = sample.pop()           # removes and returns a random element
print("popped :", popped)
print("after pop() :", sample)

sample.clear()                  # remove all elements
print("after clear() :", sample)


# set operations
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print("\nset A :", set_a)
print("set B :", set_b)

# union - all elements from both sets
print("\nunion (|) :", set_a | set_b)
print("union method :", set_a.union(set_b))

# intersection - only common elements
print("intersection (&) :", set_a & set_b)
print("intersection method :", set_a.intersection(set_b))

# difference - elements in A but not in B
print("difference A-B (-) :", set_a - set_b)
print("difference method :", set_a.difference(set_b))

# symmetric difference - elements in either but not both
print("symmetric difference (^) :", set_a ^ set_b)
print("symmetric difference method :", set_a.symmetric_difference(set_b))


# subset and superset checks
small = {1, 2, 3}
large = {1, 2, 3, 4, 5}

print("\nsmall :", small)
print("large :", large)
print("is small subset of large? (<= or issubset) :", small <= large)
print("is large superset of small? (>= or issuperset) :", large >= small)
print("is small proper subset? (< strict) :", small < large)
print("are sets disjoint? (no common elements) :", {1, 2}.isdisjoint({3, 4}))


# set membership testing (very fast - O(1))
print("\nmembership testing :")
big_set = set(range(1000))
print("500 in set :", 500 in big_set)
print("9999 in set :", 9999 in big_set)


# using sets to remove duplicates from a list
duplicate_list = [1, 2, 2, 3, 4, 4, 5, 5, 5]
unique_list = list(set(duplicate_list))
print("\noriginal list :", duplicate_list)
print("unique list :", sorted(unique_list))


# set comprehension
squared_set = {x**2 for x in range(1, 6)}
print("\nset comprehension (squares) :", squared_set)

even_set = {x for x in range(20) if x % 2 == 0}
print("even numbers set :", even_set)


# frozenset - immutable version of a set
frozen = frozenset([1, 2, 3, 4, 5])
print("\nfrozenset :", frozen)
print("type :", type(frozen))
# frozen.add(6)  # this would raise AttributeError

# frozenset can be used as a dictionary key
lookup = {frozenset([1, 2]): "pair one", frozenset([3, 4]): "pair two"}
print("frozenset as dict key :", lookup[frozenset([1, 2])])


# iterating over a set
print("\niterating over set :")
for item in {10, 20, 30, 40}:
    print(f"  {item}")


# update operations that modify the set in place
set_x = {1, 2, 3, 4}
set_y = {3, 4, 5, 6}

set_x.intersection_update(set_y)        # keep only common elements
print("\nintersection_update result :", set_x)

set_x = {1, 2, 3, 4}
set_x.difference_update(set_y)          # remove elements in y from x
print("difference_update result :", set_x)

set_x = {1, 2, 3, 4}
set_x.symmetric_difference_update(set_y)  # keep only non-common elements
print("symmetric_difference_update result :", set_x)

print("\nall set concepts demonstrated successfully")
