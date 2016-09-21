# Practice Exercises les 3
# 3_6 (functie met (im)mutable parameter)
print('------------------------------------------------------------------------')
print('---------- Exercise 3_6 (functie met (im)mutable parameter)  -----------')
print('------------- Nick Bout - 1709217 - V1Q - Programming - HU -------------')
print('------------------------------------------------------------------------')
def wijzig(letterList):
    letterList.clear()
    letterList.extend(['d', 'e', 'f'])

lijst = ['a', 'b', 'c']
print(lijst)
wijzig(lijst)
print(lijst)

print('''
# Waarom kun je in de functie niet de opdracht lijst = ['d', 'e', 'f'] geven?
## Omdat er dan een copie van lijst gemaakt wordt, die vervolgens niet geretured wordt

# Werkt jouw functie ook met een string-parameter? Probeer dit! Waarom werkt het wel/niet?
## Omdat str object de functie clear niet kent, dit is omdat een string immutable is

# Welke rol speelt (im)mutabiliteit in deze vraag?
## Zie vraag b
''')
