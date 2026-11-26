# def show(n):
#     if n == 0:
#         print("End")
#         return

#     print("Start", n)
#     show(n - 1)
#     print("Back", n)

# # show(2)
# x = "G"
# def outer():
#     x = "E"
#     def inner():
#         print(x)
#     inner()
# # outer()
# def outer():
#     count = 0

#     def inner():
#         count = count + 1

#     inner()

# outer()
x = 10

def demo():
    print(x)
    x = 20

demo()
