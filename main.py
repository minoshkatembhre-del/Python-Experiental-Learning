# python-name = input("Enter student name: ")

m1 = int(input("Enter marks of Subject 1: "))
m2 = int(input("Enter marks of Subject 2: "))
m3 = int(input("Enter marks of Subject 3: "))

total = m1 + m2 + m3
percentage = (total / 300) * 100

if percentage >= 40:
    result = "PASS"
else:
    result = "FAIL"

print("\nStudent Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Result:", result)
