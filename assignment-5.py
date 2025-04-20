'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

import random
from collections import deque

# 1. Create list of 5 odd + 4 even integers using random
odds = [random.randrange(1, 100, 2) for _ in range(5)]
print("Odd integers:", odds)

evens = [random.randrange(0, 100, 2) for _ in range(4)]
print("Even integers:", evens)

odds[2] = evens
print("Replaced 3rd odd element with even list:", odds)

# Flattening
flat = []
for item in odds:
    if isinstance(item, list):
        flat.extend(item)
    else:
        flat.append(item)

print("Flattened list:", flat)

flat.sort()
print("Sorted list:", flat)

# 2. Generate 20 random integers, find all positions of a user-input number
nums = [random.randint(1, 10) for _ in range(20)]
print("Generated list:", nums)

target = int(input("Enter number to find positions: "))
positions = []

for idx, val in enumerate(nums):
    if val == target:
        positions.append(idx)

print("Positions:", positions)

# 3. Generate 50 random numbers in range 1-30 and remove duplicates
numbers = [random.randint(1, 30) for _ in range(50)]
print("Original list:", numbers)
unique = list(set(numbers))
print("After removing duplicates:", unique)

# 4. 30 random numbers split into positive and negative lists
mixed = [random.randint(-50, 50) for _ in range(30)]
positives = []
negatives = []

for n in mixed:
    if n >= 0:
        positives.append(n)
    else:
        negatives.append(n)

print("Original:", mixed)
print("Positives:", positives)
print("Negatives:", negatives)

# 5. Convert 5 strings to uppercase
strs = ["pdeu", "hello", "python", "rocks", "lists"]
for i in range(len(strs)):
    strs[i] = strs[i].upper()
print("Uppercase strings:", strs)

# 6. Convert list of Fahrenheit temps to Celsius
f = [32, 68, 86, 104, 122]
c = []
for temp in f:
    cel = (temp - 32) * 5 / 9
    c.append(cel)
print("Fahrenheit:", f)
print("Celsius:", c)

# 7. Stack - Menu-driven
stack = []

while True:
    print("\nStack Menu\n1. Push\n2. Pop\n3. Display\n4. Exit")
    choice = input("Enter choice: ")
    if choice == '1':
        val = input("Enter value to push: ")
        stack.append(val)
    elif choice == '2':
        if stack:
            print("Popped:", stack.pop())
        else:
            print("Stack is empty.")
    elif choice == '3':
        print("Stack contents:", stack)
    elif choice == '4':
        break
    else:
        print("Invalid")

# 8. Queue - Menu-driven
queue = deque()

while True:
    print("\nQueue Menu\n1. Insert\n2. Delete\n3. Display\n4. Exit")
    choice = input("Enter choice: ")
    if choice == '1':
        val = input("Enter value to insert: ")
        queue.append(val)
    elif choice == '2':
        if queue:
            print("Deleted:", queue.popleft())
        else:
            print("Queue is empty.")
    elif choice == '3':
        print("Queue contents:", list(queue))
    elif choice == '4':
        break
    else:
        print("Invalid")

# 9. Elements from list1 not in list2
list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [2, 4, 6]
list3 = [x for x in list1 if x not in list2]
print("List1:", list1)
print("List2:", list2)
print("List3 (only in List1):", list3)
