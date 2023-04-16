# Задача 1:Создайте кортеж, заполненный случайными числами.
# Напишите метод, который заменяет элемент в кортеже по заданному индексу другим случайным числом.

import random
numbers = tuple(random.randint(1, 10) for _ in range(10))

print(numbers)

def replacing_an_element(numbers):
    index = int(input("Введите индекс числа: "))
    return numbers[:index] + (random.randint(1, 10), ) + numbers[index + 1:]
    

print(replacing_an_element(numbers))