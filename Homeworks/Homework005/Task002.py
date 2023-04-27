# Задача 2. Дан список случайных чисел. Создайте список, в который попадают числа, 
# описывающие случайную возрастающую последовательность. Порядок элементов менять нельзя.

import random

def Function(numbers, numbers2):
    counter = 0
    for i in numbers:
        counter += 1
        if i > numbers2[-1]:
            numbers2.append(i)
            print(numbers2)
            Function(numbers[counter:], numbers2)
    numbers2.pop()

numbers = [random.randint(1, 10) for i in range(10)]
print(numbers)
for i in range(len(numbers)):
    numbers2 = []
    numbers2.append(numbers.pop(0)) 
    Function(numbers, numbers2)




# for i in numbers:
#     result = [i]
#     numbers2 = numbers[counter:]
#     for k in numbers2:
#         for j in numbers2:
#             if j > i: 
#                 i = j
#                 result.append(i)
#                 print(result)
#     counter += 1