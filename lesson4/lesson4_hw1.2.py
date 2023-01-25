"""При анализе собранных по результатам научных экспериментов данных зачастую возникает необходимость избавиться от
экстремальных значений, прежде чем продолжать двигаться дальше. Напишите функцию, создающую копию списка с исключенными
из него n наибольшими и наименьшими значениями и возвращающую ее в качестве результата. Порядок следования элементов
в измененном списке не обязательно должен в точности совпадать с источником.
В основной программе должна быть продемонстрирована работа вашей функции. Для начала попросите пользователя ввести
целые числа, затем соберите их в список и вызовите написанную вами ранее функцию. Выведите на экран измененную версию
списка вместе с оригинальной. Если пользователь введет менее четырех чисел, должно быть отображено
соответствующее сообщение об ошибке."""


def edit_values(original_list: list) -> list:
    temp_list = original_list[::]
    max_value = max(temp_list)
    min_value = min(temp_list)
    temp_list.remove(max_value)
    temp_list.remove(min_value)
    return temp_list


value = int(input('Enter a value (0 to exit):  '))

values_list = []
while value:
    values_list.append(value)
    value = int(input('Enter a value (0 to exit):  '))


if len(values_list) > 4:
    edited_list = edit_values(values_list)
    print(f"Processed values are {', '.join(map(str, edited_list))}.")
    print(f"Original values are {', '.join(map(str, values_list))}.")
else:
    print('We need more values for accurate calculations. Please enter more values.')
