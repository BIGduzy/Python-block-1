# Practice Exercises les 3
# 3_3 (functie met if)
print('------------------------------------------------------------------------')
print('------------------- Exercise 3_3 (functie met if)  ---------------------')
print('------------- Nick Bout - 1709217 - V1Q - Programming - HU -------------')
print('------------------------------------------------------------------------')
def lang_genoeg(lengte):
    print("Je bent lang genoeg voor de attractie!") if lengte >= 120 else print('Sorry je bent te klein!')

print('100:', end = ' ')
lang_genoeg(100)
print('120:', end = ' ')
lang_genoeg(120)
print('130:', end = ' ')
lang_genoeg(130)
print()
