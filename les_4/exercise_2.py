# Practice Exercises les 4
print('------------------------------------------------------------------------')
print('-------------------- Exercise 4_2 (files lezen)  -----------------------')
print('------------- Nick Bout - 1709217 - V1Q - Programming - HU -------------')
print('------------------------------------------------------------------------')
def getFileLines(fileName):
    file = open(fileName)
    return file.readlines()

lines = getFileLines('kaartnummers.txt')
for i in lines:
    # strip linebreak an split on ,
    data = i.replace('\n', '').split(',')
    print(data[1], 'heeft kaartnummer:', data[0])

print()
