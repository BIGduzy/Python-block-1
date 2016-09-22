# Practice Exercises les 5
print('------------------------------------------------------------------------')
print('------------------ Exercise 5_1 (decision control)  --------------------')
print('------------- Nick Bout - 1709217 - V1Q - Programming - HU -------------')
print('------------------------------------------------------------------------')

# season
# Returns season of the month
#
# @param Int month || Index of the month
# @return String || Name of the season
def getSeason(month):
    # give season default Winter
    season = 'Winter'

    # boundary control
    if month > 12:
        month = 12
    elif month < 1:
        month = 1

    if month >= 3 and month <= 5: # 3-5 is spring
        season = 'Spring'
    elif month >= 6 and month <= 8: # 6-8 is summer
        season = 'Summer'
    elif month >= 9 and month <= 11: # 9-11 is summer
        season = 'Autumn'

    return season

for i in range(1, 13):
    print('Month: {0:2} is in {1}'.format(i, getSeason(i)))

print()
