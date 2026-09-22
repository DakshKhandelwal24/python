fail = 0
pass_count = 0 
excellent = 0
good = 0

for i in range(10):
    marks = int(input("Enter marks: "))

    if marks < 35:
        print("Fail")
        fail =fail+ 1
    elif marks <= 49:
        print("Pass")
        pass_count = pass_count +1
    elif marks <= 74:
        print("Good")
        good = good +1

    else:
        print("Excellent")
        excellent = excellent +1

print("Number of students=10")
print("Fail:", fail)
print("Pass:", pass_count)
print("Good:", good)
print("Excellent:", excellent)