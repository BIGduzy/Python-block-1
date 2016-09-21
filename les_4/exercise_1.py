# Practice Exercises les 4
# 4_1 (formatting)
print('------------------------------------------------------------------------')
print('--------------------- Exercise 4_1 (formatting)  -----------------------')
print('------------- Nick Bout - 1709217 - V1Q - Programming - HU -------------')
print('------------------------------------------------------------------------')
def convert(celsius):
    return celsius * 1.8 + 32

def table():
    print('{0:>5}\t{1:>5}'.format('C', 'F'))
    for i in range(-30, 41, 10):
        f = convert(i)
        print('{0:5}\t{1:5.0f}'.format(i, f))

table()
print()
