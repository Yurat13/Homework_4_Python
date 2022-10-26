# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
k = int(input('Введите степень многочлена k = '))
koefs = []
for i in range (0, k + 1):
    i = randint (0, 100)
    koefs.append(i)
print (koefs)

# st = ''
# n = len(koefs)
# for koef in koefs:
#     if n - 1 != 0:
#         st = str(st) + str(koef) + 'x^' + str(n - 1) + ' + '
#         n = n - 1
#     else:
#         st = str(st) + str(koef) + 'x'
# print(st + " = 0")


# koefs = [3, 0, 4, 5]

st = ''
n = len(koefs) - 1
for i, koef in enumerate (koefs):
    if koef == 0:
        st = st
    elif n - i != 0:
        st = st + str(koef) + 'x^' + str(n - i) + ' + '
        # n = n - 1
    else:
        st = str(st) + str(koef)
    


print(st + " = 0")