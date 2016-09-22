# Practice Exercises les 5
print('------------------------------------------------------------------------')
print('--------------- Exercise 5_6 (two-dimensional-lists)  ------------------')
print('------------- Nick Bout - 1709217 - V1Q - Programming - HU -------------')
print('------------------------------------------------------------------------')

def averageStudent(studentGrades):
    grades = []
    for i in studentGrades:
        grades.append(sum(i) / len(i))

    return grades

def averageClass(studentGrades):
    grades = []
    for i in studentGrades:
        grades.append(sum(i) / len(i))

    return sum(grades) / len(grades)

studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]

print(averageStudent(studentencijfers))
print(averageClass(studentencijfers))

print()
