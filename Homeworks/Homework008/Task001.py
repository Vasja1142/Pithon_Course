# Задача 1. Напишите бота для техподдержки. Бот должен записывать обращения пользователей в файл.

import telebot


Tocken = "5893272464:AAEj_9DuDrFmd9j65PAfXmIokqM0Shwm958"
bot = telebot.TeleBot(Tocken)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f"Здравствуйте, {message.from_user.first_name}! Я бот техподдержки последнего поколения! Задавайте вопрос.")

@bot.message_handler(func=lambda m: True)
def Question(message):
    data = open("Questions.txt", mode='a', encoding='utf=8')
    data.write(f"{message.from_user.last_name} {message.from_user.first_name} |{message.from_user.id}| {message.text}\n")
    data.close
    bot.reply_to(message, f"{message.from_user.first_name}, ваш вопрос уже обрабатывается! Все силы и средства службы поддержки брошены на разрешение данного вопроса! С минуты на минуту вам ответят. Главное верить и надеяться!")


bot.polling()