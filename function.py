# What is a function?

def function_name():
    # Code to be executed
    return "Hello, World!" #Optional

#print(function_name())

# without return statement
def print_hello(): 
    # Code to be executed
    print("Hello, World!") #Optional

#print_hello()


# Function parameters and arguments

def add(numberA, numberB):
    return numberA + numberB

#print(add(1, 2))

# numberA and numberB are parameters
# 1 and 2 are arguments


# Default parameters
def add(numberA: int, numberB: int = 2) -> int:
    return numberA + numberB

#print(add()) # 1 + 2 = 3
#print(add(3)) # 3 + 2 = 5
#print(add(1, 2)) # 1 + 2 = 3 (overriding the default values)

# Keyword arguments
def add(numberA = 0, numberB = 0):
    return numberA + numberB

#print(add(numberB = 1, numberA = 2))


# Return statement
def multiple_return_values():
    return "Hello", "World", 30

print(multiple_return_values())

# Variable scope — local vs global

#Local scope

def get_house_member():
    house_member = "Harry Potter"

    return house_member

get_house_member()
# Here house_member is not defined because it is a local variable and can only be accessed within the function get_house_member().
#print(house_member)


#Global scope

house_member = "Harry Potter"

def get_house_member_global():
    return house_member

print(house_member)
get_house_member_global()

# *args and **kwargs
# Example of *args
# def add(numberA, numberB, numberC):
#     return numberA + numberB + numberC

def add(*args):
    #*args the args vaiable will be capture those values which has no keyword
    print(args)
    total = 0
    for number in args:
        total += number
    return total

result = add(1, 2, 3, 4, 5, 8, 9)
print(result)


# Example of **kwargs

def user_info(name, age, email):
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Age: {age}")

user_info(name = "Atanu", email = "atanu@gmail.com", age = 25)

def user_info_with_kwargs(*args, **kwargs):
    print("User info with kwargs")
    print(args)
    print(kwargs)


    print(f"Email: {kwargs['email']}")
    print(f"Age: {kwargs['age']}")

user_info_with_kwargs("Atanu", email = "atanu@gmail.com", age = 25)

def student(name, class_name, *subjects, **details):
    print(f"Name: {name}")
    print(f"Class: {class_name}")
    print(f"Subjects: {subjects}")
    print(f"Additional info: {details}")
    

student("Atanu", "class 10", "Javascript", "Python", "C++", email = "atanu@gmail.com", age = 25)

#Lambda (anonymous) functions

# This is the normal function example
def add(numberA, numberB):
    return numberA + numberB

# This is the lambda function example
add = lambda numberA, numberB: numberA + numberB
# How this works and how the syntax is diffrent
#lambda => this the the keyword to define a lambda function
# numberA, numberB => these are the parameters of the function
# : => this is the separator between the parameters and the expression
# numberA + numberB => this is the expression that the function will return

print(add(1, 2))

# Recursion — concept

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

# Built-in functions: print() , len() , range() , abs() , round() , sorted() , etc

print(len("Hello, World!")) # 13
print(abs(-5)) # 5
print(round(3.14559, 2)) # 3.15
print(sorted([3, 1, 4, 1, 5])) # [1, 1, 3, 4, 5]