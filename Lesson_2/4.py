"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""

n = int(input('Please enter number of elements for geometric progression: '))
b1 = 1.0
q = -0.5


def geom_progr_member(m1, mult, qty):
    if qty > 2:
        return geom_progr_member(m1, mult, qty - 1) * mult
    else:
        if qty == 2:
            return m1 * mult
        else:
            return m1


geom_pr = ''
sum_pr = 0
for i in range(1, n+1):
    geom_pr += str(geom_progr_member(b1, q, i)) + ' '
    sum_pr += geom_progr_member(b1, q, i)
print('Geom. progression: ', geom_pr)
print('Sum: ', sum_pr)
