"""
7.	По длинам трех отрезков, введенных пользователем, определить возможность
существования треугольника, составленного из этих отрезков. Если такой
треугольник существует, то определить, является ли он
разносторонним, равнобедренным или равносторонним.
"""

l1 = float(input('Please enter first length: '))
l2 = float(input('Please enter second length: '))
l3 = float(input('Please enter third length: '))

if (l1 + l2) > l3 and (l1 + l3) > l2 and (l2 + l3) > l1:
    print('It is possible to build triangle!')
    if l1 == l2 and l2 == l3:
        print('Triangle is equilateral!')
    elif (l1 == l2 and l3 != l1) or (l2 == l3 and l1 != l2) or (l1 == l3 and l2 != l1):
        print('Triangle is isosceles!')
    else:
        print('Triangle is versatile!')
else:
    print('It is impossible to build triangle!')
