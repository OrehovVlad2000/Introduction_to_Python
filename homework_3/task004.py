# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

num = int(input("Введите число: "))

bin_num = bin(num)
print(bin_num[2:])
