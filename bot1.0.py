from telebot import types

import telebot

from bs4 import BeautifulSoup
import requests

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
    bot.send_message(message.chat.id, f'Приятно познакомиться, {name}. Что бы ты хотел посмотреть?', reply_markup=otvet)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
   try:
       if call.message:
           if call.data == "command1":

                   otvet1 = types.InlineKeyboardMarkup(row_width=2)

                   otvet3 = types.InlineKeyboardMarkup(row_width=2)
                   btn1 = types.InlineKeyboardButton("Аниме", callback_data='anime')
                   btn2 = types.InlineKeyboardButton("Биографии", callback_data='command2')
                   btn3 = types.InlineKeyboardButton("Боевики", callback_data='command1')
                   btn4 = types.InlineKeyboardButton("Вестерны", callback_data='command2')
                   btn5 = types.InlineKeyboardButton("Военные", callback_data='command1')
                   btn6 = types.InlineKeyboardButton("Детективы", callback_data='command2')
                   btn7 = types.InlineKeyboardButton("Драммы", callback_data='command2')
                   btn8 = types.InlineKeyboardButton("Исторические", callback_data='command1')
                   btn9 = types.InlineKeyboardButton("Комедии", callback_data='command2')
                   btn10 = types.InlineKeyboardButton("Криминал", callback_data='command1')
                   btn11 = types.InlineKeyboardButton("Мелодраммы", callback_data='command2')
                   btn12 = types.InlineKeyboardButton("Мультфильмы", callback_data='command1')
                   btn13 = types.InlineKeyboardButton("Мюзиклы", callback_data='command2')
                   btn14 = types.InlineKeyboardButton("Приключения", callback_data='command1')
                   btn15 = types.InlineKeyboardButton("Семейные", callback_data='command2')
                   btn16 = types.InlineKeyboardButton("Спортивные", callback_data='command1')
                   btn17 = types.InlineKeyboardButton("Триллеры", callback_data='command2')
                   btn18 = types.InlineKeyboardButton("Ужасы", callback_data='command1')
                   btn19 = types.InlineKeyboardButton("Фантастика", callback_data='command2')
                   btn20 = types.InlineKeyboardButton("Фэнтези", callback_data='command1')
                   bttn3=types.InlineKeyboardButton("В этом жанре", callback_data='command1')
                   bttn4 = types.InlineKeyboardButton("В другом", callback_data='command1')
                   otvet1.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15, btn16, btn17, btn18, btn19, btn20)


                   otvet2.add(bttn3, bttn4)



                   bot.send_message(call.message.chat.id, 'Отлично. Давай определимся с жанром',
                                    reply_markup=otvet1)


           if call.data == "command2":
               bot.send_message(call.message.chat.id, "Ничего, все наладится!")

           if call.data == "anime":
                   otvet2 = types.InlineKeyboardMarkup(row_width=2)
                   bttn1 = types.InlineKeyboardButton("Да", callback_data='command1')
                   bttn2 = types.InlineKeyboardButton("Предложи другой", callback_data='command1')
                   otvet2.add(bttn1, bttn2)
                   url = 'https://www.kinopoisk.ru/lists/top250/anime/?tab=all'
                   response = requests.get(url)

                   soup = BeautifulSoup(response.text, 'lxml')

                   name1 = soup.find_all('p', class_='selection-film-item-meta__name')
                   original1 = soup.find_all('p', class_='selection-film-item-meta__original-name')
                   rating1 = soup.find_all('span', class_='rating__value rating__value_positive')
                   country1 = soup.find_all('span', class_='selection-film-item-meta__meta-additional-item')

                   out = []
                   out2 = []
                   out3 = []

                   for m in range(0, len(original1)):
                       out.append(original1[m].text)
                   for k in range(0, len(out)):
                       out2.append(out[k].split(', '))
                   for y in range(0, len(out2)):
                       if len(out2[y]) == 1:
                           out2[y].insert(0, '')
                   for i in range(0, len(name1)):
                       out3.append(
                           'Название: ' + name1[i].text + '\n' + 'Оригинальное название: ' + out2[i][
                               0] + '\n' + 'Год: ' +
                           out2[i][
                               1] + '\n' + 'Страна: ' + country1[::2][i].text + '\n' + 'Жанр: ' + country1[1::2][
                               i].text + '\n' + 'Оценка: ' +
                           rating1[i].text + '\n')

                   bot.send_message(call.message.chat.id, "".join(out3[1]))
                   bot.send_message(call.message.chat.id, "Вам нравится этот вариант?",reply_markup=otvet2)


   except Exception as e:
       print(repr(e))



bot.polling()