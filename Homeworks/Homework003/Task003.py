# Задача 3. Создайте скрипт бота, который находит ответы на фразы по ключу в словаре. Бот должен, как минимум,
# отвечать на фразы «привет», «как тебя зовут». Если фраза ему неизвестна, он выводит соответствующую фразу.

data = open('Library.txt', encoding='utf-8')

print('"Здравствуйте! Вы запустили примитивного чат бота. Для выхода из него нажмите "Enter"')
print(KeyError)
text = data.readlines()
bot = {}
for i in text:
    phrase = i.split(':')
    bot[phrase[0]] = phrase[1]
data.close()
flag = True
while flag:
    inp = input().lower()
    flag2 = True
    for (k, v) in bot.items():
        if k == inp:
            flag2 = False

    if inp == '':
        flag = False
    elif flag2:
        print("Такую фразу я еще не знаю!")
    else:
        print(bot[inp])
