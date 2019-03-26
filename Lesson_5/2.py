"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

hex_num_1 = list(input('Пожалуйста, введите первое шестнадцатеричное число: '))
hex_num_2 = list(input('Пожалуйста, введите второе шестнадцатеричное число: '))
print(hex_num_1, hex_num_2)


def hex_sum(num1, num2):
    from collections import deque

    n1 = deque(num1)
    n2 = deque(num2)

    hex_order = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f')

    i = 0
    n1.reverse()
    number_1 = n1[i]

    n2.reverse()
    number_2 = n2[i]

    result = deque()
    remember_category = False
    while number_1 in n1 or number_2 in n2 or remember_category:
        index = (hex_order.index(number_1) + hex_order.index(number_2)) % 16
        new_hex_number = hex_order[index]

        if index < 15 and remember_category:
            new_hex_number = hex_order[index + 1]
            remember_category = False
        elif index == 15 and remember_category:
            new_hex_number = hex_order[0]
            remember_category = True
        else:
            remember_category = False

        if (hex_order.index(number_1) + hex_order.index(number_2)) // 16:
            remember_category = True

        result.appendleft(new_hex_number)

        i += 1
        if i < len(n1):
            number_1 = n1[i]
            number_1 = number_1.lower()
        else:
            number_1 = '0'
        if i < len(n2):
            number_2 = n2[i]
            number_2 = number_2.lower()
        else:
            number_2 = '0'

    result = list(result)

    return result


print('Результат сложения: ', hex_sum(hex_num_1, hex_num_2))
