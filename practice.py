# def factorial(num):
#     fact=1
#     for y in range(1, num+1):
#         fact = fact * y
#     print(fact)

# factorial(5)

from collections import namedtuple

user = namedtuple("User", ["name", "age", "city"])
user = user("Atanu", 30, "Kolkata")
print(user)

#  iterator and generators

# def my_gen():
#     yield 1
#     yield 2
#     yield 3

# for value in my_gen():
#     print(value)

# iterator  StopIteration call

# my_gen = my_gen()
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))


# generator expression

# numbers = [1, 2, 3, 4, 5]
# generator = (x for x in numbers)
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))


