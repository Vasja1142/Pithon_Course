# Задача 3. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*.
# приоритет операций стандартный.
# а) Решите задачу для одного действия;
# б) Дополнительное задание. Решите задачу для нескольких действий;
# в) Решите задачу средствами python.

arithmetic_expression = input("Введите арифметическое выражение (с пробелами): ") #2 + 43 * 3    = 14
array = arithmetic_expression.split()
print(array)

counter = 1
for i in array[1: -1: 2]:
    if i == "*" or i == "/":
        if i == "*":
            value = int(array[counter-1]) * int(array[counter+1])
            del array[counter-1: counter+2]
            array.insert(counter-1, value)
        elif i == "/":
            value = int(array[counter-1]) / int(array[counter+1])
            del array[counter-1: counter+2]
            array.insert(counter-1, value)
    else:
        counter += 2

counter = 1
for i in array[1: -1: 2]:
    if i == "+" or i == "-":
        if i == "+":
            value = int(array[counter-1]) * int(array[counter+1])
            del array[counter-1: counter+2]
            array.insert(counter-1, value)
        elif i == "-":
            value = int(array[counter-1]) / int(array[counter+1])
            del array[counter-1: counter+2]
            array.insert(counter-1, value)

print(array)

     































# adding = arithmetic_expression.split("+")
# print(adding)
# result = None
# for i in adding:
#     subtraction = i.split("-")
#     print(subtraction)
#     for j in subtraction:
#         multiplication = j.split("*")
#         print(multiplication)
#         for k in multiplication:
#             division = k.split("/")
#             for l in division[1:]:
#                 if result == None:
#                     result = int(division[0])
#                 result = int(division[0])
#                 result /= int(l)
#             k = result
#         for k in multiplication[1:]:
#             result *= int(k) 
#         j = result
#     for j in subtraction[1:]:
#         result -= int(j)
#     i = result
# for i in adding[1:]:
#     result += int(i)