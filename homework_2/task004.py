#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов
# на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

import random

num = int(input("Введите количество элементов списка: "))

num_list = [random.randint(-num, num) for i in range(num)]

position = open('file.txt', 'r')
my_lines = position.readlines()
count = 1

for i in range(len(my_lines)):
    pos = int(my_lines[i])
    if -num < pos < num:
        count *= num_list[pos]
    else:
        continue
position.close()
print(count)
