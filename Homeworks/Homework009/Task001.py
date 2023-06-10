# Задача 1. Дан список элементов. Используя библиотеку NumPy, подсчитайте количество уникальных элементов в нём.
import numpy as np

numbers = np.random.randint(1, 10, 10)
num_uniq = np.unique(numbers)
print(f"Массив: {numbers}")
print(f"Уникальные элементы: {num_uniq}")
print(f"Количество уникальных элементов: {len(num_uniq)}")


