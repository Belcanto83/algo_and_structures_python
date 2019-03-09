# 3.	По введенным пользователем координатам двух точек вывести
# уравнение прямой вида y = kx + b, проходящей через эти точки.

p1 = input('Please enter first point (x, y) coordinates through a blank:')
p1_x, p1_y = p1.split(' ')
p1_x = float(p1_x)
p1_y = float(p1_y)

p2 = input('Please enter second point (x, y) coordinates through a blank:')
p2_x, p2_y = p2.split(' ')
p2_x = float(p2_x)
p2_y = float(p2_y)

if (p2_x == p1_x) and (p2_y == p1_y):
    print('You have entered the same point twice! It is not possible to draw the line!')
elif p2_x == p1_x:
    print(f'Equation of the line: x={p1_x}')
else:
    k = round((p2_y - p1_y) / (p2_x - p1_x), 2)
    b = round(p1_y - k * p1_x, 2)
    if b == 0:
        print(f'Equation of the line: y={k}x')
    elif b > 0:
        print(f'Equation of the line: y={k}x+{b}')
    else:
        print(f'Equation of the line: y={k}x-{abs(b)}')
