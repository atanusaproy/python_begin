# Dunder methods or magic methods

# __str__ : This method is called when you use the str() function on an object. It should return a string representation of the object.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def __str__(self):
        return f"My Person object name is {self.name}, age is {self.age}"


person = Person("Atanu", 30)
#print(person)

# __repr__ : This method is called when you use the repr() function on an object. It should return a string that, when passed to eval(), would create an object with the same state as the original object.

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __str__(self):
        return f"My User object username is {self.username}, email is {self.email}"

    def __repr__(self):
        return f"This is a python user Object: User('{self.username}', '{self.email}')"


user = User("atanu", "atanu@gmail.com")
print(str(user))
print(repr(user))



# __len__ : This method is called when you use the len() function on an object. It should return the length of the object

class School:
    def __init__(self, name, students):
        self.name = name
        self.students = students

    def __len__(self):
       return len(self.students)


school = School("ABC School", ["Alice", "Bob", "Charlie"])

print(len(school))


# __eq__ : This method is called when you use the == operator to compare two objects. It should return True if the objects are equal, and False otherwise.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.name == other.name and self.age == other.age
        return False


student1 = Student("Atanu", 30)
student2 = Student("Arnab", 330)

print(student1 == student2)
