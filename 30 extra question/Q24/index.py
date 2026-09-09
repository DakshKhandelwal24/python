amount=int(input("entre the amount"))
if amount<500 :
    print("no discount sorry you have to pay $",amount)
elif amount>500 and amount<999:
    print("you got discount of 5 % ")
    print(amount*0.05)
    print(amount-amount*0.05)   
elif amount>1000 and amount<1999:
    print("you got discount of 10 % ")
    print(amount*0.1)
    print(amount-amount*0.1)   
elif amount>2000 and amount<4999:
    print("you got discount of 15 % ")
    print(amount*0.15)
    print(amount-amount*0.15)   
elif amount>5000 :
    print("you got discount of 20 % ")
    print(amount*0.2)
    print(amount-amount*0.2)   
else :
    print("please entre valid data")
    
