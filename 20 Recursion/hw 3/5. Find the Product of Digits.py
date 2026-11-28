def product(n):
    if n == 0:
        return 1
    i= n%10
    return i*product(n//10)
print(product(234333))