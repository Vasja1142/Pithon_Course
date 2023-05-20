# Задача 1. Дан список случайных элементов. Проверьте, что все его элементы уникальны.

import random
numbers = [random.randint(1, 10) for i in range(5)]
numbers2 = set(numbers)

print(numbers, len(numbers) == len(numbers2))