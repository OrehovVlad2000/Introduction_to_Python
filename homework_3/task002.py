# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
#
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random

num_list = [random.randint(1, 10) for i in range(5)]
print(num_list)

sum_list = []

for i in range((len(num_list) + 1) // 2):
    sum_list.append(num_list[i] + num_list[-i - 1])

print(sum_list)