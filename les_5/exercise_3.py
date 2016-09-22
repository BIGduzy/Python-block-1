# Practice Exercises les 5
print('------------------------------------------------------------------------')
print('------------------------ Exercise 5_3 (lists)  -------------------------')
print('------------- Nick Bout - 1709217 - V1Q - Programming - HU -------------')
print('------------------------------------------------------------------------')

invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
strings = invoer.split('-')
numbers = []
for i in strings:
    numbers.append(int(i))
numbers.sort()

print('Gesorteerde list van ints:', numbers)
print('Grootste getal:', numbers[-1], 'en kleinste getal:', numbers[0])
print('Aantal getallen:', len(numbers), 'en som van de getallen:', sum(numbers))
print('gemiddelde:', sum(numbers) / len(numbers))

print()
