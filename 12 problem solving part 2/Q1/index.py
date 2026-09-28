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