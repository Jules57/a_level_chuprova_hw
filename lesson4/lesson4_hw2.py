import random

fizzes = [random.randint(1, 20) for i in range(20)]
buzzes = [random.randint(1, 20) for j in range(20)]
totals = [random.randint(20, 60) for k in range(20)]

with open('fizzbuzzvalues4.2.txt', 'w') as infile:
    for i in range(20):
        fizz = str(fizzes[i]) + ' '
        buzz = str(buzzes[i]) + ' '
        total = str(totals[i]) + '\n'
        data = fizz + buzz + total
        infile.write(data)

with open('fizzbuzzvalues4.2.txt', 'r') as file:
    result = ''
    for line in file:
        fizz, buzz, final = list(map(int, line.split()))

        for i in range(1, final + 1):
            if not i % fizz and not i % buzz:
                result += 'FB '
            elif not i % fizz:
                result += 'F '
            elif not i % buzz:
                result += 'B '
            else:
                result = result + str(i) + ' '
        result += '\n'

with open('fizzbuzzresults4.2.txt', 'w') as file2:
    file2.write(result)







