#5.	Пользователь вводит две буквы. Определить, на каких местах
# алфавита они стоят, и сколько между ними находится букв.

import string

alphabet = string.ascii_lowercase
print(alphabet)

letters = input('Please enter 2 lower case latin letters through a blank:')
a, b = letters.split(' ')
a_num = alphabet.find(a)
b_num = alphabet.find(b)
print(f'Number of letter "{a}" is {a_num}')
print(f'Number of letter "{b}" is {b_num}')
distance = abs(a_num - b_num) - 1
print(f'Between letter "{a}" and letter "{b}" is {distance} letters')
