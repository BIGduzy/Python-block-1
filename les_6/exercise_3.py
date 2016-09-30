# Practice Exercises les 6
print('------------------------------------------------------------------------')
print('------------------------ Exercise 6_3 (dict)  -------------------------')
print('------------- Nick Bout - 1709217 - V1Q - Programming - HU -------------')
print('------------------------------------------------------------------------')

def askNames():
    names = {}
    while True:
        name = input('Enter a name: ').capitalize() # capitalize the name so nick and Nick still counts as 1
        if name == '':
            break

        if name in names:
            names[name] += 1
        else:
            names[name] = 1

    return names

def printNames(names):
    for key, value in names.items():
        if value > 1:
            print('Er zijn', value, 'studenten met de naam:', key)
        else:
            print('Er is', value, 'student met de naam:', key)

names = askNames()
printNames(names)

print()
