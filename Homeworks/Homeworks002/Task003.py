# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй

string1 = input("Введите первую строку: ")
string2 = input("Введите вторую строку: ")
lenght1 = len(string1)
lenght2 = len(string2)
new_string = []

counter = 0
for i in range(lenght1):
    if string1[i] not in new_string:
        new_string.insert(counter, string1[i])
        counter += 1
    
array = []
for i in range(len(new_string)):
    counter = 0
    
    for j in range(lenght2):
       if new_string[i] == string2[j]:
            counter += 1
    array.insert(i, counter)

for i in range(len(new_string)):
    print(f'Количество символов "{new_string[i]}" в строке "{string2}": {array[i]}')

