"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
"""


def perform_operation(num1, num2, operation):

    operation_control = False
    while not operation_control:
        operation_control = operation == '+' or operation == '-' or operation == '*' or operation == '/' or \
                            operation == '0'
        if not operation_control:
            print('Please choose a right operation!')
            if num2 != 0:
                operation = input('Please choose operation over entered numbers: "+", "-", "*", "/", "0"-exit: ')
            else:
                operation = input('Please choose operation over entered numbers: "+", "-", "*", "0"-exit: ')

    if operation == '+':
        return f'Result: {round(num1 + num2, 2)}'
    elif operation == '-':
        return f'Result: {round(num1 - num2, 2)}'
    elif operation == '*':
        return f'Result: {round(num1 * num2, 2)}'
    elif operation == '/':
        if num2 != 0:
            return f'Result: {round(num1 / num2, 2)}'
        else:
            print('It is impossible to divide by zero! Please choose another operation')
            operation = input('Please choose operation over entered numbers: "+", "-", "*", "0"-exit: ')
            return perform_operation(num1, num2, operation)
    else:
        return 'exit'


while True:
    a, b = input('Please enter two numbers through a blank: ').split()
    a, b = float(a), float(b)

    if b != 0:
        your_operation = input('Please choose operation over entered numbers: "+", "-", "*", "/", "0"-exit: ')
    else:
        your_operation = input('Please choose operation over entered numbers: "+", "-", "*", "0"-exit: ')

    result = perform_operation(a, b, your_operation)
    print(result)

    if result == 'exit':
        break
