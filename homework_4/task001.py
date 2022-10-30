# Вычислить число c заданной точностью d
#
# Пример:
# при d = 0.001, π = 3.142 10^(-1) ≤ d ≤10^(-10)

from decimal import Decimal

d = Decimal(input("Задайте точность числа: "))
num = Decimal(input("Введите число: "))

print(num.quantize(d))