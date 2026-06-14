import math
#Arithmetic operators: + , - , * , / , // , % , **

#1 - Addition Operator
a = 10
b = 20
result = a + b
print("result of a + b is ", result)

#2 - Subtraction Operator
a = 10
b = 20
result = a - b
print("result of a - b is ", result)

#3 Multification Operator
a = 10
b = 20
result = a * b
print("result of a * b is ", result)

#4 Division Operator
a = 10
b = 3
result = a / b
print("result of a / b is ", result)

#5 Floor Division Operator
a = 10
b = 3
result = a // b
print("result of a // b is ", result)

#6 Modulus Operator
a = 10
b = 3
result = a % b
print("result of a % b is ", result)

#7 Exponentiation Operator
a = 2
b = 3
result = a ** b

print("result of a ** b is ", result) 


#We have 114 users, each page we have to show 11 users.
# how many pages will be there?

total_users = 114
per_page_users = 11

# Page Number calculation
pages = total_users / per_page_users
print(pages)

# Total Pages (rounded up)
total_pages = math.ceil(total_users / per_page_users)
print(total_pages)



