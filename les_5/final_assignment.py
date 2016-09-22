# Final assignment les 5
print('------------------------------------------------------------------------')
print('----------------------- Final assignment les 5  ------------------------')
print('------------- Nick Bout - 1709217 - V1Q - Programming - HU -------------')
print('------------------------------------------------------------------------')

stations = (
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
)

def getStartStation():
    station = input('Wat is je beginstation?: ')

    # First station can not be last in list because endstation needs to have a higher index
    # TODO: better error for last in list
    while station not in stations or station == stations[-1]:
        print('Station niet gevonden!')
        station = input('Wat is je beginstation?: ')

    return { 'name': station, 'index': stations.index(station)}

def getEndStation(startIndex):
    station = input('Wat is je eindstation?: ')

    while station not in stations or stations.index(station) <= startIndex:
        print('Eindstation niet correct')
        station = input('Wat is je eindstation?: ')

    return { 'name': station, 'index': stations.index(station)}

def displayTicket(startStation, endStation):
    startName = startStation['name']
    startIndex = startStation['index']
    endName = endStation['name']
    endIndex = endStation['index']
    numStations = endIndex - startIndex

    ## Ticket stuff ##
    print('Het beginstation {0} is het {1}e station in het traject'.format(startName, startIndex + 1))
    print('Het beginstation {0} is het {1}e station in het traject'.format(endName, endIndex + 1))
    # use ternary operator to replace the ugly (s) after station(s)
    print('De afstand bedraagt {0} station{1}'.format(numStations, 's' if numStations > 1 else ''))
    price = 5
    print('De prijs van het kaartje is {0} euro.'.format(numStations * price))
    print()

    ## Adventure log ##
    print('Jij stapt in de trein in:', startName)
    for i in range(startIndex + 1, endIndex):
        print('-', stations[i])
    print('Jij stapt uit in:', endName)


### Begin simulation ###
## get stations ##
startStation = getStartStation()
endStation = getEndStation(startStation['index'])

## Display Ticket ##
displayTicket(startStation, endStation)

print()
