# Practice Exercises les 5
print('------------------------------------------------------------------------')
print('--------------------- Exercise 5_4 (while-loop)  -----------------------')
print('------------- Nick Bout - 1709217 - V1Q - Programming - HU -------------')
print('------------------------------------------------------------------------')

numbers = []
while True:
    number = int(input('Geef nummer 0:'))
    if number == 0:
        break
    else:
        numbers.append(number)

print('Er zijn {0} getallen ingevoerd, de som is: {1}'.format(len(numbers), sum(numbers)))

print()
