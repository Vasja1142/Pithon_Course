# Задача 3. Дано число N. Заполните список длиной N элементами 1, -3, 9, -27, 81, -243...

number = int(input("Введите любое число больше 0: "))
result = []
value = 1
if number > 0:
    for i in range(number):
        result.insert(i, value)
        value *= -3
    print(result)
else:
    print("Это число не больше 0")
