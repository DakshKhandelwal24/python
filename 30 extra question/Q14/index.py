cost_price = int(input("enter the cost price :"))
selling_price = int(input("enter the selling price:"))

if cost_price>=selling_price:
    print("its a loss")
elif selling_price>=cost_price:
    print("its a profit")
elif selling_price==cost_price:
    print("no profit and no loss")
else:
    print("invalid")
