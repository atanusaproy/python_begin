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
