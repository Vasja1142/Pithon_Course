# Задача 4. Найдите все числа до 10000, у которыx количество делителей равно 10.

def calculation(number):
    result = []
    index = 0
    for i in range(1, number + 1):
        counter = 0
        for j in range(1, i + 1):
            if i % j == 0:
                counter +=1
        if counter == 10:
            result.insert(index, i)
            index += 1
    return result

array = calculation(10000)
print(array)