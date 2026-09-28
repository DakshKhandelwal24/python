sentence = input("Enter any sentence :").lower()
words = sentence.split()
highest_score = 0
for i in words :
    score = 0 
    for i in i :
        if i == "aeiou":
            score += 2
        elif i == "bcdfghiklmnpqrstvwxyz":
            score += 1
        elif i == "0123456789":
            score += 3
        else:
            score += 4
    if score > highest_score :
        highest_score = score
        word = i
print(word)