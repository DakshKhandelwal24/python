# Ques - 1
# def show(n):
#     if n == 0:
#         print("Stop")
#         return
#     print(n)
#     show(n - 1)
#     print(n)
# show(2)

# Output :
# 2
# 1
# Stop
# 1
# 2


# Ques - 2
# def total(n):
#     if n == 0:
#         return 0
#     return n + total(n - 1)

# The base case is if n == 0: return 0.
# When n becomes 0, the function stops calling itself and returns 0. This stops recursion.


# Ques - 3

# def count(n):
#     if n == 0:
#         return
#     count(n+1)

# Here the function using (n + 1) instead of (n - 1).
# When we call count(2), so n keeps increasing (3, 4, 5 etc.) instead of printing 0.

# correct code 
# def count(n):
#     if n==0:
#         return
#     count(n-1)


# Ques - 4
# def answer(n):
#     if n == 0:
#         return 0
#     (n + answer(n - 1))

# print(answer(3))
# Because n+answer(n - 1) has no return statement The function calculates the value but does not return it.

# Ques - 5
# def countdown(n):
#     if n == 0:
#         print("Done!")
#         return
#     print(n)
#     countdown(n - 1)
# countdown(3)

# Ques - 6
# def count_up(n):
#     if n == 0:
#         return
#     count_up(n - 1)
#     print(n)
# count_up(4)

# Ques - 7
# def sum_to(n):
#     if n==0:
#         return 0 
#     return n+sum_to(n - 1)
# print(sum_to(5))
# print(sum_to(0))

# Ques - 8
# def factorial(n):
#     if n==0:
#         return 1
#     return n*factorial(n - 1)
# print(factorial(4))
# print(factorial(0))

# Ques - 9
# def digit_sum(n):
#     if n<10:
#         return n
#     return n%10 + digit_sum(n//10)
# print(digit_sum(583))  
# print(digit_sum(7))    
# print(digit_sum(0))

# Ques - 10
# def power(base, exponent):
#     if exponent == 0:
#         return 1
#     return base * power(base, exponent - 1)
# print(power(2, 5))
# print(power(9, 0))
# print(power(3, 1))

# Ques - 11
# def count_digits(n):
#     if n<10:
#         return 1
#     return 1+count_digits(n//10)
# print(count_digits(5382))
# print(count_digits(6))
# print(count_digits(0))
