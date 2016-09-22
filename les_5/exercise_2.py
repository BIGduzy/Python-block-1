import re

# Practice Exercises les 5
print('------------------------------------------------------------------------')
print('------------------------ Exercise 5_2 (lists)  -------------------------')
print('------------- Nick Bout - 1709217 - V1Q - Programming - HU -------------')
print('------------------------------------------------------------------------')

# I refuse to use eval with input
listString = input('Geef een lijst met minimaal 10 strings: ')
# use regex instead of eval to create list from string, and since we use redex we can use it to only get te 4 letter stings
lst = re.findall(r'"([^"]{4})"', listString)
print('De nieuw-gemaakte lijst met alle vier-letter strings is:', lst)

print()
