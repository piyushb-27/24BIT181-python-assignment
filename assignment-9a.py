'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# 1. Three functions in a list
def fun():
    print("fun called")
def disp():
    print("disp called")
def msg():
    print("msg called")

lst = [fun, disp, msg]
for f in lst:
    f()

# 2. Map + lambda with two lists
l1 = [1, 2, 3, 4, 5, 6]
l2 = [6, 5, 4, 3, 2, 1]
res = list(map(lambda x, y: x + y, l1, l2))
print(res)

# 3. 10 random numbers between -15 and 15, get their squares
import random
nums = random.sample(range(-15, 16), 10)
squares = list(map(lambda x: x**2, nums))
print(nums)
print(squares)

# 4. Print palindromes only
lst = ['madam', 'Python', 'malayalam', 12321]
for item in lst:
    s = str(item)
    if s == s[::-1]:
        print(s)

# 5. Filter names with length > 8
names = ["Ravi", "Shantanu", "Bhargav", "Madhusudan", "Priyanka", "Anand", "Udaybhanu"]
long_names = list(filter(lambda x: len(x) > 8, names))
print(long_names)
