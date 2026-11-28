def cnt(n):
    if n == "":
        return 0
    return 1 + cnt(n[1:])
print(cnt("coding"))
