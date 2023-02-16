number = int(input('Number: '))
digit_place = 1

if number == 0:
    print('The digit place is 1, the multiplier is 0.')

while number != 0:
    multiplier = number % 10
    print(f'The digit place is {digit_place}, the multiplier is {multiplier}.')
    number = number // 10
    digit_place *= 10
