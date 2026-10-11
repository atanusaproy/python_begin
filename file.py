import csv
import json

# def retrieve_csv(path):
#     with open(path, 'r', encoding="utf-8") as file:
#         reader = csv.reader(file)
#         return list(reader)

# rows = retrieve_csv("data.csv")
# print(rows)
# for row in rows:
#     print(row)


    


# def retrieve_JSON(path):
#     with open(path, 'r', encoding="utf-8") as file:
#         return file.read()

# row = retrieve_JSON('data.json')
# print(row)




def retrieve_csv(path):
    with open(path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)

rows = retrieve_csv("data.csv")

groupData = {}

for row in rows:
    age = int(row["age"])

    if age == 25 and age < 30:
        row["group"] = "A"
    elif age == 30 and age < 35:
        row["group"] = "B"
    elif age == 35 and age < 40:
        row["group"] = "C"
    else:
        row["group"] = "D"

for item in rows:
    group = item['group']

    if group not in groupData:
        groupData[group] = []

    groupData[group].append(item)

print(groupData)

