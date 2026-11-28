n = input("Enter a String: ")
def palan(n,a=0):
    b=len(n)-1-a
    if a > b:
        return True
    if n[a]!=n[b]:
        return False
    return palan(n,a+1)
print(palan(n))