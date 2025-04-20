'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# 1. Count number of boys and girls in the list
# Boys' names are stored as tuples

names = ["Anjali", "Priya", ("Rohan",), "Meena", ("Amit",), "Neha", ("Raj",), "Sonal"]

boys = 0
girls = 0

for ele in names:
    if isinstance(ele, tuple):
        boys += 1
    else:
        girls += 1

print("Number of boys:", boys)
print("Number of girls:", girls)


# 2. Split a list of student data into three separate lists

students = [
    (101, "Ravi", 18),
    (102, "Asha", 19),
    (103, "Kunal", 18),
    (104, "Seema", 20)
]

roll_nos = []
names = []
ages = []

for student in students:
    roll_nos.append(student[0])
    names.append(student[1])
    ages.append(student[2])

print("Roll Numbers:", roll_nos)
print("Names:", names)
print("Ages:", ages)


# 3. Find number of days between two date tuples

from datetime import date

date1 = (12, 4, 2023)  # 12 April 2023
date2 = (20, 4, 2025)  # 20 April 2025

d1 = date(date1[2], date1[1], date1[0])  # (year, month, day)
d2 = date(date2[2], date2[1], date2[0])

difference = d2 - d1
print("Number of days between two dates:", difference.days)


# 4. Sort list of food items by price in descending order

food_items = [
    ("Samosa", 20),
    ("Pizza", 150),
    ("Burger", 90),
    ("Vada Pav", 15),
    ("Dosa", 50)
]

sorted_items = sorted(food_items, key=lambda x: x[1], reverse=True)

print("Sorted food items by price (descending):")
for item in sorted_items:
    print(item)


# 5. Remove empty tuples from a list

tuples_list = [(), (1, 2), (), (3, 4, 5), (), ("a", "b")]

filtered_list = []

for tup in tuples_list:
    if tup != ():
        filtered_list.append(tup)

print("List after removing empty tuples:", filtered_list)


# 6. Modify an element of a tuple

original_tuple = (10, 20, 30)

# Convert to list
temp_list = list(original_tuple)

# Modify the second element
temp_list[1] = 99

# Convert back to tuple
modified_tuple = tuple(temp_list)

print("Modified tuple:", modified_tuple)


# 7. Delete an element of a tuple

original_tuple = (5, 10, 15, 20)

# Convert to list
temp_list = list(original_tuple)

# Delete the 3rd element (index 2)
del temp_list[2]

# Convert back to tuple
new_tuple = tuple(temp_list)

print("Tuple after deleting an element:", new_tuple)
