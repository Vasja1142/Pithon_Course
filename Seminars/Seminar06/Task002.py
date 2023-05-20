# Задача 2. Даны два случайных пятизначных числа.
# Определить, состоят ли они из одних и тех же цифр.

def Check(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    num1 = set(num1)
    num2 = set(num2)
    return num1 == num2

num1 = int(input("Введите первое пятизначное число: "))
num2 = int(input("Введите второе пятизначное число: "))
print(f"Ответ: {Check(num1, num2)}")

