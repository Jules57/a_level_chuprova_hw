import sys

filename = sys.argv[1]
file = open(filename, 'r')

for line in file:
    print(line, end='')
file.close()
