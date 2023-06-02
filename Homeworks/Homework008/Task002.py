# Задача 2. Напишите программу, которая позволяет считывать из файла вопрос, отвечать на него и отправлять ответ обратно пользователю.

import telebot

Tocken = "5893272464:AAEj_9DuDrFmd9j65PAfXmIokqM0Shwm958"
bot = telebot.TeleBot(Tocken)

data = open("Questions.txt", mode='r', encoding='utf=8')
questions = data.read().split("\n")
questions = questions[:-1]
print(questions)
for i in questions:
    question = str(i)
    question =  question.split("|")
    print(f"{question[0]}:{question[2]}")
    answer = input()
    bot.send_message(question[1], answer)

