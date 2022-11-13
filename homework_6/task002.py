# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности, список повторяемых
# и убрать дубликаты из заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и [1, 3, 5] и [1, 2, 5, 3, 10]

num_list = [1, 2, 3, 5, 1, 5, 3, 10]
print(num_list)
sort_list = []
sort_list_2 = []

for i in range(len(num_list)):
    count = 0
    for j in range(len(num_list)):
        if num_list[i] == num_list[j]:
            count += 1
    if count == 1:
        sort_list.append(num_list[i])

print(sort_list)

for i in range(len(num_list)):
    count = 0
    for j in range(len(num_list)):
        if num_list[i] == num_list[j]:
            count += 1
    if count > 1:
        if num_list[i] not in sort_list_2:
            sort_list_2.append(num_list[i])

print(sort_list_2)

num_list = list(set(num_list))
print(num_list)