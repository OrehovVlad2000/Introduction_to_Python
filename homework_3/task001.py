# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
#
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

num_list = [random.randint(1, 10) for i in range(5)]
sum = 0
print(num_list)

for i in range(1, len(num_list), 2):
    sum += num_list[i]

print(sum)