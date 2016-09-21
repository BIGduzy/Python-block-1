# Final assignment les 3
print('------------------------------------------------------------------------')
print('----------------------- Final assignment les 3  ------------------------')
print('------------- Nick Bout - 1709217 - V1Q - Programming - HU -------------')
print('------------------------------------------------------------------------')

# standaardtarief
# Calculates standard price
#
# @param Int afstandKM || Distance in kilometers
def standaardtarief(afstandKM):
    # if distance is less or equal than 0 the standard price is always 0
    if afstandKM <= 0:
        return 0

    # a distance greater than 50 kilometers has a different
    if afstandKM > 50:
        return 15 + 0.60 * afstandKM
    else:
        return 0.80 * afstandKM

# ritprijs
# Calculates price with discount based on age
#
# @param Int leeftijd || leeftijd of traveler
# @param Boolen weekendrit || if is weekendrit
# @param Int afstandKM || Distance in kilometers
def ritprijs(leeftijd, weekendrit, afstandKM):
    price = standaardtarief(afstandKM)

    # less than 12 or greater than 64
    if leeftijd < 12 or leeftijd > 64:
        # in weekend
        if weekendrit:
            price *= 0.65 # 35% discount
        else:
            price *= 0.7 # 30% discount
    # 12 - 64 in weekend
    elif weekendrit:
        price *= 0.6 # 40% discount

    return round(price, 2)

# test case
print('Test case:')
# we use format to display 2 digits
print('Not weekend')
print('11 years, 55 km:', '{:.2f}'.format(ritprijs(11, False, 55)))
print('12 years, 55 km:', '{:.2f}'.format(ritprijs(12, False, 55)))
print('64 years, 55 km:', '{:.2f}'.format(ritprijs(64, False, 55)))
print('65 years, 55 km:', '{:.2f}'.format(ritprijs(65, False, 55)))
print('Weekend')
print('11 years, 55 km:', '{:.2f}'.format(ritprijs(11, True, 55)))
print('12 years, 55 km:', '{:.2f}'.format(ritprijs(12, True, 55)))
print('64 years, 55 km:', '{:.2f}'.format(ritprijs(64, True, 55)))
print('65 years, 55 km:', '{:.2f}'.format(ritprijs(65, True, 55)))
print('Other')
print('Negative distance:', '{:.2f}'.format(ritprijs(11, True, -10)))
print('12 years, 44 km:', '{:.2f}'.format(ritprijs(12, True, 40)))
print('Negative age:', '{:.2f}'.format(ritprijs(-10, True, 55)))
print()
