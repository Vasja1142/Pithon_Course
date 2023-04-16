# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.

N = int(input("Введите любое положительное число: "))
array = []
if N > 0:
    array.insert(0, N - 1)
    array.insert(1, N)
    counter = 2
    for i in range(-N, N - 1):
        array.insert(counter, i)
        counter += 1
    print(array)

elif N == 0:
    array = [None, None, 0]
    print(array)
else:
    print("Данное число не является положительным!")