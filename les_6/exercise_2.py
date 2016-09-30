# Practice Exercises les 6
print('------------------------------------------------------------------------')
print('-------------------- Exercise 6_2 (file & dict)  -----------------------')
print('------------- Nick Bout - 1709217 - V1Q - Programming - HU -------------')
print('------------------------------------------------------------------------')

def getTicketsFromFile(fileName):
    file = open(fileName)
    lines = file.readlines()
    file.close()

    tickets = {}
    for i in lines:
        t = i.replace('\n', '').split(':') # remove line break
        tickets[t[0]] = t[1]

    return tickets

tickets = getTicketsFromFile('tickerSymbols.txt')
print(tickets)

# Ask for company name, give ticker
while True:
    name = input('Enter company name: ')

    if name in tickets:
        print('Ticker symbol:', tickets[name])
        break
    else:
        print('Company not found')

    print()


print()

# Ask for ticker name, give company
while True:
    isCompany = False
    companyName = None
    name = input('Enter ticker name: ')

    for t in tickets:
        if tickets[t] == name:
            isCompany = True
            companyName = t


    if isCompany:
        print('Company name:', companyName)
        break
    else:
        print('Ticker not found')

    print()
