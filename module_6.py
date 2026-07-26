# Module 6 List & Tuples

# Creating and accessing lists

# This way we can create a list.
numbers = [1, 2, 3, 4, 5, "Hello"]

print(numbers)
print(numbers[4]) # Accessing the first element of the list
print(numbers[-1]) # Accessing the last element of the list

numbers[5] = "World" # Changing the value of the last element of the list
print(numbers)


# List methods: .append() , .extend() , .insert() , .remove() , .pop() , .sort() , .reverse()

# Append method adds an element to the end of the list.

fruits = ["Apple", "Banana", "Cherry"]
new_fruit = "Mango"
fruits.append(new_fruit)
print(fruits)

# Extend method adds multiple elements to the end of the list.  

fruits = ["Apple", "Banana", "Cherry"]
new_fruits = ["Mango", "Banana", "Pineapple"]
fruits.extend(new_fruits)
print(fruits)

# Insert method adds an element at a specific index in the list.

numbers = [1,3,4,5,6]
numbers.insert(1, 2)
print(numbers)

# Remove method removes an element from the list.

fruits = ["Apple", "Banana", "Cherry"]
fruits.remove("Banana")
print(fruits)

# Pop method removes an element at a specific index in the list.

numbers = [1, 2, 3, 4, 5]
numbers.pop(1)
print(numbers)

# Sort method sorts the elements of the list in ascending order.

num = [4,3,6,2,1]
# num.sort(reverse=True) # Sorting in descending order
# print(num)

num1 = sorted(num) # Sorting in ascending order
num.sort() # Sorts the list in place
print("List sort")
print(num1)

# `Reverse` method reverses the elements of the list in place.
numbers = [100, 2, 3, 4, 5]
numbers.reverse()
print(numbers)


# List slicing

numbers = [1, 2, 3, 4, 5, 6]

# Positive indexing
# 1 2  3  4  5
# 0 1  2  3  4

# Negative indexing
# 1   2  3  4  5
# -5 -4 -3 -2 -1

# Start Index
# Stop Index
# Step Size

print(numbers[1:3]) # [2, 3]
print(numbers[1:]) # [2, 3, 4, 5]
print(numbers[:3]) # [1, 2, 3]
print(numbers[::2]) # [1, 3, 5]
print(numbers[::-1]) # [5, 4, 3, 2, 1]

# With step size
numbers = [1, 2, 3, 4, 5, 6]
after_slicing = numbers[1:6:2]
print(after_slicing) # [2, 4, 6]

 
def our_sum(*args):
    return sum(args)


# arr_list = [1, 2, 3, 4, 5, "Hello"]
# print(our_sum(*arr_list)) # Unpacking the list into the function arguments


# List comprehension
# List comprehension is a concise way to create lists in Python. It allows you to generate a new list by applying an expression to each item in an existing iterable (like a list or range) and optionally filtering items based on a condition. 

# New list creation using for loop(old way)

numbers = []

for i in range(1, 11):
    numbers.append(i)

print(numbers)

# Using list comprehension (new way)

numbers = [i for i in range(1, 11)]

print("List comprehension:", numbers)

# Example 1:

squares = [i**2 for i in range(1, 11)]
print("Squares:", squares)

#Example 2: (If condition)

even_numbers = [i for i in range(1, 11) if i % 2 == 0]
print("Even numbers:", even_numbers)

# Example 3: 
user_names = ["Alice", "Bob", "Charlie", "David"]
upper_case_names = [name.upper() for name in user_names]
print("Upper case names:", upper_case_names)

#### Nested list ####

numbers_list = [1 ,3 , 5, 7, 9]
nested_list = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
]

print("Nested list:", nested_list)
print(nested_list[1][0]) 



## Tuples
#tuples are similar to lists, but they are immutable, meaning their elements cannot be changed after creation. Tuples are defined using parentheses ().

# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)
print("First element of tuple:", my_tuple[0]) # Accessing the first element of the tuple
print(type(my_tuple)) # Checking the type of the tuple


fruits = "Apple", "Banana", "Cherry"
print("Fruits tuple:", fruits)

# Unpacking a tuple
fruits = ("Apple", "Banana", "Cherry")
apple, banana, cherry = fruits
print("Unpacked tuple:", apple, banana, cherry)

def get_user():
    return "John", 25, "New York"

name, age, city = get_user()
print("Name:", name)
print("Age:", age)
print("City:", city)

numbers = (1, 2, 3, 4, 5) # 1, [2,3,4], 5

first, *middle, last = numbers
print("First:", first)
print("Middle:", middle)
print("Last:", last)


# Named tuples
from collections import namedtuple

# before named tuples

person = ("John", 25, "New York") # this is a tuple
print("Person:", person)
print("Name:", person[0])
print("Age:", person[1])
print("City:", person[2])

# after named tuples

person = namedtuple("Person", ["name", "age", "city"])
person = person("John", 25, "New York")

print("Person:", person)
print("Name:", person.name)
print("Age:", person.age)
print("City:", person.city)



def get_person():
    user = namedtuple("User", ["name", "age", "city"])
    return user("sahinoor", 30, "Kolkata")

print("Person:", get_person())


# Iterators and generators
# Iterators are objects that can be iterated upon. They return one element at a time.
# It using iter() and next() functions.
numbers = [1, 2, 3, 4, 5] # this is a list
iterator = iter(numbers) # this is an iterator

print("Iterator:", iterator) # this will print the iterator object
print(next(iterator)) # this will print the first element of the list
print(next(iterator)) # this will print the second element of the list
print(next(iterator)) # this will print the third element of the list
print(next(iterator)) # this will print the fourth element of the list
print(next(iterator)) # this will print the fifth element of the list
print(next(iterator)) # this will raise a StopIteration error because there are no more elements to iterate through




