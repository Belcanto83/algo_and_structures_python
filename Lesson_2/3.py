"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""

number = int(input('Please enter natural number: '))

# Определим порядок введенного числа
order = 10
while number // order != 0:
    order *= 10
order //= 10

# Выполним перестановку цифр введенного числа
new_number = 0
new_order = 1
while order // 10 != 0 or order == 1:
    digit = number // order
    new_number += digit * new_order
    number -= digit * order
    order //= 10
    new_order = new_order * 10

print('New number: ', new_number)
