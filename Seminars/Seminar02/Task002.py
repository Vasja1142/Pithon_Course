# Задача 2. Напишите программу, в которой пользователь будет задавать две строки, а программа
# - определять количество вхождений одной строки в другую.


string1 = input("Введите первую строку: ")
string2 = input("Введите вторую строку: ")
lenght1 = len(string1)
lenght2 = len(string2)

counter = 0
for i in range(lenght1, lenght2 + 1):
    if string2[i - lenght1: i] == string1:
        counter += 1

print(f'Количество вхождений первой строки во вторую: {counter}')