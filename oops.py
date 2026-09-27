# Object-Oriented Programming in Python
# What is Object-Oriented Programming (OOP)?

# Procedural programming

def helloWorld():
    print("Hello, World!")

customer_name = "Atanu"
bank_balance = 100000
def deposit(amount):
    return bank_balance + amount

def withdraw(amount):
    return bank_balance - amount

def check_balance():
    return bank_balance


# Procedural to OOPs

class BankAccount:
    def __init__(self, customer_name, bank_balance):
        self.customer_name = customer_name
        self.bank_balance = bank_balance

    def deposit(self, amount):
        self.bank_balance += amount

    def withdraw(self, amount):
        self.bank_balance -= amount

    def check_balance(self):
        return self.bank_balance


atanu_account = BankAccount("Atanu", 100000)
arnab_account = BankAccount("Arnab", 50000)
atanu_account.check_balance()
arnab_account.check_balance()

# BankAccount.__init__(BankAccount, "Arnab", 50000) is a constructor method


# __init__ method is a constructor method in Python.

class Car:

    _make = "Toyota"
    _model = "Camry"

    def start(self):
        self.__model = "Corolla"
        print("Car is starting.")

    def stop(self):
        print("Car is stopping.")

    def do_car_start(self):
        
        
        self.start()

my_car = Car()
# Car.__init__(Car) is a constructor method



class Person():
    def __init__(self, name, age):
        
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    def introduce_myself(self):
        self.introduce()


person = Person("Atanu", 35)
person.introduce()


#@classmethod

class Student:
    school_name = "ABC School"
    name = None
    age = None


    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def get_school_name(cls, new_school_name, student_name=None, student_age=None):
        cls.school_name = new_school_name
        return cls(student_name, student_age)


my_student = Student("Atanu", 35)
print(my_student.name)  # Output: XYZ School

#print(my_student.get_school_name("XYZ School", "Arnab", 25).name)  # Output: XYZ School
Student.get_school_name("XYZ School", "Arnab", 25)



#@staticmethod

class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        sum_result = MathOperations.add(a, b)
        print(f"Sum of {a} and {b} is: {sum_result}")
        return a - b

    
MathOperations.add(5, 10)  # Output: 15

class Config:
    @staticmethod
    def get_config_value(key):
        config = {
            "database": "my_database",
            "host": "localhost",
            "port": 5432
        }
        return config.get(key, None)


# Encapsulation -> Data Hiding


class BankAccount:
    def __init__(self, customer_name, bank_balance):
        self.customer_name = customer_name
        self.__bank_balance = bank_balance

    def deposit(self, amount):
        self.__bank_balance += amount

    def withdraw(self, amount):
        self.__bank_balance -= amount

    def check_balance(self):
        return self.__bank_balance

    # Using getter
    @property
    def balance(self):
        return self.__bank_balance

    # Using setter
    @balance.setter
    def balance(self, value):
        if value < 0:
            print("Balance cannot be negative.")
        else:
            self.__bank_balance = value


atanu_account = BankAccount("Atanu", 100000)
print(atanu_account.check_balance())
print(atanu_account.balance)
atanu_account.balance = -50000
print(atanu_account.balance)
#print(atanu_account.__bank_balance) 

# atanu_account._bank_balance = 50000
# print(atanu_account._bank_balance) 
