# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл,
# содержащий сумму многочленов.

from sympy import Symbol, collect
import re

def convert_line(line):
    line = re.sub(r'(\d)(x)', r'\1*\2', line)
    line = line.replace('^', '**')
    line = line[:-4:]
    return line

with open("polynomial.txt", "r") as file_1:
    pol_1 = file_1.readline()

with open("polynomial_2.txt", "r") as file_2:
    pol_2 = file_2.readline()

print(f"Первый многочлен: {pol_1}")
print(f"Второй многочлен: {pol_2}")

pol_1 = convert_line(pol_1)
pol_2 = convert_line(pol_2)

x = Symbol("x")

sum_line = str(collect(pol_1 + "+" + pol_2, x))
sum_line = sum_line.replace("**", "^")
sum_line = sum_line.replace("*", "")
sum_line += " = 0"

print(f"Сумма многочленов: {sum_line}")

with open("polynomial_sum.txt", "w") as file:
    file.write(sum_line + "\n")
