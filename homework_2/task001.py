# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

num = input("Введите вещественное число: ")
count = 0
for i in range(len(num)):
    if num[i] != "," and num[i] != ".":
        count += int(num[i])
    else:
        continue
print(count)