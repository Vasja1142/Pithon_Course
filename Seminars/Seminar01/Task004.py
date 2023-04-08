# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

num = int(input('Введите любое число: '))
if(num > 0):
    for value in range(-num, num + 1):
        print(value)
else:
    for value in range(-num, num -1, -1):
        print(value)
