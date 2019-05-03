"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""

import random


def merge_sorting(m1, m2):
    i, j = 0, 0
    merge_m = []
    # Сравниваем элементы 2 исходных массивов попарно и добавляем минимальный из них в результирующий массив
    while i in range(len(m1)) and j in range(len(m2)):
        if m1[i] > m2[j]:
            merge_m.append(m2[j])
            j += 1
        else:
            merge_m.append(m1[i])
            i += 1
    # Прицепляем остаток, который уже отсортирован
    while i < len(m1):
        merge_m.append(m1[i])
        i += 1
    while j < len(m2):
        merge_m.append(m2[j])
        j += 1

    return merge_m


# a = (1, 3.2, 5, 6)
# b = [4]
# print(merge_sorting(a, b))
# print()

number = 25
initial_data = tuple(round(random.random() * 50, 2) for _ in range(number))
initial_array = []
for k in range(number):
    array = (initial_data[k],)
    initial_array.append(array)
print('Исходный массив: ', initial_data)

k = 0
while len(initial_array) > 1:
    initial_array[k:k + 2] = [merge_sorting(initial_array[k], initial_array[k + 1])]
    k += 1
    print(initial_array)
    if k > len(initial_array) - 2:
        k = 0

result = initial_array[0]
print('Результат сортировки: ', result)
