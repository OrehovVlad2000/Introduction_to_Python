# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.

import random

num_list = [random.randint(0, 5) for i in range(7)]
print(num_list)
sort_list = []
for i in range(len(num_list)):
    count = 0
    for j in range(len(num_list)):
        if num_list[i] == num_list[j]:
            count += 1
    if count == 1:
        sort_list.append(num_list[i])

print(sort_list)