'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# 1. Count how many vowels are there in a string. Accept the string from the user.
s = input("Enter a string: ")
count = 0
for ch in s:
    if ch in "aeiouAEIOU":
        count = count + 1
print("vowel count:", count)

# 2. Own functions to convert to lower/upper/toggle case
s = input("Enter a string for case conversion: ")

# Convert to uppercase
upper_str = ""
for ch in s:
    if 'a' <= ch <= 'z':
        upper_str += chr(ord(ch) - 32)
    else:
        upper_str += ch
print("uppercase:", upper_str)

# Convert to lowercase
lower_str = ""
for ch in s:
    if 'A' <= ch <= 'Z':
        lower_str += chr(ord(ch) + 32)
    else:
        lower_str += ch
print("lowercase:", lower_str)

# Toggle case
toggle_str = ""
for ch in s:
    if 'A' <= ch <= 'Z':
        toggle_str += chr(ord(ch) + 32)
    elif 'a' <= ch <= 'z':
        toggle_str += chr(ord(ch) - 32)
    else:
        toggle_str += ch
print("togglecase:", toggle_str)

# 3. Accept two strings. Check whether one string is there in another string.
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if s1 in s2:
    print("present")
elif s2 in s1:
    print("present")
else:
    print("not present")

# 4. Remove one string from another if present
one = input("Enter the main string: ")
remove = input("Enter the string to remove: ")

final = ""
i = 0
while i < len(one):
    if one[i:i+len(remove)] == remove:
        i += len(remove)
    else:
        final += one[i]
        i += 1
print("final string:", final)
