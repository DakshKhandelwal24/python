# # Problem 1

# # IPO Model 

# INPUT
# Read 1 number
# Read 2 number

# PROCESSING
# # Add 1 and 2 number

# # OUTPUT
# # Sum of 2 number

# # Algorithm 
# # 1. Start 
# # 2. Read firdt number
# # 3. Read 2 number
# # 4. Add both numbers
# # 5. Display their sum
# # 6. Stop 

# # Python Solution
# number_1 = int(input("Enter 1 number "))
# number_2 = int(input("Enter 2 number "))

# sum = number_1 + number_2

# print(sum)

# # #Problem 2

# #IPO Model
 # INPUT 
 # Read a number 

# # PROCESSING
# # If number is divisible by 2 - Even 
# # Otherwise - Odd 

# # OUTPUT
# # Display the result whether it's even or odd


#  #Algorithm
# ]# 1. Start
#  2. Read a number
#  3. If number is divisible by 2
#  4. Display even 
#  5. Otherwise display odd
#  6. Stop


# #Python Solution
# number = int(input("Enter a number: "))

# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# #Problem 3

# # IPO Model 

# # INPUT
# # Read 1 number 
# # Read 2 number 
# # Read third number 

# # PROCESSING
# # If 1 number is greater than 2 and third number - First number is greater 
# # If 2 number is greater than 1 and third number - Second number is greater 
# # otherwise - Third number is greater

# # OUTPUT 
# # display which number is greater

# # Algorithm
# # 1. Start 
# # 2. Read 1 number 
# # 3. Read 2 number 
# # 4. Read third number 
# # 5. If 1 number is greater than 2 and third number 
# # 6. Display 1 number is greater
# # 7. If 2 number is greater than 1 and third number 
# # 8. Display 2 number is greater
# # 9. Otherwise display third number is greater 
# # 10. Stop 

# # Python Solution
# number_1 = int(input("Enter 1 number: "))
# number_2 = int(input("Enter 2 number: "))
# number_3 = int(input("Enter third number: "))

# if number_1 > number_2 and number_1 > number_3:
#     print(f"{number_1} is greater")
# elif number_2 > number_1 and number_2 > number_3:
#     print(f"{number_2} is greater")
# else:
#     print(f"{number_3} is greater")

# #Problem 4

# # IPO 

# # INPUT 
# # Read person's age

# # PROCESSING
# # If person is greater than or equal to 18 -  Eligible to vote
# # Otherwise - Not eligible to vote

# # OUTPUT
# # Print either eligible to vote or not eligible to vote


# # Algorithm
# # 1. Start 
# # 2. Read person's age 
# # 3. If person is greater than or equal to 18
# # 4. Display eligible to vote
# # 5. otherwise display not eligible to vote
# # 6. Stop 

# # Python Solution
# age = int(input("Enter age: "))

# if age >= 18:
#     print("Eligible to vote")
# else:
#     print("Not eligible to vote")

# # Problem 5

# # IPO 

# # INPUT 
# # Read price of an item 

# # PROCESSING 
# # Create a discount variable and assign 0 value to it.
# # If price is greater than or equal to 2000,
# # Give 20% discount and subtract it from original price 
# # otherwise discount = 0

# # OUTPUT
# # Display the final price

# # Algorithm
# # 1. Start 
# # 2. Read price of an item
# # 3. Create a discount variable and assign 0 value to it
# # 4. If price is greater than or equal to 2000
# # 5. Update the discount value 
# # 6. otherwise keep the discount 0
# # 7. Subtract it from original price
# # 8. Display the final price
# # 9. Stop 

# # Python Solution
# price = float(input("Enter price: "))
# discount = 0

# if price >= 2000:
#     discount = price * 0.2
#     price = price - discount
# else:
#     discount = 0

# print(f"Price: {price} ₹")

# # Problem 6
# # INPUT

# # Read 1 subject marks
# # Read 2 subject marks
# # Read third subject marks

# # PROCESSING

# # Calculate average

# # OUTPUT

# # Display Pass or Fail


# # Algorithm

# # 1. Start
# # 2. Read 1 subject marks
# # 3. Read 2 subject marks
# # 4. Read third subject marks
# # 5. Calculate average
# # 6. If average is greater than or equal to 40
# # 7. Display Pass
# # 8. Otherwise display Fail
# # 9. Stop


# # Python Solution

# marks_1 = float(input("Enter 1 subject marks: "))

# marks_2 = float(input("Enter 2 subject marks: "))

# marks_3 = float(input("Enter third subject marks: "))

# average = (marks_1 + marks_2 + marks_3) / 3

# if average >= 40:
#     print("Pass")
# else:
# #     print("Fail")
# row = 3
# for i in range(row+1):
#     for j in range (i + 1):
#         print("*",end=" ")
number=int(input("Enter a Number"))
middle= number//2+1
for i in range(1,number+1):
    for j in range(1,number+1):
        if j==1 or j==number or i==number or (i==middle and j==middle ):
            print("* ",end="")
        else:
            print(" " , end="")
    print()