# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

num = int(input("Введите число: "))
i = 2
num_list = []
old = num
while i <= num:
    if num % i == 0:
        num_list.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f"Список простых множителей числа {old}: {num_list}")
