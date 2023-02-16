"""Напишите программу, которая, как и в предыдущем случае, будет запрашивать у пользователя целые числа и сохранять их
в виде списка. Индикатором окончания ввода значений также должен служить ноль. На этот раз необходимо вывести на экран
введенные значения в порядке убывания."""

CONTROL_VALUE = 0

value = int(input('Enter a number (enter 0 to exit): '))

value_list = []
while value:
    value_list.append(value)
    value = int(input('Enter a number(Enter 0 to exit): '))

if CONTROL_VALUE in value_list:
    value_list.remove(CONTROL_VALUE)

output = [x for x in sorted(value_list, reverse=True)]

for elem in output:
    print(elem)