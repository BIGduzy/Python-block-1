import csv

# Practice Exercises les 7
print('------------------------------------------------------------------------')
print('--------------- Exercise 7_4 (CSV-files met headers)  --------- --------')
print('------------- Nick Bout - 1709217 - V1Q - Programming - HU -------------')
print('------------------------------------------------------------------------')

with open('products.csv', 'r') as file:
    mostExpensive = None
    leastStocked = None
    totalStock = 0
    highestPrice = 0
    lowestStock = 999999
    reader = csv.DictReader(file, delimiter = '\t', quotechar = '|')

    for row in reader:
        price = float(row['Prijs'])
        stock = int(row['Voorraad'])

        # Total stock
        totalStock += stock

        # price
        if price > highestPrice:
            highestPrice = price
            mostExpensive = row

        if stock < lowestStock:
            lowestStock = stock
            leastStocked = row

    print()
    print('Het duurste artikel is', mostExpensive['Naam'], 'en die kost', mostExpensive['Prijs'], 'Euro')
    print('Er zijn slechts', leastStocked['Voorraad'], 'exemplaren in voorraad van het product met nummer', leastStocked['Artikelnummer'])
    print('In totaal hebben wij', totalStock, 'producten in ons magazijn liggen')

print()
