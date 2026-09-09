side1 = int(input("enter the side1 of triangle:"))
side2 = int(input("enter the side2 of triangle:"))
side3 = int(input("enter the side3 of triangle:"))

if side1+side2>=side3 or side2+side3>=side1 or side1+side3>=side2:
    print("it is a triangle")
else:
    print("it's not a triangle")