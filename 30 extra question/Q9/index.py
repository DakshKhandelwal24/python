age = int(input("enter the age :"))

if age<0 or age>120:
    print("unrealistic age")
elif age<18:
    print("cannot vote")
elif age>18:
    print("can vote")
