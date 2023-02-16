import sys

filename = sys.argv[1]
file = open(filename, 'r')
total_text = []

for line in file:
    total_text.append(line[::-1].strip())

total_text = list(reversed(total_text))

for elem in total_text:
    print(f'{elem: >45}')
file.close()
