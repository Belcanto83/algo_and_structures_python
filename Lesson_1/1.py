# 1.	Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

number = int(input('Введите трехзначное число: '))

first_digit = number // 100
second_digit = (number % 100) // 10
third_digit = (number % 100) % 10
print(first_digit, second_digit, third_digit)

print('Сумма чисел:', first_digit + second_digit + third_digit)
print('Произведение чисел:', first_digit * second_digit * third_digit)
