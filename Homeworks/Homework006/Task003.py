# Задача 3. Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11.

numerator = 1
denominator = 1
result = []
for i in range(1, 12):
    for j in range(1, i):
        flag = True
        for k in range(2, j+1):
            if i % k == 0 and j % k == 0:
                flag = False
                break
        if flag == True:
            result.append(f"{j}/{i}")
            
print(result)
