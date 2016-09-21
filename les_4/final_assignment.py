import time
import os # we use os because we need the full path of the file (else it will break when we run it with program.py)

# Final assignment les 4
print('------------------------------------------------------------------------')
print('----------------------- Final assignment les 4  ------------------------')
print('------------- Nick Bout - 1709217 - V1Q - Programming - HU -------------')
print('------------------------------------------------------------------------')

# getStations
# reads lines from file and returns the stations
#
# @param String fileName || Name of the file that holds the stations
# @param Boolean canceled || If it needs to check for canceled rides || default False
# @return List stations || list with all stations from the file
def getStations(fileName, canceled = False):
    file = open(fileName)
    lines = file.readlines()
    stations = []
    for i in lines:
        if canceled:
            station = i.replace('\n', '').split(': ')[1] # remove line break
            stations.append(station)
        else:
            data = i.replace('\n', '').split(' - ') # remove line break
            stations.append({ 'time': data[0], 'station': data[1]})

    file.close()
    return stations

# createRidesFile
# creates file with updated train rides
#
# @param List stations || List with all stations/times
# @param List canceledStation || List with station names that should be canceled || default []
# @return String fileName || Name of the newly created file
def createRidesFile(stations, canceledStations = []):
    newStations = ''
    # loop through stations and add non canceled stations to newStations string
    for i in stations:
        if i['station'] not in canceledStations:
            newStations += i['time'] + ' - ' + i['station'] + '\n' # e.g. train_rides_20_09_2016.txt

    # create file name based on current date
    fileName = time.strftime(os.path.dirname(os.path.abspath(__file__)) + os.sep + 'rides' + os.sep + 'train_rides_%d_%m_%Y.txt')

    # Add the new stations to the file
    file = open(fileName, 'w')
    file.write(newStations)
    file.close()

    return fileName

# get the data
canceledStations = getStations(os.path.dirname(os.path.abspath(__file__)) + os.sep + 'train_rides_canceled.txt', True)
stations = getStations(os.path.dirname(os.path.abspath(__file__)) + os.sep + 'train_rides.txt')

# create the file (in te rides folder)
name = createRidesFile(stations, canceledStations)
print('New file with train rides for today created:', name)

print()
