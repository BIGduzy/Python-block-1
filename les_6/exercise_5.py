from random import randint

# Practice Exercises les 6
print('------------------------------------------------------------------------')
print('----------------------- Exercise 6_5 (random)  -------------------------')
print('------------- Nick Bout - 1709217 - V1Q - Programming - HU -------------')
print('------------------------------------------------------------------------')

def monopolyDice():
    double = True
    numDoubles = 0;

    while double and numDoubles < 3:
        # rol dices
        dice1 = randint(1, 6)
        dice2 = randint(1, 6)
        double = dice1 == dice2

        # 3 doubles and you are in prison
        if double:
            numDoubles += 1

        # print outcome
        printTurn(dice1, dice2, double, numDoubles)

def printTurn(dice1, dice2, double, numDoubles = 0):
    if numDoubles > 2 and double:
        print(dice1, '+', dice2, '=', '(direct naar gevangenis)')
    elif double:
        print(dice1, '+', dice2, '=', dice1 + dice2, '(dubbel)')
    else:
        print(dice1, '+', dice2, '=', dice1 + dice2)

monopolyDice()

print()
