#  question 1

# def show(n):
#     if n == 0:
#         print("Stop")
#         return

#     print(n)
#     show(n - 1)
#     print(n)

# show(2)


# output
# 2
# 1
# Stop
# 1
# 2

# question 2

# def total(n):
#     if n == 0:     # base case
#         return 0

#     return n + total(n - 1)

# here in line 2 the condition returns a value stoping the recalling of functon. 

#  question 3

# def count(n):
#     if n == 0:
#         return

#     count(n - 1)

# here Recursion will stop when n becomes 0 and 2 being a positive number n wont become 0 as the expression in increasing.

#  question 4

def answer(n):
    if n == 0:
        return 0

    n + answer(n - 1)

print(answer(3))

# Here a Typeerror rise.

# question 5

def countdown(n):
    if n==0:
        print("done")
        return
    print(n)
    countdown(n+1)

countdown(3)
countdown(0)

#  question 6

def count_up(n,c=0):
    if n==c:
        return
    c+=1
    print(c)
    count_up(n,c)

count_up(3)
count_up(0)

# question 7

def sum_to(n):
    if n==0:
        return 0

    return n + sum_to(n-1)


print(sum_to(5))  # 15
print(sum_to(0))  # 0

#  question 8

def factorial(n):
    if n==0:return 1
    return n * factorial(n-1)



print(factorial(4))  # 24
print(factorial(0))  # 1

#  question 9

def digit_sum(n):
    if n==0:
        return 0
    return n%10 + digit_sum(n//10)

print(digit_sum(583))  # 16
print(digit_sum(7))    # 7
print(digit_sum(0))    # 0

#  question 10

def power(base, exponent):
    if exponent==0:return 1
    return base * power(base,exponent-1)

print(power(2, 5))  # 32
print(power(9, 0))  # 1
print(power(3, 1))  # 3

# question 11

def count_digits(n):
    if -10<n<10:return 1
    return 1 + count_digits(n//10)

print(count_digits(5382))  # 4
print(count_digits(6))     # 1
print(count_digits(0))     # 1
print(count_digits(-123))     # 3

# question 12

def reverse_text(s):
    if s=="":return ""
    return reverse_text(s[1:]) + s[0]



print(reverse_text("cat"))  # "tac"
print(reverse_text("a"))    # "a"
print(reverse_text(""))     # ""

#  question 13

def fibonacci(n):
    if n<=1:return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(0))  # 0
print(fibonacci(1))  # 1
print(fibonacci(6))  # 8

#  question 14

def max_digit(n,m=0):
    m=n%10 if n%10 > m else m
    if n==0:return m
    return max_digit(n//10,m)

print(max_digit(4729))  # 9
print(max_digit(555))   # 5
print(max_digit(0))     # 0

#  question 15

def mystery(n):
    if n <= 1:
        return n

    return mystery(n - 1) + mystery(n - 2)

# the code is for fibonacci number
# for mystery(4) :
#     mystery(3)+mystery(2)
#     mystery(2)+mystery(1)+mystery(1)+mystery(0)
#     mystery(1)+mystery(0)+1+1+0
#     1+0+2
#     3

# also mystery(0), mystery(1), mystery(2) = 0, 1, 1


# // question 16

def factorial(n):
    if n == 0:
        # return 0
        return 1

    return n * factorial(n - 1)

# // question 17

def stop_at_zero(n):
    if n == 0:
        return

    # stop_at_zero(n)
    stop_at_zero(n-1)


# // question 18

# it gives a error.
# RecursionError
# because loops don't have a reversal so they have better time complex