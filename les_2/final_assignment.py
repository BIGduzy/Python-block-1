# Final assignment les 2
print('------------------------------------------------------------------------')
print('------------------------ Final assignment les 2 ------------------------')
print('------------- Nick Bout - 1709217 - V1Q - Programming - HU -------------')
print('------------------------------------------------------------------------')

stations = [
    'Schagen',
    'Heerhugowaard',
    'Alkmaar',
    'Castricum',
    'Zaandam',
    'Amsterdam Sloterdijk',
    'Amsterdam Centraal',
    'Amsterdam Amstel',
    'Utrecht Centraal',
    '’s-Hertogenbosch',
    'Eindhoven',
    'Weert',
    'Roermond',
    'Sittard',
    'Maastricht'
]

### Begin simulation ###

## Begin Station ##
startStation = input('Wat is het beginstation: ')

# check if the station is not in the list
if not startStation in stations:
    print('Station niet gevonden,' +  stations[0] + 'is standaard geselecteerd')
    startStation = stations[0]

# set index of the station for later
startIndex = stations.index(startStation)



## End Station ##
endStation = input('Wat is het eindstation: ')

err = ''
endIndex = 0
# check if the station is in the list
if endStation in stations:
    # set endIndex for later
    endIndex = stations.index(endStation)

    # check if the end index is below or equal start index
    if endIndex <= startIndex:
        err = 'Station niet correct,' + stations[-1] + 'is standaard geselecteerd'
else:
    err = 'Station niet gevonden,' + stations[-1] + 'is standaard geselecteerd'

# If there is a error print it and select the last station by default
if err:
    print(err)
    endStation = stations[-1]
    endIndex = len(stations) - 1
print()


## Display Ticket ##

print('Het beginstation', startStation, 'is het', str(startIndex + 1) + 'e station in het traject')
print('Het eindstation', endStation, 'is het', str(endIndex + 1) + 'e station in het traject')
# use ternary operator to replace the ugly (s) after station(s)
print('De afstand bedraagt', endIndex - startIndex, 'stations' if endIndex - startIndex> 1 else 'station')
price = 5
print('De prijs van het kaartje is', (endIndex - startIndex) * price, 'euro.')
print()

## Adventure log ##
print('Jij stapt in de trein in: ', startStation)
for i in range(startIndex + 1, endIndex):
    print('-', stations[i])
print('Jij stapt uit in:', endStation)
print()
