'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# 1. Largest and smallest of two numbers
a = 10
b = 20
if a > b:
    print("largest:", a)
    print("smallest:", b)
else:
    print("largest:", b)
    print("smallest:", a)

# 2. Largest and smallest of three numbers
a = 10
b = 30
c = 20

if a > b and a > c:
    largest = a
elif b > c:
    largest = b
else:
    largest = c

if a < b and a < c:
    smallest = a
elif b < c:
    smallest = b
else:
    smallest = c

print("largest:", largest)
print("smallest:", smallest)

# 3. Odd or Even
num = 7
if num % 2 == 0:
    print("even")
else:
    print("odd")

# 4. Divisible by 10 or not
num = 50
if num % 10 == 0:
    print("divisible")
else:
    print("not divisible")

# 5. Age check (minor/major)
age = 17
print("minor" if age < 18 else "major")

# 6. Number of digits in a number
num = 12345
num_str = str(num)
print(len(num_str))

# 7. Leap year check
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("leap year")
else:
    print("not a leap year")

# 8. Valid triangle check (sum of angles = 180)
a = 60
b = 60
c = 60
if a + b + c == 180:
    print("valid")
else:
    print("invalid")

# 9. Absolute value
num = -25
if num < 0:
    print(-num)
else:
    print(num)

# 10. Area vs Perimeter of rectangle
l = 10
b = 5
area = l * b
perimeter = 2 * (l + b)
if area > perimeter:
    print("area greater")
else:
    print("perimeter greater or equal")

# 11. Check if 3 points lie on a straight line
x1, y1 = 0, 0
x2, y2 = 2, 2
x3, y3 = 4, 4
if (y2 - y1)*(x3 - x2) == (y3 - y2)*(x2 - x1):
    print("straight line")
else:
    print("not on line")

# 12. Point inside/on/outside circle
import math
x, y = 3, 4
center_x, center_y = 0, 0
radius = 5
distance = math.sqrt((x - center_x)**2 + (y - center_y)**2)
if distance < radius:
    print("inside")
elif distance == radius:
    print("on")
else:
    print("outside")

# 13. 0 to 19 to words using match-case
num = 17
match num:
    case 0: print("zero")
    case 1: print("one")
    case 2: print("two")
    case 3: print("three")
    case 4: print("four")
    case 5: print("five")
    case 6: print("six")
    case 7: print("seven")
    case 8: print("eight")
    case 9: print("nine")
    case 10: print("ten")
    case 11: print("eleven")
    case 12: print("twelve")
    case 13: print("thirteen")
    case 14: print("fourteen")
    case 15: print("fifteen")
    case 16: print("sixteen")
    case 17: print("seventeen")
    case 18: print("eighteen")
    case 19: print("nineteen")
    case _: print("out of range")

# 14. Marks, total, average, pass/fail, grade using if-else
m1 = 75
m2 = 65
m3 = 38
total = m1 + m2 + m3
average = total / 3
print("total:", total)
print("average:", average)

if m1 <= 39 or m2 <= 39 or m3 <= 39:
    print("fail")
else:
    print("pass")

if m1 == "Absent":
    print("NA")
elif m1 <= 39:
    print("F")
elif m1 <= 44:
    print("P")
elif m1 <= 49:
    print("C")
elif m1 <= 54:
    print("B")
elif m1 <= 59:
    print("B+")
elif m1 <= 69:
    print("A")
elif m1 <= 79:
    print("A+")
elif m1 <= 100:
    print("O")
else:
    print("Invalid")

if m2 == "Absent":
    print("NA")
elif m2 <= 39:
    print("F")
elif m2 <= 44:
    print("P")
elif m2 <= 49:
    print("C")
elif m2 <= 54:
    print("B")
elif m2 <= 59:
    print("B+")
elif m2 <= 69:
    print("A")
elif m2 <= 79:
    print("A+")
elif m2 <= 100:
    print("O")
else:
    print("Invalid")

if m3 == "Absent":
    print("NA")
elif m3 <= 39:
    print("F")
elif m3 <= 44:
    print("P")
elif m3 <= 49:
    print("C")
elif m3 <= 54:
    print("B")
elif m3 <= 59:
    print("B+")
elif m3 <= 69:
    print("A")
elif m3 <= 79:
    print("A+")
elif m3 <= 100:
    print("O")
else:
    print("Invalid")