# Задача 3: Сгенерируйте список случайных чисел от 1 до 20, состоящий из 10 элементов. 
# Удалите из списка дубликаты уже имеющихся элементов. Определите, сколько элементов было удалено.
import random
numbers = list(random.randint(1, 20) for _ in range(10))
numbers2 = list(set(numbers))
difference = len(numbers) - len(numbers2)
print(f"Начальный список: {numbers2}.")
print(f"Готовый список: {numbers2}.")
print(f"Удалено элементов: {difference}")