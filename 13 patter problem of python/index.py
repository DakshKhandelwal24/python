# # question 1
# for i in range(3):
#     for j in range(3):
#         print("*", end=" ")
#     print()



# question 2
# num=int(input("enter your input"))
# for i in range(1,4):
#     for k in range(1,4):
#         print(k, end=" ")
#     print()



# question 3
# num=int(input("enter your input"))
# for i in range(1,4):
#     for j in range(1,4):
#         print(i,end=" ")
#     print() 


# question 4
# for i in range (1,6):
#     for k in range(i):
#         print("*",end=" ")
#     print()

# Question 5
# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()    

# Question 6
# num=int(input("enter till where uou want to print number"))
# for i in range(1,6):
#     for j in range(1,i+1):
#       print(j,end=" ")
#     print()  

# # Question 7
# num=int(input("enter number till where you want to print:"))
# for i in range(1,6):
#     for k in range(i):
#         print(i,end=" ")
#     print()    


# Question 8
# for i in range(1,11):
#     for j in range(1,11):
#         print(f"{i} X {j} = {i*j}")
#     print()    

# Question 9
# for i in range(1,4):
#     for j in range(1,6):
#         print(f"{i*j}" ,end=" ")
#     print()    

# question 10
# for i in range(5):
#     for j in range(1,6):
#         print(j*j,end=" ")
#     print()   
# 
# quesion 11
# for i in range(1,6):
#     for j in range(i):
#         print(chr(65+j),end=" ")
#     print()    

# question 12
# for i in range(1,6):
#     for j in range(i):
#         print(chr(64+i),end=" ")
#     print()    

# Question 13
# num = int(input("enter a number :"))
# for i in range(0,num+1,2):
#     for j in range(1,i,2):
#         print(j,end=" ")
#     print()


# Question 14
# num = int(input("enter a number :"))
# for i in range(2,num,2):
#     for j in range(2,i,2):
#         print(j,end=" ")
#     print()


#     # question 15
# for i in range(1,6):
#     for j in range(1,6):
#         print("*",end=" ")
#     print()            

#     # QUEStion 16
# for i in range(1,6):
#     for j in range(1,6):
#         print(j,end=" ")
#     print()

#     # question 17
#     num = int(input("enter a number :"))
# for i in range(1,num,3):
#     for j in range(i,i+3):
#         print(j,end=" ")
#     print()

#     # question 18
#     num = int(input("enter a number :"))
# for i in range(1,21,5):
#     for j in range(i,i+5):
#         print(j,end=" ")
#     print()
#     # Question 19
#     num = int(input("enter a number :"))
# for i in range(1,num+1):
#     for j in range(1,num+1):
#         print(f"({i},{j})",end=" ")
#     print()
#     # question 20
# num = 3
# for i in range(1,num+1):
#      for j in range(1,num+1):
#         print(i,j)

#     # question 21
# for i in range(1,11):
#      for j in range(1,11):
#          print(f"{i} X {j} = {i*j}")
#      print()

#     # Question 22
#     num = int(input("enter a number :"))
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print(i,end="")
#     print()

#     # question 23
#     num = int(input("enter a number :"))
# for i in range(num,0,-1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

#     # Question 24
#     num = int(input("enter a number :"))
# for i in range(num,0,-1):
#     for j in range(0,i):
#         if j==1:
#             print("5",end="")
#         elif j==2:
#             print("4",end="")
#         elif j==3:
#             print("3",end="")
#         elif j==4:
#             print("2",end="")
#         elif j==5:
#             print("1",end="")
#     print()
#     # Question 25
#     num = int(input("enter a number :"))
# for i in range(1,num+1):
#     for j in range(1,num+1):
#         print(i,end="")
# #     print()
# num = int(input("enter a number :"))
# for i in range(0,num+1,2):
#     for j in range(1,i,2):
#          print(j,end=" ")
#          print()
# question 14
# for i in range(1,6):
#     a=1
#     for j in range(i):
#         print(a,end=" ")
#         a += 2
#     print() 
string = input("Enter any string : ")
count = 0       # uppercase
count1 = 0      # lowercase
count2 = 0      # digits
count3 = 0      # spaces
count4 = 0      # special characters
for i in string:
    if i >= chr(65) and i <= chr(90):
        count += 1
    elif i >= chr(97) and i <= chr(122):
        count1 += 1
    elif i >= chr(48) and i <= chr(57):
        count2 += 1
    elif i == " ":
        count3 += 1
    else:
        count4 += 1
if count > count1 and count > count2 and count > count3 and count > count4:
    print(f"Highest count is of uppercase letters, Count is: {count}")
elif count1 > count and count1 > count2 and count1 > count3 and count1 > count4:
    print(f"Highest count is of lowercase letters, Count is: {count1}")
elif count2 > count and count2 > count1 and count2 > count3 and count2 > count4:
    print(f"Highest count is of digits, Count is: {count2}")
elif count3 > count and count3 > count1 and count3 > count2 and count3 > count4:
    print(f"Highest count is of spaces, Count is: {count3}")
elif count4 > count and count4 > count1 and count4 > count2 and count4 > count3:
    print(f"Highest count is of special characters, Count is: {count4}")
else:
    print("Tie")