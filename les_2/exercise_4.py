# Practice Exercises les 2
# 2_4 (if-else)
print('------------------------------------------------------------------------')
print('------------------------ Exercise 2_4 (if-else) ------------------------')
print('------------- Nick Bout - 1709217 - V1Q - Programming - HU -------------')
print('------------------------------------------------------------------------')
age = input('Geef je leeftijd: ')
passport = input('Nederlands paspoort (Ja/Nee): ')

# passport is converted to lower case to make it case-insensitive
if int(age) >= 18 and passport.lower() == 'ja':
    print('Gefeliciteerd, je mag stemmen!')
else:
    print('Nope jij mag niet')

print()
