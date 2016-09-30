# Practice Exercises les 6
print('------------------------------------------------------------------------')
print('------------------------ Exercise 6_4 (sets)  --------------------------')
print('------------- Nick Bout - 1709217 - V1Q - Programming - HU -------------')
print('------------------------------------------------------------------------')

brown = {
    'Boxtel',
    'Best',
    'Beukenlaan',
    'Eindhoven',
    'Helmond\'t Hout',
    'Helmond',
    'Helmond Brouwhuis',
    'Deurne',
}
green = {
    'Boxtel',
    'Best',
    'Beukenlaan',
    'Eindhoven',
    'Geldrop',
    'Heeze',
    'Weert',
}

print('De zelfde stations')
print(brown.intersection(green))
print()

print('De stations die alleen brown heeft')
print(brown.difference(green))
print()

print('Alle stations')
print(brown.union(green))
print()

print()
