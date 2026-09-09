username=input("entre username")
password=input("entre password")
Username = input("enter the username:")
Password = input("enter the password:")

if Username=="admin" and Password=="python123":
    print("login successful")
elif Password!="python123":
    print("Wrong password")
elif Username!="admin":
    print("User not found")
else:
    print("please try again")