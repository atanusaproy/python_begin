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
fruits.remove("Bananas")
print(fruits)

