import time

# Practice Exercises les 4
print('------------------------------------------------------------------------')
print('------------------ Exercise 4_4 (files schrijven)  ---------------------')
print('------------- Nick Bout - 1709217 - V1Q - Programming - HU -------------')
print('------------------------------------------------------------------------')

# createFile
# creates file with write, if there is al ready a file with name it returns that one
#
# @param fileName || Name of the file
# return _io.TextIOWrapper || the file
def createFile(fileName):
    file = open(fileName, 'a')
    return file

file = createFile('hardlopers.txt')
name = input('Please enter your name: ')
curTime = time.strftime('%a %d %b %Y, %H:%M:%S, ')
file.write(curTime + name + '\n')
print('Bedankt voor het inschrijven.')


# close file
file.close()

print()
