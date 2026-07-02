
# String position Indexing
name = "Atanu"
print(name[0])
print(name[1])

#Negative Indexing
print(name[-1])
print(name[-2])

print(name[4])

# String Slicing
name = "Atanu"
print(name[0:3]) # Ata
print(name[1:4]) # tan
print(name[2:5]) # anu

print(name[:3]) # Ata
print(name[3:]) # nu
print(name[:-1]) 

# concatenation
first_name = "Atanu"
last_name = "Roy"

full_name = first_name + " " + last_name
print(full_name)

# F-strings
name = "Atanu"
age = 25
email = "atanu@gmail.com"

user_info = f"Name: {name}, Age: {age}, Email: {email}"
print(user_info)
