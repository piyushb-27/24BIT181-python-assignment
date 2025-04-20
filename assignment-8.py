'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

import random

# 1. Convert list words to uppercase and store in set
words = ["hello", "world", "pdeu", "energy", "university"]
upper_set = {w.upper() for w in words}
print(upper_set)

# 2. 10 random numbers in range 15–45, count <30, delete >35
nums = set()
while len(nums) < 10:
    nums.add(random.randint(15, 45))
print(nums)

count = 0
for n in nums:
    if n < 30:
        count += 1
print("count <", count)

to_remove = {n for n in nums if n > 35}
nums -= to_remove
print(nums)

# 3. Create empty set, add 5 names, modify 1, delete 2
names = set()
names.add("Ravi")
names.add("Amit")
names.add("Rohit")
names.add("Kiran")
names.add("Priya")

names.remove("Ravi")
names.add("Ravindra")

names.discard("Kiran")
names.discard("Amit")

print(names)

# 4. Split names into sets A and B
s = {"Amit", "Anil", "Bhavesh", "Bhavin", "Ajay", "Bharat"}
a_set = {name for name in s if name.startswith("A")}
b_set = {name for name in s if name.startswith("B")}
print(a_set)
print(b_set)
