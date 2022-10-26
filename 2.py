# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('Enter number N = '))
lst = []
i = 2

while i <= n:
    if n % i == 0:
        lst.append(i)
        n = n / i
    else: i += 1
print(f'Простые множители числа: {lst}')
