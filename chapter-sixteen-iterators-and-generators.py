# iterators and generators in python
# iterators are objects that implement __iter__() and __next__()
# generators are a simpler way to create iterators using yield

# ---- ITERABLES vs ITERATORS ----
print("iterables vs iterators :")

# lists, strings, dicts are iterables (have __iter__)
my_list = [1, 2, 3]
my_iter = iter(my_list)       # iter() calls __iter__, returns iterator

print("next(iter) :", next(my_iter))
print("next(iter) :", next(my_iter))
print("next(iter) :", next(my_iter))

# StopIteration raised when exhausted
try:
    next(my_iter)
except StopIteration:
    print("StopIteration raised - iterator exhausted")


# for loop internally uses iter() and next()
print("\nfor loop uses iterator protocol internally:")
for item in [10, 20, 30]:
    print(f"  {item}")


# ---- CUSTOM ITERATOR CLASS ----
print("\ncustom iterator class :")

class CountDown:
    """Counts down from n to 0"""
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self         # iterator returns itself

    def __next__(self):
        if self.n < 0:
            raise StopIteration
        value = self.n
        self.n -= 1
        return value

countdown = CountDown(5)
print("CountDown from 5 :", list(countdown))

for num in CountDown(3):
    print(f"  {num}")


class RangeCustom:
    """Custom range-like iterator"""
    def __init__(self, start, stop, step=1):
        self.current = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        value = self.current
        self.current += self.step
        return value

print("custom range(0, 10, 2) :", list(RangeCustom(0, 10, 2)))


# ---- GENERATORS WITH yield ----
print("\ngenerators with yield :")

def count_up_to(n):
    """Generator that yields numbers from 1 to n"""
    count = 1
    while count <= n:
        yield count             # suspends execution, returns value
        count += 1

gen = count_up_to(5)
print("type :", type(gen))
print("next() :", next(gen))
print("next() :", next(gen))
print("remaining :", list(gen))   # consume rest


def count_down(n):
    while n >= 0:
        yield n
        n -= 1

print("countdown generator :", list(count_down(5)))


# ---- GENERATOR EXPRESSIONS ----
print("\ngenerator expressions :")

# list comprehension creates full list in memory
list_comp = [x**2 for x in range(10)]
print("list comp :", list_comp)

# generator expression is lazy - values created on demand
gen_expr = (x**2 for x in range(10))
print("gen expression :", gen_expr)
print("first 5 values :", [next(gen_expr) for _ in range(5)])

# sum of squares using generator
total = sum(x**2 for x in range(100))
print("sum of squares 0-99 :", total)


# ---- INFINITE GENERATORS ----
print("\ninfinite generators :")

def fibonacci():
    """Infinite Fibonacci sequence generator"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
first_10 = [next(fib) for _ in range(10)]
print("first 10 fibonacci :", first_10)


def natural_numbers():
    """Infinite natural numbers generator"""
    n = 1
    while True:
        yield n
        n += 1

import itertools
first_5_naturals = list(itertools.islice(natural_numbers(), 5))
print("first 5 natural numbers :", first_5_naturals)


# ---- yield FROM ----
print("\nyield from :")

def chain_generators(*iterables):
    """Chains multiple iterables together"""
    for it in iterables:
        yield from it         # delegates to sub-iterator

result = list(chain_generators([1, 2, 3], [4, 5], [6, 7, 8]))
print("chain_generators :", result)

def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)    # recursive yield from
        else:
            yield item

nested_list = [1, [2, 3], [4, [5, 6]], 7]
print("flattened :", list(flatten(nested_list)))


# ---- SENDING VALUES TO GENERATORS ----
print("\nsending values to generators :")

def accumulator():
    total = 0
    while True:
        value = yield total     # yield suspends AND receives via send()
        if value is None:
            break
        total += value

acc = accumulator()
next(acc)                        # prime the generator
print("send(10) :", acc.send(10))
print("send(20) :", acc.send(20))
print("send(5) :", acc.send(5))


# ---- PRACTICAL GENERATOR EXAMPLES ----
print("\npractical generator examples :")

def read_large_file(chunk_size=1024):
    """Simulate reading large file in chunks (memory efficient)"""
    data = "A" * 5000
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

chunks = list(read_large_file())
print(f"file read in {len(chunks)} chunks of 1024 chars")


def take(n, iterable):
    """Take first n elements from any iterable"""
    return list(itertools.islice(iterable, n))

print("take(5, fibonacci()) :", take(5, fibonacci()))
print("take(10, natural_numbers()) :", take(10, natural_numbers()))

print("\nall iterator and generator concepts demonstrated successfully")
