"""В данном упражнении вам предстоит разработать программу, в которой у пользователя будет запрошен список слов, пока он
не оставит строку ввода пустой. После этого на экране должны быть показаны слова, введенные пользователем, но без
повторов, – каждое по одному разу. При этом слова должны быть отображены в том же порядке, в каком их вводили с
клавиатуры. Например, если пользователь на запрос программы введет следующий список слов:
first second first third second программа должна вывести: first second third"""


word = input('Please, enter a word (press Enter to exit): ')
word_list = []

while word:
    word_list.append(word)
    word = input('Please, enter a word (press Enter to exit): ')

final_list = []
for word in word_list:
    if word not in final_list:
        final_list.append(word)

for word in final_list:
    print(word)
