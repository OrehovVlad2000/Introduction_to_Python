# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

num = int(input("Выедите число: "))

fibo = [0, 1]
for i in range(2, num + 1):
    fibo.append(fibo[i - 1] + fibo[i - 2])

nega_fibo = []

for i in range(1, len(fibo)):
    nega_fibo.append((-1) ** (i + 1) * fibo[i])

nega_fibo = nega_fibo[::-1]

nega_fibo.extend(fibo)
print(nega_fibo)