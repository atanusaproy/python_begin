# if , elif , else — conditional branching

age = 25
if age < 18:
    print("You are a minor.")
elif age == 18:
    print("Congratulations on becoming an adult!")
else:
    print("You are an adult.")


number = 50

if number > 90:
    print("Grade is A+")
elif number > 80:
    print("Grade is A")
else:
    print("Grade is B or below")    


# Nested statements
if age >= 18:
    if age >= 65:
        print("You are a senior citizen.")
    else:
        print("You are an adult.")
else:
    print("You are a minor.")

# While loop
#1st example
count = 0
while count <= 5:
    print(f"Count is: {count}")
    count += 1

#2nd example
count = 5
while count >= 0:
    print(f"Count is: {count}")
    count -= 1

# For loop
#1st example
users = ["Alice", "Bob", "Charlie"]
for user in users:
    print(f"Hello, {user}!")


for user in users:
    if user == "Bob":
        print(f"Hello, {user}!")
        break
    else:
        print(f"Not greeting {user}.")
        

for user in users:
    if user == "Bob":
        print(f"Hello, {user}!")
        continue
    else:
        print(f"Not greeting {user}.")