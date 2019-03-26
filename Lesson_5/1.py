"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""

from collections import namedtuple

n = int(input('Введите количество предприятий: '))

organizations_dict = {}

for i in range(n):
    organization_name = input(f'Введите название {i+1}-й огранизации: ')
    organization_profit = tuple(
        float(elem) for elem in input('Введите прибыль организации за 4 квартала (4 числа через пробел): ').split()
    )
    organizations_dict[organization_name] = organization_profit

Organizations = namedtuple('Organizations', organizations_dict)
organizations = Organizations(**organizations_dict)
print()
print('*'*100)
print(organizations)
print('*'*100)

profit_list = []
common_profit = 0
for organization in organizations:
    profit = sum(organization)
    common_profit += profit
    profit_list.append(profit)
average_profit = round(common_profit / len(organizations), 2)

s_high_profitable_orgs = f'Организации с годовой прибылью, выше или равной средней {average_profit}:\n'
s_low_profitable_orgs = f'Организации с годовой прибылью, ниже средней {average_profit}:\n'

i = 0
for organization in organizations:
    name = organizations._fields[i]
    if profit_list[i] >= average_profit:
        s_high_profitable_orgs += name + ' - ' + str(profit_list[i]) + '\n'
    else:
        s_low_profitable_orgs += name + ' - ' + str(profit_list[i]) + '\n'
    i += 1

print()
print(s_high_profitable_orgs, s_low_profitable_orgs, sep='\n')
