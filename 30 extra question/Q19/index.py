number = int(input("enter a number :"))

if number<0:
    print("Negative")
elif number>=0 and number<=10:
    print("number is between 0 and 10")
elif number>=11 and number<=50:
    print("number is between 11 and 50")
elif number>=51 and number<=100:
    print("number is between 51 and 100")
elif number>100:
    print("number is above 100")
else:
    print("please enter a number again")
