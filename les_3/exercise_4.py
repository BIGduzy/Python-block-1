# Practice Exercises les 3
# 3_4 (functie met if)
print('------------------------------------------------------------------------')
print('------------------- Exercise 3_4 (functie met if)  ---------------------')
print('------------- Nick Bout - 1709217 - V1Q - Programming - HU -------------')
print('------------------------------------------------------------------------')
def new_password(oldPassword, newPassword):
    # check if digit for each char in newPassword check
    hasNumber = any(i.isdigit() for i in newPassword)
    return oldPassword != newPassword and len(newPassword) and hasNumber

print("hank, hank:", new_password("hank", "hank"), "(same password)") # false (same)
print("hank, harry:", new_password("hank", "harry"), "(to short)") # false (to short)
print("hank, A#@$JYjosad@#:", new_password("hank", "A#@$JYjosad@#"), "(no number)") # false (no number)
print("hank, topge1:", new_password("hank", "topge1")) # true
print()
