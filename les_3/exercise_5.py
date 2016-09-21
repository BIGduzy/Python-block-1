# Practice Exercises les 3
# 3_5 (functie met list-parameter en for-loop)
print('------------------------------------------------------------------------')
print('-------- Exercise 3_5 (functie met list-parameter en for-loop)  --------')
print('------------- Nick Bout - 1709217 - V1Q - Programming - HU -------------')
print('------------------------------------------------------------------------')
def kwadraten_som(intergers):
    sum = 0
    for i in intergers:
        if i > 0:
            sum += i ** 2

    return sum

print("kwadraten_som([4, 5, 3, -81]) == 50", kwadraten_som([4, 5, 3, -81]) == 50)
print("kwadraten_som([3, 4, 5, -81, 10]) == 150", kwadraten_som([3, 4, 5, -81, 10]) == 150)
print()
