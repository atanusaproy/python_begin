# for loop in python
fruits = ["apple", "banana", "cherry", "mango", "orange", "pineapple", "strawberry", "watermelon"]

for fruit in fruits:
    print(fruit)

# I want to print 0 to 10 using for loop in javascript
# for(let i=0; i<10; i++){
#     console.log(fruits[i]);
# }


# The same example in python 
    for i in range(len(fruits)):
        print(i)


# Loop control statements
# break statement

for i in range(10):
    if (i == 5):
        break
    print(f"Number is {i} for break statement")

# continue statement
for i in range(1,6):
    if (i == 3):
        continue
    print(f"Number is {i} for continue statement")


# pass statement
for i in range(1,6):
    print(f"Number is {i} for pass statement")
    pass

age = 18
if age >= 18:
    pass
else:
    print("You are not eligible to vote")


# else in loop
for i in range(1,6):
    print(f"Number is {i} for else in loop")
else:
    print("Loop is finished")


for i in range(1,6):
    print(f"Number is {i} for else in loop")
    if (i == 3):
        break
else:
    print("Loop is finished but else is not executed")