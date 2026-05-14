# inheritance in python
# inheritance allows a class to derive properties and methods from another class
# promotes code reuse and hierarchical design

# ---- SINGLE INHERITANCE ----
print("single inheritance :")

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}"

    def breathe(self):
        return f"{self.name} breathes air"

    def __str__(self):
        return f"Animal({self.name})"


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Woof")    # call parent __init__
        self.breed = breed

    def fetch(self):
        return f"{self.name} fetches the ball!"

    # method overriding
    def speak(self):
        return f"{self.name} barks loudly: {self.sound}!!!"

    def __str__(self):
        return f"Dog({self.name}, {self.breed})"


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Meow")

    def purr(self):
        return f"{self.name} is purring..."


dog = Dog("Buddy", "Labrador")
cat = Cat("Whiskers")

print("dog :", dog)
print("dog.speak() :", dog.speak())
print("dog.fetch() :", dog.fetch())
print("dog.breathe() :", dog.breathe())    # inherited from Animal

print("cat :", cat)
print("cat.speak() :", cat.speak())        # inherited (not overridden)
print("cat.purr() :", cat.purr())


# ---- isinstance() and issubclass() ----
print("\nisinstance() and issubclass() :")
print("isinstance(dog, Dog) :", isinstance(dog, Dog))
print("isinstance(dog, Animal) :", isinstance(dog, Animal))
print("isinstance(cat, Dog) :", isinstance(cat, Dog))
print("issubclass(Dog, Animal) :", issubclass(Dog, Animal))
print("issubclass(Cat, Animal) :", issubclass(Cat, Animal))
print("issubclass(Dog, Cat) :", issubclass(Dog, Cat))


# ---- MULTI-LEVEL INHERITANCE ----
print("\nmulti-level inheritance :")

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def info(self):
        return f"{self.make} {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)
        self.doors = doors

    def car_info(self):
        return f"{self.info()} ({self.doors} doors)"


class ElectricCar(Car):
    def __init__(self, make, model, doors, battery_kw):
        super().__init__(make, model, doors)
        self.battery_kw = battery_kw

    def full_info(self):
        return f"{self.car_info()} | battery: {self.battery_kw} kWh"


tesla = ElectricCar("Tesla", "Model 3", 4, 75)
print("tesla.info() :", tesla.info())
print("tesla.car_info() :", tesla.car_info())
print("tesla.full_info() :", tesla.full_info())


# ---- MULTIPLE INHERITANCE ----
print("\nmultiple inheritance :")

class Flyable:
    def fly(self):
        return f"{self.__class__.__name__} is flying"

class Swimmable:
    def swim(self):
        return f"{self.__class__.__name__} is swimming"

class Duck(Animal, Flyable, Swimmable):
    def __init__(self, name):
        Animal.__init__(self, name, "Quack")

    def describe(self):
        return f"{self.name} can fly and swim!"

donald = Duck("Donald")
print("duck.speak() :", donald.speak())
print("duck.fly() :", donald.fly())
print("duck.swim() :", donald.swim())
print("duck.describe() :", donald.describe())


# ---- METHOD RESOLUTION ORDER (MRO) ----
print("\nMRO (Method Resolution Order) :")
print("Duck MRO :")
for cls in Duck.__mro__:
    print(f"  {cls.__name__}")


# ---- MIXIN PATTERN ----
print("\nmixin pattern :")

class LogMixin:
    def log(self, message):
        print(f"  [{self.__class__.__name__}] LOG: {message}")

class ValidateMixin:
    def validate(self, data):
        if not data:
            raise ValueError("data cannot be empty")
        return True

class UserService(LogMixin, ValidateMixin):
    def __init__(self, name):
        self.name = name

    def save(self, data):
        self.validate(data)
        self.log(f"saving data for {self.name}: {data}")
        return True

service = UserService("Alice")
service.save({"email": "alice@example.com"})


# ---- super() in depth ----
print("\nsuper() with multiple inheritance :")

class Base:
    def greet(self):
        print("  Base.greet()")

class A(Base):
    def greet(self):
        print("  A.greet()")
        super().greet()

class B(Base):
    def greet(self):
        print("  B.greet()")
        super().greet()

class C(A, B):
    def greet(self):
        print("  C.greet()")
        super().greet()

c = C()
c.greet()
print("  C MRO :", [cls.__name__ for cls in C.__mro__])

print("\nall inheritance concepts demonstrated successfully")
