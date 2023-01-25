"""Напишите программу, запрашивающую у пользователя целые числа, пока он не оставит строку ввода пустой.
После окончания ввода на экран должны быть выведены сначала все отрицательные числа, которые были введены, затем
нулевые и только после этого положительные. Внутри каждой группы числа должны отображаться в той последовательности,
в которой были введены пользователем. Например, если он ввел следующие числа: 3, -4, 1, 0, -1, 0 и -2, вывод должен
оказаться таким: -4, -1, -2, 0, 0, 3 и 1. Каждое значение должно отображаться на новой строке."""

number = input('Please, enter a number (press Enter to exit): ')

number_list = []
while number != '':
    number_list.append(int(number))
    number = input('Please, enter a number (press Enter to exit): ')

negatives = [elem for elem in number_list if elem < 0]
# I truly believe that comparison to zero in this case is more evident than [0 for elem in number_list if not elem]
zeros = [elem for elem in number_list if elem == 0]
positives = [elem for elem in number_list if elem > 0]

final_list = negatives + zeros + positives


for elem in final_list:
    print(elem)
