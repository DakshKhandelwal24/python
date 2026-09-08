name = input("Enter a character: ")

if name.isupper():
    print("Uppercase alphabet")

elif name.islower():
    print("Lowercase alphabet")

elif name.isdigit():
    print("Digit")

else:
    print("Special character")
