# Задача 3. Создайте двумерный массив случайного размера. Найдите индексы максимального и минимального элементов в нём.
# Выведите элементы главной диагонали матрицы в виде одномерного массива.

import numpy as np

array = np.random.randint(0, 100, (np.random.randint(1, 10), np.random.randint(1, 10)))
max_num = np.unravel_index(np.argmax(array, axis=None), array.shape)
min_num = np.unravel_index(np.argmin(array, axis=None), array.shape)
diag = np.diag(array)
print(array)
print(f"Индекс максимального значения: {max_num}")
print(f"Индекс минимального значения: {min_num}")
print(f"Элементы главной диагонали: {diag}")

