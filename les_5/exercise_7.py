# Practice Exercises les 5
print('------------------------------------------------------------------------')
print('------------------- Exercise 5_7 (nested loop)  ------------------------')
print('------------- Nick Bout - 1709217 - V1Q - Programming - HU -------------')
print('------------------------------------------------------------------------')

for i in range(1, 11):
    print('Tafel van:', i)
    for j in range(1, 11):
        print('{0:2} x {1:2} = {2}'.format(i, j, i * j))
    print()
print()
