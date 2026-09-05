# if Entre :
#     print("Hey there!!")
# Result=12
# if Result>32 :
#     print("passs!!")

# else :
# #     print("fail!!")

is_indian=input("Are you indian ? yes or no:")

if is_indian=="yes":
    age=int(input("Enter your age:-"))
    if age>=18:
        print("allowed to vote")
    if age<18:
        print("you are not elligable for vote rn")

if is_indian=="no":
        print("you are not allowed to vote")