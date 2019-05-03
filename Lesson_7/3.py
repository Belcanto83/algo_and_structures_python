"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках
"""

import random


def qsort_inplace(lst, start=0, end=None):
    """
    Отсортировать список методом быстрой сортировки
    """
    def subpart(lst, start, end, pivot_index):
        # перемещаем случайно выбранный "опорный" элемент в начало массива
        lst[start], lst[pivot_index] = lst[pivot_index], lst[start]
        # выбранное "опорное" значение
        pivot = lst[start]
        right_pointer = end
        left_pointer = start + 1

        while left_pointer <= right_pointer:
            if lst[left_pointer] >= pivot > lst[right_pointer]:
                lst[left_pointer], lst[right_pointer] = lst[right_pointer], lst[left_pointer]
                left_pointer += 1
                right_pointer -= 1
            elif lst[left_pointer] < pivot:
                left_pointer += 1
            elif lst[right_pointer] >= pivot:
                right_pointer -= 1

        lst[start], lst[right_pointer] = lst[right_pointer], lst[start]

        return right_pointer

    if end is None:
        end = len(lst) - 1
    if end - start < 1:
        return

    pivot_index = random.randint(start, end)
    # x - новый индекс "опорного" элемента после сортировки
    x = subpart(lst, start, end, pivot_index)
    qsort_inplace(lst, start, x - 1)
    qsort_inplace(lst, x + 1, end)

    return lst


ary = [54, 1, 2, 3, 52, 3, 1, 2, 3, 5, 3, 67, 3, 2, 543]
print(ary)
print(qsort_inplace(ary))
print('*'*50)


m = int(input('Введите целое число "m" для генерации массива случайных вещественных чисел, размером "2m+1": '))
array = list(round(random.random() * 50, 2) for _ in range(2*m+1))
print(array)
# print(qsort_inplace(array))
# print('Медиана массива: ', array[(2*m+1)//2])


# Решение задачи итеративное (через цикл)
"""
def median(array):
    modified_array = array[:]

    def find_minimum(arr):
        min_ind = 0
        i = min_ind
        minimum = arr[min_ind]
        for item in arr:
            if item < minimum:
                minimum = item
                min_ind = i
            i += 1
        return min_ind

    for i in range(len(array)//2+1):
        ind = find_minimum(modified_array)
        median_item = modified_array.pop(ind)

    return median_item
"""


# Решение задачи рекурсивное
def median(array, counter=0):
    modified_array = array[:]

    def find_minimum(arr):
        min_ind = 0
        i = min_ind
        minimum = arr[min_ind]
        for item in arr:
            if item < minimum:
                minimum = item
                min_ind = i
            i += 1
        return min_ind

    ind = find_minimum(modified_array)
    min_item = modified_array.pop(ind)
    if len(modified_array) > counter:
        counter += 1
        return median(modified_array, counter)
    else:
        return min_item


print('Медиана массива [test]: ', median(array))

print(qsort_inplace(array))
print('Медиана массива: ', array[(2*m+1)//2])
