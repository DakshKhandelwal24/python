cost_price = int(input("enter the cost price :"))
selling_price = int(input("enter the selling price:"))
profit = selling_price - cost_price
loss = cost_price - selling_price
if  profit>loss:
    print("profit")
    print({f"profit of {profit}"})
    print(f"profit of {profit/cost_price*100}%")
elif loss>profit:
    print("loss")
    print(f"loss of {loss}")
    print(f"loss of {loss/cost_price*100}%")
else:
    print("invalid")

