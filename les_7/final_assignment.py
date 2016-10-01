import csv
from random import randint

# Final assignment les 7
print('------------------------------------------------------------------------')
print('----------------------- Final assignment les 7  ------------------------')
print('------------- Nick Bout - 1709217 - V1Q - Programming - HU -------------')
print('------------------------------------------------------------------------')


## functions ##

# getAvailableLockers
# returns all available lockers from the LOCKERS tuple
#
# @return List || List with the lockers dictionaries
def getAvailableLockers() -> list:
    openLockers = []

    for i in LOCKERS:
        if i['in_use'] == 'FALSE':
            openLockers.append(i)

    return openLockers


# getValidOption
# Asks user for option from options tuple
#
# @return Int || The index of the option in the options tuple
def getValidOption() -> int:
    optionInt = 0
    while True:
        option = input('Optie nummer: ')
        try:
            optionInt = int(option) - 1 # we use -1 because our tuple starts with 0
        except:
            optionInt = -1 # -1 will print "optie onbekent"

        if optionInt >= 0 and optionInt <= len(OPTIONS):
            break

        print('Optie onbekent')
        print()

    return optionInt


# setLocker
# sets locker in the csv file
#
# @param Int locker || Locker number (in the csv file, not the list index)
# @param String code || 4 digit code for the locker || default '0000'
# @param Bool inUse || in_use field for csv file || default False
# @return Void
def setLocker(locker, code = '0000', inUse = False):
    inUse = 'TRUE' if inUse else 'FALSE'
    with open(FILE_NAME, 'w', newline = '') as file:
        writer = csv.DictWriter(file, ['locker', 'code', 'in_use'], delimiter = ',', quotechar = '|', quoting = csv.QUOTE_MINIMAL)
        writer.writeheader()

        for row in LOCKERS:
            if row['locker'] == locker:
                writer.writerow({ 'locker': locker, 'in_use': inUse, 'code': code })
                row['in_use'] = inUse
                row['code'] = code
            else:
                writer.writerow(row)


# init
# initializes program
#
# @return Void
def init():
    with open(FILE_NAME, 'r') as file:
        reader = csv.DictReader(file, delimiter = ',', quotechar = '|')

        # get open lockers
        for row in reader:
            LOCKERS.append(row)

# newLocker
# sets available locker with random code and prints is
#
# @return Void
def newLocker():
    openLockers = getAvailableLockers()

    if len(openLockers) == 0:
        print('Er zijn geen kluizen vrij')
        return

    # get random free locker
    locker = openLockers[randint(0, len(openLockers) - 1)]['locker']
    # random 4 digit code
    code = str(randint(0, 9)) + str(randint(0, 9)) + '' + str(randint(0, 9)) + '' + str(randint(0, 9))

    # write te locker to te csv file
    setLocker(locker, code, True)
    print('Uw kluis nummer is:', locker, 'met de code:', code)


# openLocker
# Asks user for locker number and code to open a locker
#
# return Dict || The locker that is opened || returns None if somting went wrong
def openLocker() -> dict:
    locker = None
    while True:
        attempt = 0
        lockerNumber = input('Welk kluis nummer? ')
        validLocker = False

        # check for locker
        for i in LOCKERS:
            if i['locker'] == lockerNumber:
                validLocker = True

                # Ask for code
                while attempt < 3:
                    code = input('Geef het 4 cijferige nummer ({0} pogingen resterend): '.format(3 - attempt))
                    attempt += 1

                    if code == i['code']:
                        locker = i
                        break # break while for code

                    print('Code niet correct')

                break # break for LOCKERS

        if bool(locker) or attempt >= 3:
            break # break while True

        if not validLocker:
            print('Kluis niet gevonden')
        print()

    return locker

# freeLocker
# Asks user for locker and resets that one
#
# @return Void
def freeLocker():
    locker = openLocker()

    if bool(locker):
        setLocker(locker['locker'], '0000')
        print('Kluis:', locker['locker'], 'vrij gegeven')
    else:
        print('Teveel foute pogingen')


# printAvailableLockers
# prints available lockers
#
# @return Void
def printAvailableLockers():
    lockers = getAvailableLockers()

    if len(lockers) == 0:
        print('Er zijn geen kluizen vrij')
        return

    print('De volgende kluizen zijn nog vrij')
    for i in lockers:
        print(i['locker'], end = ', ')

    print()


# printOpenLocker
# Opens locker and prints outcome
#
# @return Void
def printOpenLocker():
    locker = openLocker()

    if bool(locker):
        print('Kluis:', locker['locker'],' geopend')
    else:
        print('Teveel foute pogingen')


# printOptions
# prints all options from the options tuple
#
# @return Void
def printOptions():
    index = 1
    for i in OPTIONS:
        print('{0}: {1}'.format(index, i['info']))
        index += 1

    print()


## CONTANTS ##
OPTIONS = (
    { 'info': 'Ik wil een nieuwe kluis', 'function': newLocker },
    { 'info': 'Ik wil mijn kluis openen', 'function': printOpenLocker },
    { 'info': 'Ik geef mijn kluis terug', 'function': freeLocker },
    { 'info': 'Ik wil weten hoeveel kluizen nog vrij zijn', 'function': printAvailableLockers },
    { 'info': 'Ik wil stoppen' },
)

FILE_NAME = 'lockers.csv'
LOCKERS = []



## MAIN PROGRAM ##
init()

while True:
    print('Selecteer een optie')
    printOptions()

    option = getValidOption()

    # exit
    if option == 4: # valid option returns given option - 1, so this is "5: ik wil stoppen"
        break

    OPTIONS[option]['function']()
    print()

print('Bedankt en doei')

print()
