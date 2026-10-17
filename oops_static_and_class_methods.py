class Student:
    school_name = "ABC School"
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    @classmethod
    def get_school_name(cls, student_name=None, student_age=None):
        #return cls.school_name
        cls.school_name = "XYZ School"
        return cls(student_name, student_age)

my_student = Student("Atanu", 35 )
print(type(my_student))

atanu = Student.get_school_name("Atanu", 35)


# Classmethod Use case

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


    @classmethod 
    def from_dict(cls, user_dict):
        return cls(user_dict["username"], user_dict["email"])


arnab = {"username": "arnab123", "email": "arnab@gmail.com"}
arnar_object = User.from_dict(arnab)


# Staticmethod
class AppConfig:
    __api_base_url = "https://api.example.com"

    @staticmethod
    def get_base_url():
        return AppConfig.__api_base_url


AppConfig.get_base_url() 

#public, protected, private attribute
class MyClass:
    public_attribute = "I am public"
    _protected_attribute = "I am protected"
    __private_attribute = "I am private"

    def get_private_attribute(self):
        return self.__private_attribute


# Encapsulation
class BankAccount:
    __bank_balance = 0
    def __init__(self, customer_name, bank_balance):
        self.customer_name = customer_name
        self.__bank_balance = bank_balance

    def get_balance(self):
        return self.__bank_balance

    @property
    def balance(self):
        return self.__bank_balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            print("Balance cannot be negative.")
        else:
            self.__bank_balance = value

arnab_account = BankAccount("Arnab", 10000)
print(arnab_account.customer_name)
print(arnab_account.get_balance())

arnab_account.__bank_balance = 0
print(arnab_account.__bank_balance)  # This will not change the actual bank balance

print(arnab_account.get_balance())  # This will not change the actual bank balance

arnab_account.balance = 5000
print(arnab_account.balance)  # This will not change the actual bank balance arnab_account.balance

