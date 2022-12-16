# -*- coding: utf-8 -*-
"""homework_11.ipynb

Даны две функции:
f(x) = x^3 - 50x и g(x) = -x^4 + 88x^2 - 241   
Требуется:
1. Найти координаты точек пересечения
2. Построить графики функций в одной системе координат
3. Построить график функции пересечения
"""

from sympy import*
x = Symbol('x')
fx = x**3-50*x
gx = -1*x**4+88*x**2-241
fgx = fx - gx

"""1. Найти координаты точек пересечения"""

roots = solve(fgx)
roots

coordinates = {}
c = 1
for z in roots:
    coordinates[c] = {'x': round(N(z), 5), 'y': round(N(-1*z**4+88*z**2-241), 5)}
    c += 1
coordinates

"""2. Построить графики функций в одной системе координат"""

plot(fx, gx, x)

"""3. Построить график функции пересечения"""

plot(fgx, x)

"""Общий график"""

p = plot(fx, gx, fgx, show=false)
p[2].line_color = 'g'
p.show()