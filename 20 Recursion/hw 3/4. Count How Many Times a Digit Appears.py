def digit(num, target):
    if num == 0:
        return 0
    count = 0
    if num % 10 == target:
        count = 1
    return count + digit(num // 10, target)
print(digit(54354544, 5))