# table of 2

# i = 2
# while i <= 20:
#     print(i)
#     i+=2



# srt1 = (input("Enter a name: "))
# rstr= ""
# i = len(srt1)-1
# while i >= 0:
#     rstr= rstr+srt1[i]
#     i=i-1
# if srt1== rstr:
#     print("string is palindrome")
# else :
#     print("string is not palindrome")  

string=input("enter a string")
i=0
j=len(string)-1
flag=True

while (i<j):
       if string[i]==string[j]:
        i=i+1
        j=j-1
       else :
           flag=False
           i=j #to break the loop 
if flag:
    print("string is a palindrome")           
else: 
      print("string is not a palindrome")  