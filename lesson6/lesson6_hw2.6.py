"""Интернет-магазин предоставляет услугу экспресс-доставки для части своих товаров по цене $10,95 за первый товар
в заказе и $2,95 – за все последующие. Напишите функцию, принимающую в качестве единственного параметра количество
товаров в заказе и возвращающую общую сумму доставки. В основной программе должны производиться запрос количества
позиций в заказе у пользователя и отображаться на экране сумма доставки."""

FIRST_ITEM_DELIVERY = 10.95
NEXT_ITEM_DELIVERY = 2.95


def calculate_delivery_cost(qnty: int) -> float:
    if qnty == 1:
        total_cost = FIRST_ITEM_DELIVERY
    elif qnty > 1:
        total_cost = FIRST_ITEM_DELIVERY + (qnty - 1) * NEXT_ITEM_DELIVERY
    else:
        total_cost = 0
        print('Please, check the number of items and enter a positive value.')
    return total_cost


def main():
    items = int(input('Number of items: '))
    cost = calculate_delivery_cost(items)
    print(f'The delivery of {items} item(s) costs ${cost:.2f}.')


if __name__ == '__main__':
    main()
