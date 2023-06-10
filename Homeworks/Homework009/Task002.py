# Задача 2. Создайте двумерный массив, размером 5х5. Определите, есть ли в нём одинаковые строки.
import numpy as np

array = np.random.randint(0, 2, (5, 5))
uniq_row, counts = np.unique(array, return_counts=True, axis=0)
result = sum(counts>1)
print(array)
print(f"Ответ: {bool(result)}")

# print(f"Ответ: {array==uniq_row}")
