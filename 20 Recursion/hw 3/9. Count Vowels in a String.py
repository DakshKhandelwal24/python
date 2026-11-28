def left(n, i=0):
    if i == len(n):
        return 0
    vowels = "aeiou"
    if n[i] in vowels:
        return 1 + left(n, i + 1)
    else:
        return left(n, i + 1)
print(left("education"))