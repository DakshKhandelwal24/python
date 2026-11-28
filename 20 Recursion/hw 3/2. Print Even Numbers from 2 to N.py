n = int(input("Enter a number: "))
def even(n):
    if n == 0:
        return
    even(n - 1)
    if n % 2 == 0:
        print(n, end=" ")
even(n)
