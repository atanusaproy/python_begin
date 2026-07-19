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


arr_list = [1, 2, 3, 4, 5, "Hello"]
print(our_sum(*arr_list)) # Unpacking the list into the function arguments