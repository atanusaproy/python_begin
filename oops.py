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


# Inheritance
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start(self):
        print(f"{self.make} {self.model} is starting.")

    def stop(self):
        print(f"{self.make} {self.model} is stopping.")

    def drive(self):
        print(f"{self.make} {self.model} is driving.")


class ElectricCar():
    def __init__(self, make, model, num_doors, battery_capacity):
        super().__init__(make, model, num_doors)
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"{self.make} {self.model} is charging with a battery capacity of {self.battery_capacity} kWh.")

class PetrolCar():
    def __init__(self, make, model, num_doors, fuel_capacity):
        super().__init__(make, model, num_doors)
        self.fuel_capacity = fuel_capacity

    def refuel(self):
        print(f"{self.make} {self.model} is refueling with a fuel capacity of {self.fuel_capacity} liters.")

class ElectricBike():
    def __init__(self, make, model, num_wheels, battery_capacity):
        super().__init__(make, model, num_wheels)
        self.battery_capacity = battery_capacity


class ECar(Vehicle, ElectricCar):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

class PCar(Vehicle, PetrolCar):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

class Bike(Vehicle):
    def __init__(self, make, model, num_wheels):
        super().__init__(make, model)
        self.num_wheels = num_wheels


my_car = Car("Toyota", "Camry", 4)
my_car.start()
my_car.stop()
my_car.drive()

my_bike = Bike("Honda", "CBR", 2)
my_bike.start()
my_bike.stop()
my_bike.drive()


#---------------------------------------------------

class Document:
    def __init__(self, file_name):
        self.file_name = file_name

    def get_file_name(self):
        return self.file_name


class PDFDocument(Document):
    def __init__(self, file_name, num_pages):
        super().__init__(file_name)
        self.num_pages = num_pages

    def get_num_pages(self):
        return self.num_pages


class WordDocument(Document):
    def __init__(self, file_name, num_words):
        super().__init__(file_name)
        self.num_words = num_words

    def get_num_words(self):
        return self.num_words

    def get_file_name(self):
        return f"{self.file_name} (Word Document)"

class SpreadsheetDocument(Document):
    def __init__(self, file_name, num_sheets):
        super().__init__(file_name)
        self.num_sheets = num_sheets

    def get_num_sheets(self):
        return self.num_sheets


my_pdf_file = PDFDocument("my_file.pdf", 10)
my_pdf_file.get_num_pages()  # Output: 10
my_pdf_file.get_file_name()  # Output: my_file.pdf


my_word_file = WordDocument("my_word_file.docx", 100)
my_word_file.get_num_words()  # Output: 100
my_word_file.get_file_name()  # Output: my_word_file.docx

my_spreadsheet_file = SpreadsheetDocument("my_spreadsheet.xlsx", 5)
my_spreadsheet_file.get_num_sheets()  # Output: 5
my_spreadsheet_file.get_file_name()  # Output: my_spreadsheet.xlsx


# Polymorphism
class Animal:
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return "Woof woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow meow!"


def make_animal_sound(animal):
    print(animal.make_sound())

my_dog = Dog()
make_animal_sound(my_dog)  # Output: Woof woof!

my_cat = Cat()
make_animal_sound(my_cat)  # Output: Meow meow!


