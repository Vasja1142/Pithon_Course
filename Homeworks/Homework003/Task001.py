# Задача 1. Создайте список. Запишите в него N первых элементов последовательности Фибоначчи.

number = int(input("Введите количество элементов Фибоначчи: "))
fibonatti = []
for i in range(number):
    if i < 2:
        fibonatti.append(1)
    else:
        fibonatti.append(fibonatti[i-1] + fibonatti[i-2])
print(fibonatti)