# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
#
# Пример:
# k=2 => 2x^2 + 4x + 5 = 0 или x^2 + 5 = 0 или 10x = 0

import random

k = int(input("Введите натуральную степень k: "))
result_list = []
def rand_num(): return random.randint(0, 100)

for i in range(k, 1, -1):
    num = rand_num()
    if num and num != 1:
        result_list.append(f"{num}x^{i}")
    elif num == 1:
        result_list.append(f"x^{i}")

num = rand_num()
if num and num != 1:
    result_list.append(f"{num}x")
elif num == 1:
    result_list.append("x")

num = rand_num()
if num:
    result_list.append(f"{num}")

if len(result_list) == 0:
    result_line = "0"
else:
    result_line = " + ".join(result_list) + " = 0"

print(result_line)

with open("polynomial.txt", "w") as file:
    file.write(result_line + "\n")