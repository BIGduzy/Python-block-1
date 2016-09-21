# Practice Exercises les 4
print('------------------------------------------------------------------------')
print('-------------------- Exercise 4_3 (files lezen)  -----------------------')
print('------------- Nick Bout - 1709217 - V1Q - Programming - HU -------------')
print('------------------------------------------------------------------------')
def getFileLines(fileName):
    file = open(fileName)
    print(type(file))
    lines = file.readlines()
    file.close()
    return lines

lines = getFileLines('kaartnummers.txt')
highestNumber = 0
index = 0
for i, value in enumerate(lines):
    # strip linebreak an split on ,
    data = value.replace('\n', '').split(',')
    number = int(data[0])
    if (number > highestNumber):
        highestNumber = number
        index = i

print('Deze file telt', len(lines), 'regels')
print('Het grootste kaartnummer is:', highestNumber, 'en dat staat op regel', index)
print()
