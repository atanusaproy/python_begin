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

# # 47
# import copy
# a = [[1, 2], [3, 4]]
# # b = a.copy()
# b = copy.deepcopy(a)
# a[0].append(5)

# print(a)
# print(b)

# # 46
# a = [1, 2, 3]
# b = a
# c = a.copy()

# a.append(4)

# print(a)
# print(b)
# print(c)

# # 45
# d = {
# "a": 1,
# "b": 2,
# "c": 1,
# "d": 3
# }

# result = {}

# for k, v in d.items():
#  result.setdefault(k, []).append(v)

#  print(result)

# # 44
# numbers = [1, 2, 6, 4]

# d = {x: x * x for x in numbers}

# print(d)

# # 43
# d = {}

# d.setdefault("skills", []).append("Python")
# d.setdefault("skills", []).append("SQL")

# print(d)

# # 42
# a = {"x": 1, "y": 2}
# b = {"y": 20, "z": 3}

# c = a | b

# print(c)

# # 41
# a = {"x": 1}
# b = {"y": 2}

# c = {**a, **b} 
# # unpacking operator

# print(c)

# # 40
# d = {
# "a": 10,
# "b": 20
# }

# for key, value in d.items():
#  print(key, value)

# # 39
# d = {
# "a": 10,
# "b": 20
# }

# print(d.keys())
# print(d.values())
# print(d.items())

# # 38
# d = {
# "a": 10,
# "b": 20
# }

# d["c"] = 30
# d["a"] = 100

# print(d)

# # 39
# d = {
# "name": "Atanu"
# }

# print(d.get("age"))
# print(d.get("age", 0))

# 38
d = {
"name": "Atanu",
"age": 35
}

print(d["name"])
print(d["age"])



