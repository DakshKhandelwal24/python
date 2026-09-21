# # num=int(input("entre input in integer"))
# for num in range(1,11):
# #         print(18*num)
# name=input("entre a string").strip().lower()
# lenght=len(name)
# sum=""
# for number in range (lenght-1,-1,-1):
#     sum=sum+name[number]
# print(sum)


# if name==sum:
#         print("string is palindrome")
# else :
# #         print("string is not palindrome")    
# for i in range(3):
#     for j in range(2):
# #         print(i, j)
# for i in range(4):
#     for j in range(4):
#         print("*", end="")
# #     print("")    
# for k in range(4):
#     print("*"*4)
# for i in range(4,0,-1):
#     print("*"*i)
# for i in range(1,6):

#     for j in range(i , 6-i):
#         print(" ",end="")

#     for k in range( 1 , i+1):
#         print("*",end="")
#     print("") 
# n=7
# for i in range(1,n+1,2):
#     print(" " * ( n- i) + "* " * i)
# total=0
# passed=True
# grade=""
# for i in range(5):
#     marks=int(input("enter marks"))
#     total=total+marks
#     if marks<35:
#         passed=False
# if passed:
#     percentage=total/5
# if marks>90:
#     grade="A"        
# elif marks<= 80 and marks>70:
#     grade="B"       
# elif marks>60 and marks<70:
#     grade=c
# else :
#     grade="f"
#     print(total,marks)
#     if passed:
# total = 0
# passed = True
# grade = ""

# for i in range(5):
#     marks = int(input("Enter your marks: "))
#     total = total + marks 

#     if marks < 35:
#         passed = False 

# percentage = (total / 5) * 100
# if passed:
#     if percentage >= 90:
#         grade = "A+"
#     elif percentage >= 80:
#         grade = "A"
#     elif percentage >= 70:
#         grade = "B"
#     elif percentage >= 60:
#         grade = "C"
#     elif percentage >= 50:
#         grade = "D"
#     else:
#         grade = "F"

# if passed:
#     print(f"Total: {total} Percentage: {percentage} Grade: {grade}")
#     print("you are Pass ")
# else:
#     print("Sorry,you are Fail")
total = 0
for i in range(1, 6):
    price = float(input(f"Enter price of product {i}: "))
    total = price + total

if total >= 5000:
    discount_rate = 20
elif total >= 2000:
    discount_rate = 10
elif total >= 1000:
    discount_rate = 5
else:
    discount_rate = 0

discount = total * discount_rate / 100
amount_after_discount = total - discount

# Check membership
member = input("Is the customer a member?(y/n)")

if member == "yes":
    member_discount = amount_after_discount * 5 / 100
    final_amount = amount_after_discount - member_discount
else:
    member_discount = 0
    final_amount = amount_after_discount


print(f"Total Price: ₹{total:.2f}")
print(f"Discount: ₹{discount:.2f}")
print(f"Member Discount: ₹{member_discount:.2f}")
print(f"Final Payable Amount: ₹{final_amount:.2f}")