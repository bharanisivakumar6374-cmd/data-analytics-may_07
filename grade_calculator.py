import sys

name = "Alice"

# If a number is passed as an argument, use it. Otherwise default to 60.
marks = int(sys.argv[1]) if len(sys.argv) > 1 else 60

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

print("Name:", name)
print("Marks:", marks)
print("Grade:", grade)
