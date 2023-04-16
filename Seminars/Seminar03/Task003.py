# Задача 3. Напишите скрипт генератора паролей заданной длины, состоящих из латинских букв и чисел.
import random

flag = True
while flag:
    num = int(input("Введите длинну пароля: "))
    if num < 1 or num >= 30:
        print('Введите пожалуйста число от 1 до 30!')
    else:
        flag = False

symbols = "qwertyuiopasdfghjklzxcvbnm1234567890"
lenght = len(symbols)
passwords = []
list = [random.randint(0, lenght) for index in range(num)]
for i in list:
    passwords.append(symbols[i])



print(*passwords)