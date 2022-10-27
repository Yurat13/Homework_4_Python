# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

with open('1.txt', 'r') as f1:
    polynomial_1 = f1.read()
print (f'1-st polynomial: {polynomial_1}')

with open('2.txt', 'r') as f2:
    polynomial_2 = f2.read()
print (f'2-nd polynomial: {polynomial_2}')
print ()

def find_koefs (polynomial):
    d = polynomial.split()
    st = []
    for i in d:
        if i != '+' and i!= '=' and i != '0':
            st.append(i)
    print (st)
    return st

lst1 = find_koefs(polynomial_1)
lst2 = find_koefs(polynomial_2)
sts = ''
for i, koef1 in enumerate (lst1):
    for k, koef2 in enumerate (lst2):
        if k == i:
            sts = str(koef1) + ' + ' + str(koef2) + ' + ' + sts
print(sts[:-3] + ' = 0')

