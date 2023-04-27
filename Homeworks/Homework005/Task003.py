# Задача 3. Задайте список случайных чисел от 1 до 10. 
# Посчитайте, сколько всего совпадающих элементов есть в списке. Удалите все повторяющиеся элементы.

import random
numbers = [random.randint(1, 10) for i in range(10)]
print(numbers)
result = set(numbers)
print(list(result))
print(f"{len(numbers) - len(result)} повторяющихся элемента")