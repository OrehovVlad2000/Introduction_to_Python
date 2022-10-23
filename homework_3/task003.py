# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.
#
#  Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.2

num_list = [1.1, 1.2, 3.1, 5, 10.01]
new_num_list = []

for i in range(len(num_list)):
    new_num_list.append(round(num_list[i] % 1, 2))

print(new_num_list)
print(max(new_num_list) - min(new_num_list))