# What is a function?

def function_name():
    # Code to be executed
    return "Hello, World!" #Optional

print(function_name())

# without return statement
def print_hello(): 
    # Code to be executed
    print("Hello, World!") #Optional

print_hello()


# Function parameters and arguments

def add(numberA, numberB):
    return numberA + numberB

print(add(1, 2))

# numberA and numberB are parameters
# 1 and 2 are arguments


# Default parameters
def add(numberA: int, numberB: int = 2) -> int:
    return numberA + numberB

print(add()) # 1 + 2 = 3
print(add(3)) # 3 + 2 = 5
print(add(1, 2)) # 1 + 2 = 3 (overriding the default values)

# Keyword arguments
def add(numberA = 0, numberB = 0):
    return numberA + numberB

print(add(numberB = 1, numberA = 2))


# Return statement
def multiple_return_values():
    return "Hello", "World", 30

print(multiple_return_values())

# multiple_return_values() returns a tuple
# so we can assign it to multiple variables
hel, wor, age = multiple_return_values()
print(hel)
print(wor)
print(age)

# Lambda functions