# Final assignment les 6
print('------------------------------------------------------------------------')
print('----------------------- Final assignment les 5  ------------------------')
print('------------- Nick Bout - 1709217 - V1Q - Programming - HU -------------')
print('------------------------------------------------------------------------')

### PART ONE ###

# encode
# Encodes a string
#
# @param String string || The string that needs encoding
# @return String || The encodes string
def encode(string):
    code = ''
    for i in string:
        code += chr(ord(i) + 3)

    return code

# decode
# Decodes a string
#
# @param String string || The string that needs to be decoded
# @return String || The decoded string
def decode(string):
    code = ''
    for i in string:
        code += chr(ord(i) - 3)

    return code

name = 'Nick'
startStation = 'Amsterdam C'
endStation = 'Eindhoven'
code = encode(name + startStation + endStation)

print('Part one:')
print(name)
print(startStation)
print(endStation)
print(decode(code))
print(code)
print()



### PART TWO ###
listTypes = {
    'tuple': { 'ordered': True, 'mutable': False, 'iterable': True, 'double_values': True, },
    'dictionary': { 'ordered': False, 'mutable': True, 'iterable': True, 'double_values': False, },
    'set': { 'ordered': False, 'mutable': True, 'iterable': True, 'double_values': False, },
    'list': { 'ordered': True, 'mutable': True, 'iterable': True, 'double_values': True, },
}

print('Part two:')
print('| {0:10} | {1:10} | {2:10} | {3:10} | {4:27} |'.format(
        'list types',
        'Geordend',
        'Muteerbaar',
        'Iterable',
        'Dubbele waarden toegestaan'
    ))
print('-' * 83)
for key, value in listTypes.items():
    print('| {0:10} | {1:^10} | {2:^10} | {3:^10} | {4:^27} |'.format(
        key.capitalize(),
        str(value['ordered']),
        str(value['mutable']),
        str(value['iterable']),
        str(value['double_values'])
    ))

print()
