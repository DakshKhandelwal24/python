#3
sentence = input("Enter a sentence: ").lower()
words = sentence.split()
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
digits = "0123456789"
special = "!@#$%^&*~`|?"
highest_score = 0
highest_word = ""

for word in words:
    score = 0
    for i in word:
        for j in vowels:
            if i == j:
                score += 2
        for j in consonants:
            if i == j:
                score += 1
        for j in digits:
            if i == j:
                score += 3
        for j in special:
            if i == j:
                score += 4
    if score > highest_score:
        highest_score = score
        highest_word = word

print("Highest scoring word:", highest_word)
print("Score:", highest_score)




print("Short words:", short)
print("Medium words:", medium)
print("Long words:", long)