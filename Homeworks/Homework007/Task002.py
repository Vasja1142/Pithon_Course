# Задача 2. Создайте декоратор, повторяющий функцию заданное количество раз.

def Average_Time(function):
    def Decorator(*args):
        import time
        average = 0
        num = int(input("Введите количество повторений теста: "))
        for i in range(num):
            Start = time.time()
            function(*args)
            average += time.time() - Start
        average /= num
        print(average)
    return Decorator

@Average_Time
def Fibonatti(number):
    fibonatti = []
    for i in range(number):
        if i < 2:
            fibonatti.append(1)
        else:
            fibonatti.append(fibonatti[i-1] + fibonatti[i-2])

Fibonatti(25000)