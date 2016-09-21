# Practice Exercises les 1
# 1_1 (expressions)
print('------------------------------------------------------------------------')
print('--------------------- Exercise 1_1 (expressions) -----------------------')
print('------------- Nick Bout - 1709217 - V1Q - Programming - HU -------------')
print('------------------------------------------------------------------------')
print('''
| Expression        | Uitkomst          | Type              |
| 5                 | 5                 | Integer (int)     |
| 5.0               | 5.0               | Float (float      |
| 5 % 2             | 1                 | Integer (int)     |
| 5 > 1             | True              | Boolean (bool)    |
| '5'               | '5'               | String (str)      |
| 5 * 2             | 10                | Integer (int)     |
| '5' * 2           | '55'              | String (str)      |
| '5' + '2'         | '52'              | String (str)      |
| 5 / 2             | 2.5               | Float (float)     |
| 5 // 2            | 2                 | Integer (int)     |
|[5, 2, 1]          | [5, 2, 1]         | List (list)       |
| 5 in [1, 4, 6]    | False             | Boolean (bool)    |
''')
print()


# 1_2 (strings)
print('------------------------------------------------------------------------')
print('----------------------- Exercise 1_2 (strings) -------------------------')
print('------------- Nick Bout - 1709217 - V1Q - Programming - HU -------------')
print('------------------------------------------------------------------------')
myName = 'Nick Bout'
myAddress = 'Burgemeester Doormanstraat 3'
result = 'Ik ben ' + myName + ' en mijn adres is: ' + myAddress
print(result)
print()


# 1_3 (string)
print('------------------------------------------------------------------------')
print('----------------------- Exercise 1_3 (strings) -------------------------')
print('------------- Nick Bout - 1709217 - V1Q - Programming - HU -------------')
print('------------------------------------------------------------------------')
longWord = 'Supercalifragilisticexpialidocious'
# A
print('A: ', 'The length of ', longWord, ' equals: ', len(longWord))
# B
search = 'ice'
print('B: ', longWord, ' does' if longWord.index(search) else ' does not', 'contain', search, '.')
# C
longWord1 = 'Antidisestablishmentarianism'
longWord2 = 'Honorificabilitudinitatibus'
print('C: ', longWord1, ' is' if len(longWord1) > len(longWord2) else ' is not', 'longer than ', longWord2)
# D
list = ['Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein']
list.sort()
print('D: ', 'The first in alphabetical order equals: ', list[0], ' the last in alphabetical order equals: ', list[-1])
print()


# 1_4 (getallen)
print('------------------------------------------------------------------------')
print('----------------------- Exercise 1_4 (getallen) ------------------------')
print('------------- Nick Bout - 1709217 - V1Q - Programming - HU -------------')
print('------------------------------------------------------------------------')
cijferCSN = 7.7
cijferICOR = 4.8
cijferPROG = 9
average = (cijferCSN + cijferICOR + cijferPROG) / 3
summary = 'Mijn cijfers ( gemiddeld een ' + str(round(average, 1)) + ' ) leveren een beloning van € ' + str(average * 3 * 30) + ' op!'
print(summary)
print()

# 1_5 (list)
print('------------------------------------------------------------------------')
print('------------------------ Exercise 1_5 (list) ---------------------------')
print('------------- Nick Bout - 1709217 - V1Q - Programming - HU -------------')
print('------------------------------------------------------------------------')
# A
favorites = ['Harry Baksel']
print('A: ', favorites)
# B
favorites.append('Karel barel')
print('B: ', favorites)
# C
favorites[1] = 'Wouter Dijkstra'
print('C: ', favorites)
print()
