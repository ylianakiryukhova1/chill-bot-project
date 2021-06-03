import random

from telebot import types

import telebot

from bs4 import BeautifulSoup
import requests

name = ""

bot = telebot.TeleBot('1829390927:AAGoLo77oSmRj5WQH7RVnfzAs29L8bTSXss')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.from_user.id, 'Приветствую! Давайте познакомимся! Я помогу подобрать фильм или сериал по '
                                           'вашему желанию. Как Вас зовут? '
                     )
    bot.register_next_step_handler(message, reg_name)


def reg_name(message):
    global name
    name = message.text
    global otvet
    otvet = types.InlineKeyboardMarkup(row_width=2)
    button1 = types.InlineKeyboardButton("Фильмы", callback_data='command1')
    button2 = types.InlineKeyboardButton("Сериалы", callback_data='command2')
    otvet.add(button1, button2)
    bot.send_message(message.chat.id, f'Приятно познакомиться, {name}. Что бы Вы хотели посмотреть?', reply_markup=otvet)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == "command1":
                global otvet1
                global otvet3

                otvet1 = types.InlineKeyboardMarkup(row_width=2)
                otvet3 = types.InlineKeyboardMarkup(row_width=2)
                btn1 = types.InlineKeyboardButton("Аниме", callback_data='anime')
                btn2 = types.InlineKeyboardButton("Биографии", callback_data='biography')
                btn3 = types.InlineKeyboardButton("Боевики", callback_data='action')
                btn4 = types.InlineKeyboardButton("Вестерны", callback_data='western')
                btn5 = types.InlineKeyboardButton("Военные", callback_data='war')
                btn6 = types.InlineKeyboardButton("Детективы", callback_data='mystery')
                btn7 = types.InlineKeyboardButton("Драмы", callback_data='drama')
                btn8 = types.InlineKeyboardButton("Исторические", callback_data='history')
                btn9 = types.InlineKeyboardButton("Комедии", callback_data='comedy')
                btn10 = types.InlineKeyboardButton("Криминал", callback_data='crime')
                btn11 = types.InlineKeyboardButton("Мелодраммы", callback_data='romance')
                btn12 = types.InlineKeyboardButton("Мультфильмы", callback_data='animation')
                btn13 = types.InlineKeyboardButton("Мюзиклы", callback_data='musical')
                btn14 = types.InlineKeyboardButton("Приключения", callback_data='adventure')
                btn15 = types.InlineKeyboardButton("Семейные", callback_data='family')
                btn16 = types.InlineKeyboardButton("Спортивные", callback_data='sport')
                btn17 = types.InlineKeyboardButton("Триллеры", callback_data='thriller')
                btn18 = types.InlineKeyboardButton("Ужасы", callback_data='horror')
                btn19 = types.InlineKeyboardButton("Фантастика", callback_data='sci_fi')
                btn20 = types.InlineKeyboardButton("Фэнтези", callback_data='fantasy')
                bttn3 = types.InlineKeyboardButton("В этом жанре", callback_data='click1')
                bttn4 = types.InlineKeyboardButton("В другом", callback_data='click2')
                otvet1.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14,
                           btn15, btn16, btn17, btn18, btn19, btn20)

                otvet3.add(bttn3, bttn4)

                bot.send_message(call.message.chat.id, 'Отлично. Давайте определимся с жанром',
                                 reply_markup=otvet1)
                global otvet2
                otvet2 = types.InlineKeyboardMarkup(row_width=2)
                bttn1 = types.InlineKeyboardButton("Да", callback_data='click11')
                bttn2 = types.InlineKeyboardButton("Предложи другой", callback_data='click21')
                otvet2.add(bttn1, bttn2)


            if call.data == "command2":
                global otvet5
                global otvet4

                otvet5 = types.InlineKeyboardMarkup(row_width=2)
                otvet4 = types.InlineKeyboardMarkup(row_width=2)
                btn1_1 = types.InlineKeyboardButton("Аниме", callback_data='anime1')
                btn2_1 = types.InlineKeyboardButton("Биографии", callback_data='biography1')
                btn3_1 = types.InlineKeyboardButton("Боевики", callback_data='action1')
                btn4_1 = types.InlineKeyboardButton("Вестерны", callback_data='western1')
                btn5_1 = types.InlineKeyboardButton("Военные", callback_data='war1')
                btn6_1 = types.InlineKeyboardButton("Детективы", callback_data='mystery1')
                btn7_1 = types.InlineKeyboardButton("Драмы", callback_data='drama1')
                btn8_1 = types.InlineKeyboardButton("Исторические", callback_data='history1')
                btn9_1 = types.InlineKeyboardButton("Комедии", callback_data='comedy1')
                btn10_1 = types.InlineKeyboardButton("Криминал", callback_data='crime1')
                btn11_1 = types.InlineKeyboardButton("Мелодраммы", callback_data='romance1')
                btn12_1 = types.InlineKeyboardButton("Мультфильмы", callback_data='animation1')
                btn13_1 = types.InlineKeyboardButton("Мюзиклы", callback_data='musical1')
                btn14_1 = types.InlineKeyboardButton("Приключения", callback_data='adventure1')
                btn15_1 = types.InlineKeyboardButton("Семейные", callback_data='family1')
                btn16_1 = types.InlineKeyboardButton("Спортивные", callback_data='sport1')
                btn17_1 = types.InlineKeyboardButton("Триллеры", callback_data='thriller1')
                btn18_1 = types.InlineKeyboardButton("Ужасы", callback_data='horror1')
                btn19_1 = types.InlineKeyboardButton("Фантастика", callback_data='sci_fi1')
                btn20_1 = types.InlineKeyboardButton("Фэнтези", callback_data='fantasy1')
                bttn3_1 = types.InlineKeyboardButton("В этом жанре", callback_data='click3')
                bttn4_1 = types.InlineKeyboardButton("В другом", callback_data='click4')
                otvet5.add(btn1_1, btn2_1, btn3_1, btn4_1, btn5_1, btn6_1, btn7_1, btn8_1, btn9_1, btn10_1, btn11_1,
                           btn12_1, btn13_1, btn14_1,
                           btn15_1, btn16_1, btn17_1, btn18_1, btn19_1, btn20_1)

                otvet4.add(bttn3_1, bttn4_1)

                bot.send_message(call.message.chat.id, 'Отлично. Давайте определимся с жанром',
                                 reply_markup=otvet5)

                global otvet6
                otvet6 = types.InlineKeyboardMarkup(row_width=2)
                bttn1_1 = types.InlineKeyboardButton("Да", callback_data='click1_1')
                bttn2_1 = types.InlineKeyboardButton("Предложи другой", callback_data='click2_2')
                otvet6.add(bttn1_1, bttn2_1)
                callback_inline1(call)


            if call.data == "anime":

                url = 'https://www.kinopoisk.ru/lists/top250/anime/?tab=all'

            elif call.data == "biography":
                url = 'https://www.kinopoisk.ru/lists/top250/biography/?tab=all'


            elif call.data == "action":

                url = 'https://www.kinopoisk.ru/lists/top250/action/?tab=all'


            elif call.data == "western":

                url = 'https://www.kinopoisk.ru/lists/top250/western/?tab=all'

            elif call.data == "war":

                url = 'https://www.kinopoisk.ru/lists/top250/war/?tab=all'


            elif call.data == "mystery":

                url = 'https://www.kinopoisk.ru/lists/top250/mystery/?tab=all'

            elif call.data == "drama":

                url = 'https://www.kinopoisk.ru/lists/top250/drama/?tab=all'


            elif call.data == "history":

                url = 'https://www.kinopoisk.ru/lists/top250/history/?tab=all'


            elif call.data == "comedy":

                url = 'https://www.kinopoisk.ru/lists/top250/comedy/?tab=all'


            elif call.data == "crime":

                url = 'https://www.kinopoisk.ru/lists/top250/crime/?tab=all'


            elif call.data == "romance":

                url = 'https://www.kinopoisk.ru/lists/top250/romance/?tab=all'


            elif call.data == "animation":

                url = 'https://www.kinopoisk.ru/lists/top250/animation/?tab=all'


            elif call.data == "musical":

                url = 'https://www.kinopoisk.ru/lists/top250/musical/?tab=all'


            elif call.data == "adventure":

                url = 'https://www.kinopoisk.ru/lists/top250/adventure/?tab=all'


            elif call.data == "family":

                url = 'https://www.kinopoisk.ru/lists/top250/family/?tab=all'


            elif call.data == "sport":

                url = 'https://www.kinopoisk.ru/lists/top250/sport/?tab=all'


            elif call.data == "thriller":

                url = 'https://www.kinopoisk.ru/lists/top250/thriller/?tab=all'


            elif call.data == "horror":

                url = 'https://www.kinopoisk.ru/lists/top250/horror/?tab=all'

            elif call.data == "sci_fi":

                url = 'https://www.kinopoisk.ru/lists/top250/sci-fi/?tab=all'

            elif call.data == "fantasy":

                url = 'https://www.kinopoisk.ru/lists/top250/fantasy/?tab=all'

            elif call.data == "click11":
                bot.send_message(call.message.chat.id,
                                 "Желаю Вам приятного просмотра. Не забудьте захватить вкусняшки.")

            elif call.data == "click21":
                bot.send_message(call.message.chat.id, "В каком жанре?", reply_markup=otvet3)

            elif call.data == "click1":
                bot.send_message(call.message.chat.id, "Ничем не могу помочь")

            elif call.data == "click2":
                bot.send_message(call.message.chat.id, "Давайте попробуем заново", reply_markup=otvet1)

            response = requests.get(url)

            soup = BeautifulSoup(response.text, 'html.parser')

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

            bot.send_message(call.message.chat.id, "".join(out3[0]))
            bot.send_message(call.message.chat.id, "Вам нравится этот вариант?", reply_markup=otvet2)


    except Exception as e:
        print(repr(e))


@bot.callback_query_handler(func=lambda call: True)
def callback_inline1(call):
    try:
        if call.message:

            if call.data == "anime1":

                url = 'https://www.kinopoisk.ru/lists/top250/anime/?tab=all'

            elif call.data == "biography1":

                url = 'https://www.kinopoisk.ru/lists/top250/anime/?tab=all'

            elif call.data == "action1":

                url = 'https://www.kinopoisk.ru/lists/top250/anime/?tab=all'


            elif call.data == "western1":

                url = 'https://www.kinopoisk.ru/lists/top250/anime/?tab=all'

            elif call.data == "war1":

                url = 'https://www.kinopoisk.ru/lists/top250/anime/?tab=all'

            elif call.data == "mystery1":

                url = 'https://www.kinopoisk.ru/lists/top250/anime/?tab=all'

            elif call.data == "drama1":

                url = 'https://www.kinopoisk.ru/lists/top250/anime/?tab=all'


            elif call.data == "history1":

                url = 'https://www.kinopoisk.ru/lists/top250/anime/?tab=all'

            elif call.data == "comedy11":

                url = 'https://www.kinopoisk.ru/lists/top250/anime/?tab=all'

            elif call.data == "crime1":

                url = 'https://www.kinopoisk.ru/lists/top250/anime/?tab=all'


            elif call.data == "romance1":

                url = 'https://www.kinopoisk.ru/lists/top250/anime/?tab=all'


            elif call.data == "animation1":

                url = 'https://www.kinopoisk.ru/lists/top250/anime/?tab=all'


            elif call.data == "musical1":

                url = 'https://www.kinopoisk.ru/lists/top250/anime/?tab=all'


            elif call.data == "adventure1":

                url = 'https://www.kinopoisk.ru/lists/top250/anime/?tab=all'

            elif call.data == "family1":

                url = 'https://www.kinopoisk.ru/lists/top250/anime/?tab=all'

            elif call.data == "sport1":

                url = 'https://www.kinopoisk.ru/lists/top250/anime/?tab=all'


            elif call.data == "thriller1":

                url = 'https://www.kinopoisk.ru/lists/top250/anime/?tab=all'


            elif call.data == "horror1":

                url = 'https://www.kinopoisk.ru/lists/top250/anime/?tab=all'

            elif call.data == "sci_fi1":

                url = 'https://www.kinopoisk.ru/lists/top250/anime/?tab=all'


            elif call.data == "fantasy1":

                url = 'https://www.kinopoisk.ru/lists/top250/anime/?tab=all'

            elif call.data == "click1_1":
                bot.send_message(call.message.chat.id,
                                 "Желаю вам приятного просмотра. Не забудьте захватить вкусняшки.")

            elif call.data == "click2_2":
                bot.send_message(call.message.chat.id, "В каком жанре?", reply_markup=otvet4)

            elif call.data == "click3":
                bot.send_message(call.message.chat.id, "Ничем не могу помочь")

            elif call.data == "click4":
                bot.send_message(call.message.chat.id, "Давайте попробуем заново", reply_markup=otvet5)

            response = requests.get(url)

            soup = BeautifulSoup(response.text, 'html.parser')

            name1_1 = soup.find_all('p', class_='selection-film-item-meta__name')
            original1_1 = soup.find_all('p', class_='selection-film-item-meta__original-name')
            rating1_1 = soup.find_all('span', class_='rating__value rating__value_positive')
            country1_1 = soup.find_all('span', class_='selection-film-item-meta__meta-additional-item')

            out_1 = []
            out2_1 = []
            out3_1 = []

            for m in range(0, len(original1_1)):
                out_1.append(original1_1[m].text)
            for k in range(0, len(out_1)):
                out2_1.append(out_1[k].split(', '))
            for y in range(0, len(out2_1)):
                if len(out2_1[y]) == 1:
                    out2_1[y].insert(0, '')
            for i in range(0, len(name1_1)):
                out3_1.append(
                    'Название: ' + name1_1[i].text + '\n' + 'Оригинальное название: ' + out2_1[i][
                        0] + '\n' + 'Год: ' +
                    out2_1[i][
                        1] + '\n' + 'Страна: ' + country1_1[::2][i].text + '\n' + 'Жанр: ' + country1_1[1::2][
                        i].text + '\n' + 'Оценка: ' +
                    rating1_1[i].text + '\n')

            bot.send_message(call.message.chat.id, "".join(random.choice(out3_1)))
            bot.send_message(call.message.chat.id, "Вам нравится этот вариант?", reply_markup=otvet6)


    except Exception as e:
        print(repr(e))


if __name__ == '__main__':
    bot.polling(none_stop=True)
