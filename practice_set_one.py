# # 1
# a = [10, 20, 30]
# a.append(40)
# print(a)

# # 2
# a = [1, 2]
# a.append([3, 4])
# print(a)

# # 3
# a = [1, 2]
# a.extend([3, 4])
# print(a)

# # 4
# a = [10, 20, 30, 40, 50]
# print(a[1:4])

# # 5
# a = [1, 2, 3, 4, 5]
# print(a[::-1])
# print(tuple(reversed(a)))

# # 6
# a = [10, 20, 30]
# b = a

# a.append(40)

# print(a)
# print(b)

# # 7
# a = [10, 20, 30]
# b = a.copy()

# a.append(40)

# print(a)
# print(b)

# # 8
# a = [1, 2, 3, 4, 5]

# a.remove(3)
# print(a)

# print(a.pop())
# print(a)

# 9
# a = [5, 2, 8, 1, 3]

# b = sorted(a)

# print(a)
# print(b)

# 10
# a = [5, 2, 8, 1, 3]

# a.sort()

# print(a)

# 11
# a = [1, 2, 3, 4, 5]

# result = [x * 2 for x in a if x % 2 == 0]

# print(result)

# # 50
# a = [1, 2, 3]

# b = (1, 2, 3)

# c = {1, 2, 3}

# d = {
# 1: "one",
# 2: "two",
# 3: "three"
# }

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))

# print(2 in a)
# print(2 in b)
# print(2 in c)
# print(2 in d)

# print(a == b)
# print(set(a) == c)
# print(list(d.keys()) == a)

# # 49
# a = [1, 2, 2, 3, 1, 4, 3]
# b = list(dict.fromkeys(a))
# print(b)

# # 48
# a = [1, 2, 2, 3, 3, 4]
# b = list(set(a))
# print(b)

# 47
a = [[1, 2], [3, 4]]
b = a.copy()
a[0].append(5)

print(a)
print(b)
