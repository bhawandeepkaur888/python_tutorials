# lists in python
# lists are ordered, mutable, and allow duplicate values

# creating lists
numbers = [1, 2, 3, 4, 5]
mixed = [1, "text", True, None, 3.14]
empty_list = []
nested = [[1, 2], [3, 4], [5, 6]]

print("numbers :", numbers)
print("mixed :", mixed)
print("nested :", nested)
print("type :", type(numbers))


# accessing list elements
fruits = ["apple", "banana", "mango", "orange", "grape"]
print("\naccessing elements :")
print("first element [0] :", fruits[0])
print("last element [-1] :", fruits[-1])
print("second from last [-2] :", fruits[-2])


# list slicing [start:stop:step]
print("\nlist slicing :")
print("fruits[1:3] :", fruits[1:3])
print("fruits[:3] :", fruits[:3])
print("fruits[2:] :", fruits[2:])
print("fruits[::2] :", fruits[::2])
print("fruits[::-1] :", fruits[::-1])   # reverse


# modifying lists (lists are mutable)
colors = ["red", "green", "blue"]
colors[1] = "yellow"
print("\nafter modification :", colors)


# adding elements
arr = [1, 2, 3, 4, 5]
arr.append(6)               # add to end
print("\nafter append(6) :", arr)

arr.insert(0, 0)            # insert at specific index
print("after insert(0, 0) :", arr)

arr.extend([7, 8, 9])       # add multiple elements
print("after extend([7,8,9]) :", arr)


# removing elements
sample = [10, 20, 30, 40, 50, 30]
sample.remove(30)           # removes first occurrence of value
print("\nafter remove(30) :", sample)

popped = sample.pop()       # removes and returns last element
print("popped :", popped)
print("after pop() :", sample)

popped_at = sample.pop(1)   # removes and returns element at index
print("popped at index 1 :", popped_at)
print("after pop(1) :", sample)

del sample[0]               # delete by index
print("after del [0] :", sample)

sample.clear()              # remove all elements
print("after clear() :", sample)


# searching in lists
search_list = [10, 20, 30, 40, 50]
print("\nindex of 30 :", search_list.index(30))
print("count of 20 :", search_list.count(20))
print("is 40 in list? :", 40 in search_list)
print("is 99 in list? :", 99 in search_list)


# sorting lists
nums = [5, 1, 3, 2, 4]
nums.sort()                         # sort in place ascending
print("\nafter sort() :", nums)

nums.sort(reverse=True)             # sort descending
print("after sort(reverse=True) :", nums)

words = ["banana", "apple", "cherry"]
words.sort(key=len)                 # sort by string length
print("sorted by length :", words)

sorted_nums = sorted([5, 1, 3, 2, 4])  # returns new sorted list
print("sorted() returns new list :", sorted_nums)


# other useful list methods
demo = [1, 2, 3]
demo.reverse()              # reverse in place
print("\nafter reverse() :", demo)

copy_list = demo.copy()     # shallow copy
print("copy of list :", copy_list)

print("length of list :", len(demo))
print("min of [5,1,3,2,4] :", min([5, 1, 3, 2, 4]))
print("max of [5,1,3,2,4] :", max([5, 1, 3, 2, 4]))
print("sum of [5,1,3,2,4] :", sum([5, 1, 3, 2, 4]))


# iterating over lists
print("\niterating over list :")
for item in [10, 20, 30]:
    print(f"  {item}")

# list unpacking
first, second, *rest = [1, 2, 3, 4, 5]
print("\nlist unpacking :")
print("first :", first)
print("second :", second)
print("rest :", rest)


# 2D lists (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("\n2D list (matrix) :")
for row in matrix:
    print(" ", row)
print("element at row 1, col 2 :", matrix[1][2])


# list concatenation and repetition
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print("\nconcatenation :", list1 + list2)
print("repetition :", list1 * 3)

print("\nall list concepts demonstrated successfully")
