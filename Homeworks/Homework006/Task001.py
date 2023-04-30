# Задача 1. Дано натуральное число N. Найдите значение выражения N + NN + NNN, N может быть любой длины.

num = input("Введите натуральное число: ")
num2 = num*2
num3 = num*3
result = int(num) + int(num2) + int(num3)
print("Ответ:", result)