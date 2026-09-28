even=0
odd=0
for i in range:
    num=int(input("enter any number"))
    for j in num:
        if int(j) % 2==0:
            even=even +1
        else:
            odd=odd +1
if even>odd:
    print("even occur more,total even number=",even)
elif even<odd:
    print("odd occur more,total odd occur")                 