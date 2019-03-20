"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""

import timeit

# Поиск НОД. 1)Рекурсия без мемоизации


def gcd_recursion(a, b):
    if b == 0:
        return a
    return gcd_recursion(b, a % b)


# Поиск НОД. 2)Рекурсия с мемоизацией


def memorize(func):
    def wrapper(a, b, memory={}):
        keys = [str(a) + ':' + str(b), str(b) + ':' + str(a)]
        for key in keys:
            result = memory.get(key)
            if result is not None:
                break
        if result is None:
            result = func(a, b)
            for key in keys:
                memory[key] = result
        return result
    return wrapper


@memorize
def gcd_recursion_memo(a, b):
    if b == 0:
        return a
    return gcd_recursion_memo(b, a % b)


# Поиск НОД. 3)Цикл без мемоизации


def gcd_loop(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Поиск НОД. 4)Цикл с мемоизацией


@memorize
def gcd_loop_memo(a, b):
    while b != 0:
        a, b = b, a % b
    return a


m, n = 104478, 125680

print()

print('Время работы алгоритма через рекурсию без мемоизации: ',
      timeit.timeit('gcd_recursion(m, n)', setup='from __main__ import gcd_recursion, m, n')
      )

print('Время работы алгоритма через цикл без мемоизации: ',
      timeit.timeit('gcd_loop(m, n)', setup='from __main__ import gcd_loop, m, n')
      )

print()

print('Время работы алгоритма через рекурсию с мемоизацией: ',
      timeit.timeit('gcd_recursion_memo(m, n)', setup='from __main__ import gcd_recursion_memo, m, n')
      )

print('Время работы алгоритма через цикл с мемоизацией: ',
      timeit.timeit('gcd_loop_memo(m, n)', setup='from __main__ import gcd_loop_memo, m, n')
      )

print()

res = gcd_recursion_memo(m, n)
print(f'НОД чисел {m} и {n}: {res}')


############################################################################

# РЕЗУЛЬТАТЫ ЗАМЕРОВ ВРЕМЕНИ ВЫПОЛНЕНИЯ РАЗНЫХ АЛГОРИТМОВ:


# Время работы алгоритма через рекурсию без мемоизации:  4.230804898000001
# Время работы алгоритма через цикл без мемоизации:  2.4987621970000005
#
# Время работы алгоритма через рекурсию с мемоизацией:  2.710181577
# Время работы алгоритма через цикл с мемоизацией:  2.687852381000001

############################################################################
