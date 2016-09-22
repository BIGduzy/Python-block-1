# Practice Exercises les 5
print('------------------------------------------------------------------------')
print('--------------------- Exercise 5_5 (while-loop)  -----------------------')
print('------------- Nick Bout - 1709217 - V1Q - Programming - HU -------------')
print('------------------------------------------------------------------------')

while True:
    word = input('Geef een string van vier letters: ')
    if len(word) == 4:
        break
    else:
        print(word, 'heeft', len(word), 'letters')

print('Inlezen van correcte string:', word, 'is geslaagd')

print()
