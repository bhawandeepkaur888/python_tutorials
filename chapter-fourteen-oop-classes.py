# object-oriented programming (OOP) in python
# classes are blueprints for creating objects
# objects bundle data (attributes) and behavior (methods)

# ---- DEFINING A CLASS ----
class Dog:
    # class variable - shared by all instances
    species = "Canis lupus familiaris"

    # __init__ - constructor, called when object is created
    def __init__(self, name, age, breed):
        # instance variables - unique to each object
        self.name = name
        self.age = age
        self.breed = breed

    # instance method
    def bark(self):
        return f"{self.name} says: Woof!"

    def describe(self):
        return f"{self.name} is a {self.age}-year-old {self.breed}"

    # __str__ - string representation for print()
    def __str__(self):
        return f"Dog(name={self.name}, age={self.age})"

    # __repr__ - detailed string representation for debugging
    def __repr__(self):
        return f"Dog('{self.name}', {self.age}, '{self.breed}')"


# creating objects (instances)
dog1 = Dog("Buddy", 3, "Labrador")
dog2 = Dog("Max", 5, "German Shepherd")

print("dog1 :", dog1)
print("dog2 :", dog2)
print("repr :", repr(dog1))
print("bark :", dog1.bark())
print("describe :", dog2.describe())
print("class variable :", dog1.species)
print("class variable via class :", Dog.species)


# ---- ACCESSING AND MODIFYING ATTRIBUTES ----
print("\nattribute access :")
print("dog1.name :", dog1.name)
dog1.age = 4                          # modify attribute
print("dog1.age after update :", dog1.age)
dog1.color = "golden"                 # add new attribute dynamically
print("dog1.color :", dog1.color)

print("hasattr :", hasattr(dog1, "color"))
print("getattr :", getattr(dog1, "breed"))
print("getattr default :", getattr(dog1, "weight", "unknown"))


# ---- PROPERTY DECORATOR ----
print("\n@property decorator :")

class Circle:
    def __init__(self, radius):
        self._radius = radius           # convention: _ means "private"

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("radius cannot be negative")
        self._radius = value

    @property
    def area(self):
        import math
        return math.pi * self._radius ** 2

    @property
    def circumference(self):
        import math
        return 2 * math.pi * self._radius

    def __str__(self):
        return f"Circle(radius={self._radius:.2f})"

c = Circle(5)
print("circle :", c)
print("radius :", c.radius)
print("area :", f"{c.area:.4f}")
print("circumference :", f"{c.circumference:.4f}")
c.radius = 10
print("radius after setter :", c.radius)


# ---- CLASS METHODS AND STATIC METHODS ----
print("\n@classmethod and @staticmethod :")

class BankAccount:
    interest_rate = 0.05              # class variable

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount
        return self.balance

    @classmethod
    def set_interest_rate(cls, rate):
        cls.interest_rate = rate

    @classmethod
    def create_empty(cls, owner):
        return cls(owner, 0)           # factory method

    @staticmethod
    def validate_amount(amount):
        return isinstance(amount, (int, float)) and amount > 0

    def __str__(self):
        return f"BankAccount(owner={self.owner}, balance={self.balance})"

account = BankAccount("Alice", 1000)
print("account :", account)
print("deposit 500 :", account.deposit(500))
print("withdraw 200 :", account.withdraw(200))

# class method usage
new_account = BankAccount.create_empty("Bob")
print("empty account :", new_account)

BankAccount.set_interest_rate(0.07)
print("updated interest rate :", BankAccount.interest_rate)

# static method usage
print("validate 100 :", BankAccount.validate_amount(100))
print("validate -50 :", BankAccount.validate_amount(-50))


# ---- MAGIC / DUNDER METHODS ----
print("\nmagic methods :")

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector({self.x!r}, {self.y!r})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __len__(self):
        return 2

    def __abs__(self):
        return (self.x**2 + self.y**2) ** 0.5

v1 = Vector(1, 2)
v2 = Vector(3, 4)

print("v1 + v2 :", v1 + v2)
print("v1 - v2 :", v1 - v2)
print("v1 * 3 :", v1 * 3)
print("v1 == v2 :", v1 == v2)
print("len(v1) :", len(v1))
print("abs(v2) :", f"{abs(v2):.4f}")

print("\nall OOP class concepts demonstrated successfully")
