# Dictionaries

# This is a dictionary
person = {"name": "John", "age": 25, "city": "New York"}

# "name" => key
# "John" => value

print("This is the original dictionary:",person)  # Accessing the value of the "name" key


person["name"] = "Atanu"  # Update the value of the "name" key
person["age"] = 30  # Update the value of the "age" key

print("This is the updated dictionary:",person)

student = { 101 : "Atanu", 102 : "Rohit", 103 : "Sourav"}




user = {"name": "Atanu", "age": 30, "city": "Kolkata"}

print("Name:", user["name"])
print("Age:", user["age"])
print("City:", user["city"])
user["country"] = "India"  # Adding a new key-value pair to the dictionary
print(user["country"])  # This will raise a KeyError since "country" key does not exist in the dictionary

print(user.get("name", "Unknown"))  # Printing the entire dictionary

# age delete from dictionary
del user["age"]  # Deleting the "age" key-value pair from the dictionary

print(user)

# Sets
numbers = {1, 2, 3, 4, 5}  # This is a set


print("This is the set:",numbers)
print(type(numbers))  # Printing the type of the set

empty_set = set()  # This is an empty set
print("This is the empty set:",empty_set)
print(type(empty_set))  # Printing the type of the empty set

user_ids = [101, 102, 103, 104, 101, 105, 102]  # This is a list of user IDs

user_ids_set = set(user_ids)  # This is a set of unique user IDs

print("This is the list of user IDs:",user_ids)
print("This is the set of unique user IDs:",user_ids_set)

# union, intersection, difference, symmetric difference

python_students = {"Atanu", "Rohit", "Sourav", "Ankit"}
java_students = {"Rohit", "Sourav", "Ankit", "Rahul"}

# Union of two sets
print("Python students:", python_students)
print("Java students:", java_students)
union_students = python_students.union(java_students)
print("Union of Python and Java students:", union_students)

# Intersection of two sets
intersection_students = python_students.intersection(java_students)
print("Intersection of Python and Java students:", intersection_students)

# Difference of two sets

difference_students = python_students.difference(java_students)
print("Difference of Python and Java students:", difference_students)

# Symmetric difference of two sets  

symmetric_difference_students = python_students.symmetric_difference(java_students)
print("Symmetric difference of Python and Java students:", symmetric_difference_students)


# .add, .remove, .discard

python_students.add("Ankit")
print("After adding Ankit:", python_students)

python_students.remove("Ankit")
print("After removing Ankit:", python_students)

python_students.discard("Ankit")
print("After discarding Ankit:", python_students)

python_students.discard("Ankit")
print("After discarding Ankit again:", python_students)

python_students.remove("Ankit")  # This will raise a KeyError since "Ankit" is not in the set


