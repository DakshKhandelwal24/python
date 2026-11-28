def left(n,tar=23):
    if 0<=n<10:
        return True
    if n%10 == tar:
        return True
    return left(n//10)
print(left(1234))