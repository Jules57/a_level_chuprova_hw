fizz = int(input('The first number: '))
buzz = int(input('The second number: '))
final = int(input('The third number: '))

for i in range(1, final+1):
    if i % fizz == 0 and i % buzz == 0:
        print('FB', end=' ')
    elif i % fizz == 0:
        print('F', end=' ')
    elif i % buzz == 0:
        print('B', end=' ')
    else:
        print(i, end=' ')
