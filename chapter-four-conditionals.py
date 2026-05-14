# conditionals in python

# if statement
age = 20
if age >= 18:
    print("you are eligible to vote.")


# if-else statement
balance = 500
if balance >= 1000:
    print("sufficient balance")
else:
    print("insufficient balance")


# if-elif-else chain
score = 85
if score >= 90:
    print("grade: A")
elif score >= 80:
    print("grade: B")
elif score >= 70:
    print("grade: C")
elif score >= 60:
    print("grade: D")
else:
    print("grade: F")


# nested if statements
is_logged_in = True
is_admin = False

if is_logged_in:
    if is_admin:
        print("welcome, admin!")
    else:
        print("welcome, user!")
else:
    print("please log in first")


# ternary (conditional) expression
# python equivalent of the ternary operator: value_if_true if condition else value_if_false

is_logged_in = True
message = "welcome back!" if is_logged_in else "please log in"
print(message)

number = 7
result = "odd" if number % 2 != 0 else "even"
print(f"{number} is {result}")


# match-case statement (python 3.10+)
# equivalent to switch-case in other languages

day = "Monday"
match day:
    case "Monday":
        print("start of the work week")
    case "Friday":
        print("end of the work week")
    case "Saturday" | "Sunday":
        print("weekend!")
    case _:
        print("mid-week day")


# match with patterns
point = (0, 5)
match point:
    case (0, 0):
        print("origin point")
    case (0, y):
        print(f"on y-axis at y={y}")
    case (x, 0):
        print(f"on x-axis at x={x}")
    case (x, y):
        print(f"point at ({x}, {y})")


# practical conditionals with logical operators
temperature = 28
is_raining = False

if temperature > 25 and not is_raining:
    print("good day to go outside")
elif temperature > 25 and is_raining:
    print("warm but rainy, carry an umbrella")
elif temperature <= 25 and not is_raining:
    print("cool and pleasant")
else:
    print("cold and rainy, stay indoors")


# using 'in' operator in conditions
valid_roles = ["admin", "editor", "viewer"]
user_role = "editor"

if user_role in valid_roles:
    print(f"{user_role} has access")
else:
    print("access denied")


# checking for None
user_input = None

if user_input is None:
    print("no input provided")
elif user_input == "":
    print("empty input provided")
else:
    print(f"input received: {user_input}")


# truthy and falsy values in conditions
# falsy: 0, 0.0, "", [], {}, (), set(), None, False
# truthy: everything else

values = [0, 1, "", "hello", [], [1, 2], None, True, False]
print("\ntruthy/falsy evaluation :")
for val in values:
    if val:
        print(f"{repr(val)} is truthy")
    else:
        print(f"{repr(val)} is falsy")

print("\nall conditionals demonstrated successfully")
