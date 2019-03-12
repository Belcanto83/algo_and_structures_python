"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""

number = int(input('Please enter natural number: '))

# Определим порядок введенного числа
order = 10
while number // order != 0:
    order *= 10
order //= 10
print('Порядок введенного числа: ', order)

# Подсчет четных и нечетных чисел
count_even = 0
count_uneven = 0
while order // 10 != 0 or order == 1:
    digit = number // order
    print(digit)
    if digit % 2 == 0:
        count_even += 1
    else:
        count_uneven += 1
    number -= digit * order
    order //= 10

print(f'Even numbers: {count_even}, uneven numbers: {count_uneven}')
