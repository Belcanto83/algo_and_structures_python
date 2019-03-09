# 6.	Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

import string

alphabet = string.ascii_lowercase
print(alphabet)

n = int(input('Please enter number of letter in latin alphabet ("0" based): '))

if n <= 26:
    print(f'Letter "{alphabet[n]}" corresponds to your number')
else:
    print('Please enter number from 0 to 26')
