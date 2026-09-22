#1

string = input("Enter a string: ")
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
space = " "
special = "!@#$%^&*~`|?"
upper_count = 0
lower_count = 0
digit_count = 0
space_count = 0
special_count = 0
highest = upper_count
highest_count = 0

for i in string:
    for j in uppercase:
        if i == j:
            upper_count += 1
    for j in lowercase:
        if i == j:
            lower_count += 1
    if i == space:
        space_count += 1
    for j in digits:
        if i == j:
            digit_count += 1
    for j in special:
        if i == j:
            special_count += 1

if lower_count > highest:
    highest = lower_count
if digit_count > highest:
    highest = digit_count
if space_count > highest:
    highest = space_count
if special_count > highest:
    highest = special_count

if upper_count == highest:
    highest_count += 1
if lower_count == highest:
    highest_count += 1
if digit_count == highest:
    highest_count += 1
if space_count == highest:
    highest_count += 1
if special_count == highest:
    highest_count += 1
if highest_count >= 2:
    print("Tie")
else:
    if upper_count == highest:
        print("Uppercase")
    elif lower_count == highest:
      print("Lowercase")
    elif digit_count == highest:
      print("Digits")
    elif space_count == highest:
         print("Spaces")
    else:
        print("Special Characters")




