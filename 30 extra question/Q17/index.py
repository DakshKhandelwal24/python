operation=int(input("entre number between 1 to 4"))
if operation == "1":
    print("addition")
elif operation =="2":
    print("subtraction")
elif operation == "3":
    print("multiplication")
else :
    print("dividion")
number1 = int(input("entre first number"))
number2 = int(input("entre anouther number"))
if operation ==1 and number1 and number2:
    print(number1 + number2)

if operation ==2 and number1 and number2:
    print(number1 - number2)

if operation ==3 and number1 and number2:
    print(number1 * number2)
elif operation ==4 and number1 and number2:
    print(number1 / number2)

