total1 = total2 = total3 = total4 =  0
count1 = count2 = count3 = count4 = 0
for i in range (1,9) :
    prices = input(f"Enter price of product : {i}:")
    if int(prices) >= 5000 :
        count1 += 1
        total1 = total1 + int(prices) 
        print("Luxury")
    elif 2000 <= int(prices) <= 4999 :
        count2 += 1
        total2 = total2 + int(prices)
        print("Premium")
    elif 500 <= int((prices)) <= 1999 :
        count3 += 1
        total3 = total3 + int(prices)
        print("Regular")
    else :
        count4 += 1
        total4 = total4 + int(prices)
        print("Budget")
print(f"Total amount : {(total1 + total2 + total3 + total4)}")
print(f"Products in Luxury : {count1}")
print(f"Products in Premium : {count2}")
print(f"Products in Regular : {count3}")
print(f"Products in Budget : {count4}")
print(f"Average Product Price : {(total1 + total2 + total3 + total4) / 4}")