# Задача 3. Добавьте в telegram-бота игру «Угадай числа». Бот загадывает число от 1 до 1000. Когда игрок угадывает его, бот выводит количество сделанных ходов

import telebot
import random
bot = telebot.TeleBot("5893272464:AAEj_9DuDrFmd9j65PAfXmIokqM0Shwm958")

number_random = random.randint(1, 1000)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Я загадал число от 1 до 1000. Отгадай его!")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    array = (1, 2, 3, 4, 5, 6, 7 , 8, 9, 0)
    Flag = True
    while Flag:
        flag = True
        for i in message.text:
            flag2 = False
            for j in array:
                if i == str(j):
                    flag2 = True
            if flag2 == False:
                flag = False
                break
        if flag == False:
            bot.reply_to(message, "Введите пожалуйста число!")
        elif int(message.text) == number_random:
            bot.reply_to(message, "Поздравляю, вы отгадали!")
        elif int(message.text) > number_random:
            bot.reply_to(message, "Меньше") 
        else:
            bot.reply_to(message, "Больше")         

bot.polling()