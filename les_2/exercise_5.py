# Practice Exercises les 2
# 2_5 (for + if)
print('------------------------------------------------------------------------')
print('------------------------ Exercise 2_5 (for + if) -----------------------')
print('------------- Nick Bout - 1709217 - V1Q - Programming - HU -------------')
print('------------------------------------------------------------------------')

text = "Guido van Rossum heeft programmeertaal Python bedacht."
print(text)
for i in text:
    # check if the letter (i) is a vowel bij checking if it is in the vowel list
    if i in ['a', 'e', 'i', 'o', 'u']:
        # The end argument makes sure to print in one line, this makes it easier to read
        print(i, end=" ")

print()
