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
n=7
for i in range(1,n+1,2):
    print(" " * ( n- i) + "* " * i)
