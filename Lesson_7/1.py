"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""

import random


def bubble_sorting(array):
    a = list(array)
    n = 1
    while n < len(a):
        is_sorted = False
        for i in range(len(a)-n):
            if a[i] < a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                is_sorted = True
        if not is_sorted:
            break
        n += 1
    return a


number = 25
initial_array = tuple(random.randint(-100, 100) for _ in range(number))

print(initial_array)
print(bubble_sorting(initial_array))
