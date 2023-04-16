# Задача 0. Дан список, заполненный случайными числами от 0 до 10. Определите, является ли сумма всех элементов чётной.
import random

lenght = 7
numbers = [random.randint(0, 10) for index in range(lenght)]
sum = 0
for index in range(lenght):
    sum += numbers[index]
print(numbers)
print(sum)
if sum % 2 == 0:
    print('сумма четная')
else:
    print('сумма не четная')