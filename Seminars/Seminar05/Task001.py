# Задача 1. На вход подаётся четырёхзначное число. Получите список, состоящий из цифр данного числа, увеличенных на 10.

def Calculation(num):
    num = str(num)
    array = []
    for i in num:
        array.append(int(i) + 10)
    return array


number = int(input("Введите четырехзначное число: "))
Calculation(number)
