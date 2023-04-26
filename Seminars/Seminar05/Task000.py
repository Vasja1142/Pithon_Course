# Задача 0. С помощью анонимной функции найдите в списке на 15 элементов числа, кратные 5. Заполните список случайным
# образом числами от 1 до 100.
import random

Create_list = [random.randint(1, 100) for i in range(15)]
print(Create_list)
x = filter(lambda y: y % 5 == 0, Create_list)    
print(list(x))
