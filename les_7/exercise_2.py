from datetime import datetime
import csv

# Practice Exercises les 7
print('------------------------------------------------------------------------')
print('----------------- Exercise 7_2 (CSV-files schrijven)  ------------------')
print('------------- Nick Bout - 1709217 - V1Q - Programming - HU -------------')
print('------------------------------------------------------------------------')

file = 'inloggers.csv'

while True:
    name = input('Wat is je achternaam? ')
    if name == 'exit':
        break

    voorl = input("Wat zijn je voorletters? ")
    gbdatum = input("Wat is je geboortedatum? ")
    email = input("Wat is je e-mail adres? ")

    # write to file
    with open(file, 'a', newline = '') as csvFile:
        writer = csv.writer(csvFile, delimiter = ';', quotechar = '|', quoting = csv.QUOTE_MINIMAL)

        writer.writerow([datetime.now().strftime('%a %d %b %Y at %H:%M'), name, voorl, gbdatum, email])

    print()

print()
