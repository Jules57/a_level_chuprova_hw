import sys

filename = sys.argv[1]
with open(filename, 'r') as file:
    for line in file:
        values = line.split()
        fizz = int(values[0])
        buzz = int(values[1])
        final = int(values[2])

        result = ''
        for i in range(1, final + 1):
            if i % fizz == 0 and i % buzz == 0:
                result += 'FB '
            elif i % fizz == 0:
                result += 'F '
            elif i % buzz == 0:
                result += 'B '
            else:
                result = result + str(i) + ' '

        filename2 = sys.argv[2]
        with open(filename2, 'a') as file2:
            result += '\n'
            file2.write(result)
