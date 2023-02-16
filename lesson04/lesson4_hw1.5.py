"""Собственным делителем числа называется всякий его делитель, отличный от самого числа. Напишите функцию, которая
будет возвращать список всех собственных делителей заданного числа. Само это число должно передаваться в функцию в виде
единственного аргумента. Результатом функции будет перечень собственных делителей числа, собранных в список.
Основная программа должна демонстрировать работу функции, запрашивая у пользователя число и выводя на экран список
его собственных делителей. Программа должна запускаться только в том случае, если она не импортирована в виде модуля
в другой файл."""


def get_dividers(num: int) -> list:
    dividers = []
    for i in range(1, num//2+1):
        if not num % i:
            dividers.append(i)
    return dividers


if __name__ == "__main__":
    number = int(input('Enter a number to examine its dividers: '))
    divider_list = get_dividers(number)
    print(f'The dividers of {number} are {divider_list}.')