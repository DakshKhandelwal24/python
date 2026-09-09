marks=int(input("entre your marks"))
if marks<=100 and marks>=75:
    print("Distinction")
elif marks<75 and marks>=60:
    print("first class")
elif marks<60 and marks>50:
    print("second class")
elif marks<=49 and marks>35:
    print("pass")
else :
    print(("Fail"))    
    