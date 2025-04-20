'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# 1. Create 3 dictionaries and concatenate into a 4th
d1 = {1: 'A', 2: 'B'}
d2 = {3: 'C', 4: 'D'}
d3 = {5: 'E'}
d4 = {**d1, **d2, **d3}
print(d4)

# 2. Check if a dictionary is empty
d = {}
if not d:
    print("empty")
else:
    print("not empty")

# 3. Dept-wise min and max salary
data = {
    101: {1: 25000, 2: 30000},
    102: {3: 40000, 4: 28000},
    103: {5: 35000, 6: 45000}
}

for dept in data:
    sals = list(data[dept].values())
    print("dept:", dept)
    print("min:", min(sals))
    print("max:", max(sals))

# 4. Frequency of characters in string
s = input("Enter a string: ")
freq = {}
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print(freq)

# 5. Total bill from 2 dictionaries
prices = {"rice": 60, "wheat": 40, "milk": 25}
qty = {"rice": 2, "wheat": 3, "milk": 5}
total = 0
for item in prices:
    if item in qty:
        total += prices[item] * qty[item]
print("total bill:", total)
