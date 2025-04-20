'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# 1. Count lowercase and uppercase
def count_lower_upper(s):
    d = {"lower": 0, "upper": 0}
    for ch in s:
        if ch.islower():
            d["lower"] += 1
        elif ch.isupper():
            d["upper"] += 1
    return d

print(count_lower_upper("PDEU Rocks at ICT Dept"))

# 2. compute n + nn + nnn + nnnn
def compute(n):
    n = str(n)
    return int(n) + int(n*2) + int(n*3) + int(n*4)

for i in range(4, 8):
    print(i, "->", compute(i))

# 3. Create 3D array
def create_array(x, y, z, val):
    return [[[val for _ in range(z)] for _ in range(y)] for _ in range(x)]

arr = create_array(2, 2, 2, 7)
print(arr)

# 4. Sum and average
def sum_avg(m1, m2, m3, m4, m5):
    total = m1 + m2 + m3 + m4 + m5
    avg = total / 5
    return total, avg

print(sum_avg(70, 80, 60, 90, 75))

# 5. Pangram
def ispangram(s):
    s = s.lower()
    return set("abcdefghijklmnopqrstuvwxyz") <= set(s)

print(ispangram("The quick brown fox jumps over the lazy dog"))

# 6. List of (x, x², x³)
def power_list(n):
    return [(x, x**2, x**3) for x in range(1, n+1)]

print(power_list(5))

# 7. Palindrome
def ispalindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

print(ispalindrome("A man a plan a canal Panama"))

# 8. Remove duplicates and sort
def convert(s):
    words = s.split()
    words = sorted(set(words))
    return " ".join(words)

print(convert("pdeu ict ict rocks pdeu rocks python"))

# 9. Count alphabets and digits
def count_alpha_digits(s):
    d = {"alpha": 0, "digit": 0}
    for ch in s:
        if ch.isalpha():
            d["alpha"] += 1
        elif ch.isdigit():
            d["digit"] += 1
    return d

print(count_alpha_digits("ICT2025PDEU42"))

# 10. Frequency of words
def frequency(s):
    s = s.lower().split()
    d = {}
    for word in s:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return dict(sorted(d.items()))

print(frequency("the quick brown fox jumps over the lazy dog the quick fox"))

# 11. List intersection
def create_list(l1, l2):
    return [x for x in l1 if x in l2]

print(create_list([1, 2, 3, 4], [3, 4, 5, 6]))


# Recursive Functions

# 1. Recursive Prime Factors
def prime_factors(n, i=2):
    if i > n:
        return
    if n % i == 0:
        print(i)
        return prime_factors(n // i, i)
    else:
        return prime_factors(n, i + 1)

prime_factors(180)

# 2. Binary equivalent
def binary(n):
    if n == 0:
        return ""
    else:
        return binary(n // 2) + str(n % 2)

print(binary(25))

# 3. Recursive vowel count
def count_vowels(s):
    if not s:
        return 0
    if s[0].lower() in "aeiou":
        return 1 + count_vowels(s[1:])
    else:
        return count_vowels(s[1:])

print(count_vowels("PDEU Rocks With Energy"))

# 4. Reverse list recursively
def reverse_list(l):
    if len(l) == 0:
        return []
    return [l[-1]] + reverse_list(l[:-1])

print(reverse_list([1, 2, 3, 4, 5]))

# 5. Recursive a^b
def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b - 1)

print(power(2, 5))

# 6. Replace negative with 0
def sanitize(lst, i=0):
    if i == len(lst):
        return lst
    if lst[i] < 0:
        lst[i] = 0
    return sanitize(lst, i + 1)

lst = [-2, 3, -5, 6, -1]
print(sanitize(lst))

# 7. Average of list recursively
def avg_recursive(lst, i=0, total=0):
    if i == len(lst):
        return total / len(lst)
    return avg_recursive(lst, i + 1, total + lst[i])

print(avg_recursive([10, 20, 30, 40, 50]))

# 8. Recursive string length
def str_len(s):
    if s == "":
        return 0
    return 1 + str_len(s[1:])

print(str_len("PDEU"))
