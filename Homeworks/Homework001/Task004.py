# Задача 4. Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.

num = int(input('Введите любое число: '))
array = []
index = 0
if num > 0:
    for i in range(2, num + 1, 2):
        array.insert(index, i)
        index += 1
else:
    for i in range(0, num - 1, -2):
        array.insert(index, i)
        index += 1
print(f"Все четные числа от 1 до {num}: {array}")