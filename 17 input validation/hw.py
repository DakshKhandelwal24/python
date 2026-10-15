# QUESTION 1

while True:
    marks = int(input("Enter marks (0-100): "))

    if 0 <= marks <= 100:
        break

print("Accepted marks:", marks)