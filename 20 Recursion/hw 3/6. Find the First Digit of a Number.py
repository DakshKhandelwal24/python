def left(n):
    if 0<=n<10:
        return n
    i = n%10
    count =i
    return left(n//10)
print(left(6837))