# Задача 3. Выведите число π с заданной точностью. Точность выводится в виде десятичной дроби.

import math
fraction = float(input('Введите точность числа пи ввиде десятичной дроби. Например: "0.001": '))
precision = 0
while fraction < 1:
    fraction *= 10
    precision += 1
print(round(math.pi, precision))