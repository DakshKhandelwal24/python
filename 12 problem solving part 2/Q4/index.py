for i in range(5):
    password = input("Enter password: ")

    upper = False
    lower = False
    digit = False
    special = False

    for PASSCODE in password:
        if PASSCODE.isupper():
            upper = True
        elif PASSCODE.islower():
            lower = True
        elif PASSCODE.isdigit():
            digit = True
        else:
            special = True

    if len(password) >= 8 and upper and lower and digit and special:
        print("Valid Password")
    else:
        print("Invalid Password")