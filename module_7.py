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

# age delete from dictionary
del user["age"]  # Deleting the "age" key-value pair from the dictionary

print(user)