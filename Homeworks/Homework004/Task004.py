# Задача 4*. Даны два файла, в каждом из которых находится запись многочлена. Найдите сумму данных многочленов.
import Task0041

def dictionary_creation():
    dictionary = {}
    dictionary['x^2'] = 0
    dictionary['x'] = 0
    dictionary['c'] = 0
    return dictionary

def Calculation_functions(dictionary, y):
    y = list(y.split('+'))
    for i in y:
        if "x^2" in i:
            argument = i.replace('x^2', '')
            argument = argument.replace(' ', '')
            if argument == '':
                argument = 1
            else:
                argument = int(argument)
            dictionary['x^2'] += argument

        elif "x" in i:
            argument = i.replace('x', '')
            argument = argument.replace(' ', '')
            if argument == '':
                argument = 1
            else:
                argument = int(argument)
            dictionary['x'] += argument
        
        else:
            dictionary['c'] += int(i)

# Можно добавить любое количество многочленов!

y1 = "5x^2 + 3"
y2 = "3x^2 + x + 8"
functions = [y1, y2]

functions += Task0041.functions

dictionary = dictionary_creation()
for i in functions:
    Calculation_functions(dictionary, i)

print(f"Ответ: {dictionary['x^2']}x^2 + {dictionary['x']}x + {dictionary['c']}")

