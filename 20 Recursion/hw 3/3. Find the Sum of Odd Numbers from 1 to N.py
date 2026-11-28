n = int(input("Enter a number: "))
def odd(n,add = 0):
    if n == 0:
        return add
    if n % 2 != 0:
        add+=n
    return odd(n - 1,add)
print(odd(n))