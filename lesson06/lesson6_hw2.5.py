"""Представьте, что сумма за пользование услугами такси складывается из базового тарифа в размере $4,00 плюс $0,25 за
каждые 140 м поездки. Напишите функцию, принимающую в качестве единственного параметра расстояние поездки в километрах
и возвращающую итоговую сумму оплаты такси. В основной программе должен демонстрироваться результат вызова функции.

Подсказка. Цены на такси могут меняться со временем. Используйте константы для представления базового тарифа и
плавающей ставки, чтобы программу можно было легко обновлять при изменении цен."""

MIN_RATE = 4.0
MIN_DISTANCE = 0.14
RATE_PER_MIN_DISTANCE = 0.25


def get_taxi_rate(distance_km: float) -> float:
    dist_parts = distance_km / MIN_DISTANCE
    total_cost = MIN_RATE + dist_parts * RATE_PER_MIN_DISTANCE
    return total_cost


def main():
    dist = float(input('Distance in kilometers: '))
    cost = get_taxi_rate(dist)
    print(f'The cost of your journey is ${cost:.2f}.')


if __name__ == '__main__':
    main()
