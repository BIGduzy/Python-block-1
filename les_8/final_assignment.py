import xmltodict

# Final assignment les 8
print('------------------------------------------------------------------------')
print('----------------------- Final assignment les 8  ------------------------')
print('------------- Nick Bout - 1709217 - V1Q - Programming - HU -------------')
print('------------------------------------------------------------------------')

xml = xmltodict.parse(open('nsPropaganda.xml', 'rb'))
stations = xml['Stations']['Station']

print(stations)

print('Dit zijn de codes en types van de 4 stations:')
for i in stations:
    print(i['Code'], '-', i['Type'])

print()

print('Dit zijn alle stations met één of meer synoniemen:')
for i in stations:
    if i['Synoniemen']:
        print(i['Namen']['Middel'] + ':')
        for j in i['Synoniemen']['Synoniem']:
            print('\t-', j)

print()

print('Dit zijn de codes en types van de 4 stations:')
for i in stations:
    print(i['Code'], '-', i['Namen']['Lang'])

print()
