# Practice Exercises les 7
print('------------------------------------------------------------------------')
print('----------------- Exercise 7_1 (catching exceptions)  ------------------')
print('------------- Nick Bout - 1709217 - V1Q - Programming - HU -------------')
print('------------------------------------------------------------------------')

cost = 4356
numPersons = input('Met hoeveel personen zijn jullie: ')

try:
    numPersonsInt = int(numPersons)

    if numPersonsInt < 0:
        print('Negatieve getallen zijn niet toegestan!')
    else:
        costPP = cost / numPersonsInt
        print(costPP)
except ZeroDivisionError:
    print('Delen door nul kan niet!')
except ValueError:
    print('Gebruik cijfers voor het invoeren van het aantal!')
except:
    print('Onjuiste invoer')

print()
