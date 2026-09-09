name1 = input("Enter Person 1 name: ")
age1 = int(input("Enter Person 1 age: "))

name2 = input("Enter Person 2 name: ")
age2 = int(input("Enter Person 2 age: "))

name3 = input("Enter Person 3 name: ")
age3 = int(input("Enter Person 3 age: "))

if age1 == age2 == age3:
    print("All three people are the same age")

elif age1 == age2:
    if age1 < age3:
        print(name1, "and", name2, "are the youngest")
    else:
        print(name3, "is the youngest")

elif age1 == age3:
    if age1 < age2:
        print(name1, "and", name3, "are the youngest")
    else:
        print(name2, "is the youngest")

elif age2 == age3:
    if age2 < age1:
        print(name2, "and", name3, "are the youngest")
    else:
        print(name1, "is the youngest")

else:
    if age1 < age2 and age1 < age3:
        print(name1, "is the youngest")
    elif age2 < age1 and age2 < age3:
        print(name2, "is the youngest")
    else:
        print(name3, "is the youngest")