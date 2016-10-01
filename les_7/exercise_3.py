import csv

# Practice Exercises les 7
print('------------------------------------------------------------------------')
print('------------------ Exercise 7_3 (CSV-files lezen)  ---------------------')
print('------------- Nick Bout - 1709217 - V1Q - Programming - HU -------------')
print('------------------------------------------------------------------------')

with open('scores.csv', 'r') as file:
    highScore = 0
    best = None
    reader = csv.reader(file, delimiter = ';', quotechar = '|')

    for row in reader:
        score = int(row[2])
        if score > highScore:
            highScore = score
            best = row

    print('De hoogste score is:', row[2], 'op', row[1], 'behaald door', row[0])

print()
