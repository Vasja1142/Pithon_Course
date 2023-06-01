# Задача 1. Создайте пользовательский аналог метода map().
numbers = [1,2,6,7,5,3]

def Method_map(function, array):
    return (function(el) for el in array)

def Map(num):
    return num*2

print( list(Method_map(Map, numbers)))