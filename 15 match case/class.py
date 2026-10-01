# SYNTAX FOR MATCH CASE

# match value :
#     case pattern 1
#         Code 
#     case pattern 2
#         code 
#     case pattern 3
#         code 
#     case _:
#         default code 
5

num1=int(input("enter a number"))
num2 =int(input("enter a second number"))
print("""type of operation
1 - Addition
2 - Substraction
3 - multiplication
4 - division
5 - remainder
6 - exponiential """)

choice=int(input("enter what operation you want from the above list"))
match choice:
    case 1:
        print("addition is",num1+num2)
    case 2:
        print("subtraction is",num1-num2)
    case 3:
        print("multiplication of number is",num1*num2)
    case 4:
        print("division of number is",num1/num2)
    case 5 :
        print("remainder of number is",num1%num2)
    case 6:
        print("expoiential is",num1**num2)
    case _:
        print("enter a valid input")                        