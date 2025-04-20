'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# 1. Create a CSV file for MS-Excel
with open("students.csv", "w") as f:
    f.write("RollNo,Name,Sub1,Sub2,Sub3\n")
    f.write("1,Piyush,85,90,88\n")
    f.write("2,Aryan,78,82,80\n")
    f.write("3,Nidhi,92,87,89\n")

# 2. Read CSV, convert to dict and display with total
d = {}
with open("students.csv", "r") as f:
    lines = f.readlines()[1:]
    for line in lines:
        parts = line.strip().split(",")
        roll = parts[0]
        name = parts[1]
        marks = list(map(int, parts[2:]))
        total = sum(marks)
        d[roll] = {"name": name, "marks": marks, "total": total}
print(d)

# 3. Create a vCard
name = input("Enter name: ")
phone = input("Enter phone: ")
email = input("Enter email: ")

with open("contact.vcf", "w") as f:
    f.write("BEGIN:VCARD\n")
    f.write("VERSION:3.0\n")
    f.write("FN:" + name + "\n")
    f.write("TEL:" + phone + "\n")
    f.write("EMAIL:" + email + "\n")
    f.write("END:VCARD\n")

# 4. Create subdir and copy file into it
import os, shutil

if not os.path.exists("newdir"):
    os.mkdir("newdir")

if not os.path.exists("sourcedir"):
    os.mkdir("sourcedir")

with open("sourcedir/sample.txt", "w") as f:
    f.write("Hello from PDEU!")

shutil.copy("sourcedir/sample.txt", "newdir/sample.txt")

# 5. Copy file & convert lowercase to uppercase
with open("source.txt", "w") as f:
    f.write("Pdeu\n")

with open("source.txt", "r") as f1, open("upper.txt", "w") as f2:
    for line in f1:
        f2.write(line.upper())

# 6. Merge lines alternatively
with open("file1.txt", "w") as f:
    f.write("Line1-A\nLine2-A\nLine3-A\n")
with open("file2.txt", "w") as f:
    f.write("Line1-B\nLine2-B\n")

f1 = open("file1.txt", "r")
f2 = open("file2.txt", "r")
f3 = open("merged.txt", "w")

lines1 = f1.readlines()
lines2 = f2.readlines()

i = 0
while i < len(lines1) or i < len(lines2):
    if i < len(lines1):
        f3.write(lines1[i])
    if i < len(lines2):
        f3.write(lines2[i])
    i += 1

f1.close()
f2.close()
f3.close()

# 7. Serialize/Deserialize Employee object
import json

emp = {
    "empcode": "E101",
    "empname": "Piyush",
    "doj": "2023-08-01",
    "salary": 65000
}

with open("emp.json", "w") as f:
    json.dump(emp, f)

with open("emp.json", "r") as f:
    newemp = json.load(f)

print(newemp)

# 8. Delete a/the/an from text file
with open("input.txt", "w") as f:
    f.write("This is a test of the text. An apple a day keeps the doctor away.")

with open("input.txt", "r") as f1, open("output.txt", "w") as f2:
    text = f1.read()
    for word in [" a ", " an ", " the "]:
        text = text.replace(word, " ")
    f2.write(text)
