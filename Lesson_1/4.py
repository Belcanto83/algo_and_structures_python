"""
4.	Написать программу, которая генерирует в указанных пользователем границах
●	случайное целое число,
●	случайное вещественное число,
●	случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f',
то вводятся эти символы. Программа должна вывести на экран любой
символ алфавита от 'a' до 'f' включительно.
"""

import random

print('Generation of integer random number:')
limits = input('Please enter Min and Max integer values through a blank: ')
Min, Max = limits.split(' ')
Min = int(Min)
Max = int(Max)
print('Random number from your range: ', random.randint(Min, Max))

print('Generation of real random number:')
limits = input('Please enter Min and Max real values through a blank: ')
Min, Max = limits.split(' ')
Min = float(Min)
Max = float(Max)
print('Random number from your range: ', round(random.uniform(Min, Max), 2))

print('Generation of random character:')
limits = input('Please enter Min and Max values through a blank: ')
Min, Max = limits.split(' ')
ls = [chr(x) for x in range(ord(Min), ord(Max)+1)]
print(ls)
print(random.choice(ls))
