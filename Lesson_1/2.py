# 2. Выполнить логические побитовые операции "И", "ИЛИ" и др.
# над числами 5 и 6. Выполнить
# над числом 5 побитовый сдвиг вправо и влево на два знака.

num_1 = int(input('Please enter first number:', ))
num_2 = int(input('Please enter second number:', ))

print('Binary "AND":', num_1 & num_2)
print(f'Binary "OR": {num_1 | num_2}')
print(f'Binary shift of {num_1} on 2 digits to the right: {num_1 >> 2}')
print(f'Binary shift of {num_1} on 2 digits to the left: {num_1 << 2}')
