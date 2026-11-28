message = input("Enter a string: ")
num = int(input("Enter a Number: "))
def msg(message,n=1):
    if n > num:
        return
    if 1<=n<=num:
        print(message)
    msg(message,n+1)
(msg(message))