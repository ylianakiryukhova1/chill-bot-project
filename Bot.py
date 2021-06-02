import types

import telebot

import sqlalchemy

name = ""

bot = telebot.TeleBot('1880692984:AAEbuXKhFjE6XxjjgNGfRrGgE4eiKWHpajM')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.from_user.id, 'Приветствую! Давай познакомимся! Я помогу подобрать фильм или сериал по '
                                           'твоему желанию. Как тебя зовут? '
                     )
    bot.register_next_step_handler(message, reg_name)


def reg_name(message):
    global name
    name = message.text
    otvet = types.InlineKeyboardMarkup(row_width=2)
    button1 = types.InlineKeyboardButton("Фильмы", callback_data='command1')
    button2 = types.InlineKeyboardButton("Сериалы", callback_data='command2')
    otvet.add(button1, button2)
    bot.send_message(message.chat.id, f'Приятно познакомиться, {name}. Что бы ты хотел посмотреть?', reply_markup = otvet)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
   try:
       if call.message:
           if call.data == "command1":
               otvet1 = types.InlineKeyboardMarkup(row_width=2)
               btn1 = types.InlineKeyboardButton("Фильмы", callback_data='command1')
               button2 = types.InlineKeyboardButton("Сериалы", callback_data='command2')
               otvet1.add(btn1, button2)
               bot.send_message(message.chat.id, f'Приятно познакомиться, {name}. Что бы ты хотел посмотреть?',
                                reply_markup=otvet)
           if call.data == "command2":
               bot.send_message(call.message.chat.id, "Ничего, все наладится!")
   except Exception as e:
       print(repr(e))


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message, 'Помощь\n'
                              '/start - начало работы с ботом, переход в меню\n'
                     )


@bot.message_handler(content_types=["text"])
def text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message, 'И тебе привет')


