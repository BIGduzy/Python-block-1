# Practice Exercises les 6
print('------------------------------------------------------------------------')
print('------------------------ Exercise 6_1 (dict)  --------------------------')
print('------------- Nick Bout - 1709217 - V1Q - Programming - HU -------------')
print('------------------------------------------------------------------------')

def getGoodGrades(grades):
    goodGrades = []
    for key, value in grades.items():
        if value >= 9:
            goodGrades.append({ key: value })

    return goodGrades

grades = { 'wouter': 10, 'nick': 8, 'eelke': 7, 'marco': 6, 'camille': 9 }
print(getGoodGrades(grades))

print()
