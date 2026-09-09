year = int(input("enter the year number :"))

if year%400==0:
    print("it's a leap year")
elif year%4==0 and year%100!=0:
    print("it's a leap year")
else:
    print("it is not a leap year")

