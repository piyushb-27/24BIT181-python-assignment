'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''


# 1. Print all alphabets in upper case and in lower case
for i in range(65, 91):
    print(chr(i), end=' ')
print()
for i in range(97, 123):
    print(chr(i), end=' ')
print()

# 2. Multiplication table of a given number
num = int(input("Enter number for multiplication table: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# 3. Count alphabets and digits in string
s = input("Enter a string: ")
alpha = 0
digit = 0
for ch in s:
    if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
        alpha += 1
    elif '0' <= ch <= '9':
        digit += 1
print("alphabets:", alpha)
print("digits:", digit)

# 4. Check prime, perfect, Armstrong, palindrome, automorphic
n = int(input("Enter a number: "))

# Prime
prime = True
if n < 2:
    prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break
if prime:
    print("prime")
else:
    print("not prime")

# Perfect number
sum_div = 0
for i in range(1, n):
    if n % i == 0:
        sum_div += i
if sum_div == n:
    print("perfect")
else:
    print("not perfect")

# Armstrong
temp = n
arm = 0
while temp > 0:
    d = temp % 10
    arm += d ** 3
    temp //= 10
if arm == n:
    print("armstrong")
else:
    print("not armstrong")

# Palindrome
original = n
rev = 0
while n > 0:
    rev = rev * 10 + (n % 10)
    n //= 10
if original == rev:
    print("palindrome")
else:
    print("not palindrome")

# Automorphic
num = original
square = num * num
if str(square).endswith(str(num)):
    print("automorphic")
else:
    print("not automorphic")

# 5. Pythagorean Triplets with sides <= 30
for a in range(1, 31):
    for b in range(a, 31):
        for c in range(b, 31):
            if a*a + b*b == c*c:
                print(a, b, c)

# 6. 24 Hours with suffix
for h in range(0, 24):
    if h == 0:
        print("12 Midnight")
    elif h < 12:
        print(h, "AM")
    elif h == 12:
        print("12 Noon")
    else:
        print(h - 12, "PM")

# 7. nCr and nPr
n = int(input("Enter n: "))
r = int(input("Enter r: "))

nf = 1
for i in range(1, n + 1):
    nf *= i

rf = 1
for i in range(1, r + 1):
    rf *= i

nrf = 1
for i in range(1, n - r + 1):
    nrf *= i

nCr = nf // (rf * nrf)
nPr = nf // nrf

print("nCr:", nCr)
print("nPr:", nPr)

# 8. Factorial of a given number
num = int(input("Enter number to find factorial: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("factorial:", fact)

# 9. N natural numbers in reverse
N = int(input("Enter N: "))
for i in range(N, 0, -1):
    print(i, end=' ')
print()

# 10. Fibonacci series
N = int(input("Enter how many Fibonacci numbers: "))
a = 0
b = 1
print(a, end=' ')
if N > 1:
    print(b, end=' ')
for i in range(2, N):
    c = a + b
    print(c, end=' ')
    a = b
    b = c
print()

# 11. sin(x) using series
x_deg = float(input("Enter angle in degrees: "))
x = x_deg * 3.14159 / 180

terms = 10
sinx = 0
sign = 1
for i in range(1, 2 * terms, 2):
    fact = 1
    for j in range(1, i + 1):
        fact *= j
    sinx += sign * (x ** i) / fact
    sign *= -1
print("sin(x):", sinx)
