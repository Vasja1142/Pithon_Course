# Задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и выводит название этого дня недели.

num = int(input("Введите номер дня недели: "))
if num == 1:
    print("Понедельник")
elif num == 2:
    print("Вторник")
elif num == 3:
    print("Среда")
elif num == 4:
    print("Четверг")
elif num == 5:
    print("Пятница")
elif num == 6:
    print("Суббота")
elif num == 7:
    print("Воскресенье")
else:
    print("Такого дня недели нет")
