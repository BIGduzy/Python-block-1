import time

# Practice Exercises les 8
print('------------------------------------------------------------------------')
print('---------------------- Exercise 8_2 (Namespaces)  ----------------------')
print('------------- Nick Bout - 1709217 - V1Q - Programming - HU -------------')
print('------------------------------------------------------------------------')

b = 7


def f(y):
    return 2 * y + 1


def g(x):
    return 5 + x + 10


def verdubbel_b():
    global b
    b = b + b

verdubbel_b()

print(b)
print(time.strftime(("%H:%M:%S")))
print(f(3) + g(3))

print()
