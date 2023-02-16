"""Напишите программу, которая будет запрашивать у пользователя целочисленные значения и сохранять их в виде списка.
Индикатором окончания ввода значений должен служить ноль. Затем программа должна вывести на экран все введенные
пользователем числа (кроме нуля) в порядке возрастания – по одному значению в строке. Используйте для сортировки
либо метод sort, либо функцию sorted."""

CONTROL_VALUE = 0

value = int(input('Enter a number (enter 0 to exit): '))

value_list = []
while value:
    value_list.append(value)
    value = int(input('Enter a number(Enter 0 to exit): '))

if CONTROL_VALUE in value_list:
    value_list.remove(CONTROL_VALUE)

output = [x for x in sorted(value_list)]

for elem in output:
    print(elem)
