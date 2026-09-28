num = int(input("Enter a number :"))
for i in range (1,num+1):
    for j in range (1,i*2) :
        if j % 15 == 0  :
            print("Z",end=" ")
        elif j % 3 == 0 :
            print("X",end=" ")
        elif j % 5 == 0 :
            print( "Y", end=" ")
        else :
            print(j,end=" ")
    print()
