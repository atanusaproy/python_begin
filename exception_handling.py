# Types of errors — syntax errors, runtime errors, logical errors


# Syntax Errors:

print("Hello")

if 10 > 9:
    print("10 is greater than 9")
else:
    print("10 is not greater than 9")

# Runtime Errors:

number = 10
dev_by_zero = number / 2
print(dev_by_zero)


numbers = [1, 2, 3, 4, 5]
print(numbers[1]) # IndexError: list index out of range

one_number = int("10")
print(one_number) # ValueError: invalid literal for int() with base 10: '10'

# Logical Errors:
product_price = 100
product_quantity = 10
total_price = product_price * product_quantity
print(f"Total price: {total_price}")


#try , except , else , finally blocks
try:
    one_number = int("10")
    number = 10
    dev_number = 2
    dev_by_zero = number / dev_number
    print(dev_by_zero)
except ZeroDivisionError:   
    print("Error: Division by zero")
except ValueError:
    print("Error: Invalid value")
except Exception as e:
    print(f"Error: {e}")
else:
    print("Else block executed")
finally:
    print("Finally block executed")


# Raising exceptions with raise

def raise_exception():
    raise Exception("This is a test exception")

#raise_exception()


# if 10 > 9:
#     raise Exception("10 is greater than 9")


# Custom exceptions
class InvalidAgeError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# def validate_age(age):
#     if age < 0:
#         raise InvalidAgeError("Age cannot be negative")
#     elif age < 18:
#         raise InvalidAgeError("Age cannot be less than 18")
#     else:
#         print("Age is valid")

user = {
    "name": "John",
    "age": 17,
    "email": "john@example.com"
}

try:
    if user["age"] < 18:
        raise InvalidAgeError("Age cannot be less than 18")
    else:
        print("Age is valid")
except InvalidAgeError as e:
    print(e)
except Exception as e:
    print(e)
finally:
    print("Finally block executed")


# Exception handling with files

# file = open("example.txt", "r")
# print(file.read())