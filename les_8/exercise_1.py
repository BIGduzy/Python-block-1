import json
import xmltodict

# Practice Exercises les 8
print('------------------------------------------------------------------------')
print('--------------- Exercise 8_1 (XML-bestanden schrijven)  ----------------')
print('------------- Nick Bout - 1709217 - V1Q - Programming - HU -------------')
print('------------------------------------------------------------------------')

xml = xmltodict.parse(open('products.xml', 'rb'))
for i in xml['artikelen']['artikel']:
    print(i['@nummer'], i['code'], i['naam'], i['voorraad'], i['prijs'])

print()
