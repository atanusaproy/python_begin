# List
my_numbers = [10, 20, 30, 40, 50] 
# positive indexing
# => [0, 1, 2, 3, 4]

# negative indexing
# => [-5, -4, -3, -2, -1]
print("Previous list:", my_numbers)
my_numbers[1] = 200
print("Updated list:", my_numbers)

# If we want to want to length of the list we can use len() function
print("Length of the list:", len(my_numbers))


# Language list
my_languages = ["Python", "Java", "C++", "JavaScript"]
my_languages_lower = [each_lang.lower() for each_lang in my_languages]

user_input = "javag"

#print("java" in my_languages)  # Output: True
if(user_input.lower() not in my_languages_lower):
    my_languages.append(user_input)


print("Updated list of languages:", my_languages)



# Extending a list
my_new_languages = ["Go", "Rust", "Kotlin"]

if(len(my_new_languages) > 1):
    my_languages.extend(my_new_languages)

print("Extended list of languages:", my_languages)

# Inset to the list
my_languages.insert(2, "C#")

print("List after inserting C# at index 2:", my_languages)

# Remove from the list
# try:
#     my_languages.remove("Java")
# except ValueError:
#     print("Java is not in the list.")

if "Java" in my_languages:
    my_languages.remove("Java")

print("List after removing Java:", my_languages)

# Pop from the list
print("List before popping at index 2:", my_languages)
my_languages.pop(2)

print("List after popping at index 2:", my_languages)


my_languages_list2 = ["Ruby", "PHP", "Swift"]
my_languages_list_tuple = tuple(my_languages_list2)

print("List:", my_languages_list2)
print("Tuple:", my_languages_list_tuple)

# Tiuple to list
my_languages_list3 = list(my_languages_list_tuple)
print("List:", my_languages_list3)



new_list = [
    [1, 2, 3, 4],
    [4, 5, 6, 7],
    [7, 8, 9]
]

new_list_tuple = tuple(new_list)
first_element = new_list_tuple[0]
first_element.append(100)

print("Nested list:", new_list_tuple)



new_tupple = ([1, 2, 3], [4, 5, 6], [7, 8, 9])
first_element = new_tupple[0]
first_element.append(100)

print("Nested tupple:", new_tupple)

new_list_tup = ([1, 2, 3], [4, 5, 6], [7, 8, 9], (10, 11, 12))




