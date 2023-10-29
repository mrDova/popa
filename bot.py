import telebot
import sqlite3
from telebot import types

bot = telebot.TeleBot('6383134312:AAENMCSgvUDdegij8Dg9jF6vjkslQRxVxGs')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Привет, CapyBot☀️')
    markup.row(btn1)
    bot.send_message(message.chat.id, f'Привет капибобрик, {message.from_user.first_name}!👋', reply_markup=markup)
    bot.register_next_step_handler(message, nachalo)

def nachalo(message):
    if message.text == 'Привет, CapyBot☀️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Мой Курс❤️')
        btn2 = types.KeyboardButton('Телеграм-канал Капибары')
        markup.row(btn1)
        markup.row(btn2)
        bot.send_message(message.chat.id, 'Чем могу помочь?', reply_markup=markup)
        bot.register_next_step_handler(message, vcurs)
    elif message.text == '/restart':
        bot.register_next_step_handler(message, start)
    elif message.text == '/link':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Ссылка на беседу', url='https://t.me/+Dd9o9PDg-vs5ZWEy')
        markup.row(btn1)
        bot.send_message(message.chat.id, 'Это  чат с твоим преподавателем и однокурсниками. Ко времени онлайн занятий тут будут приходить ссылки на них. А еще тут можно что-то обсудить, поделиться впечатлениями и новостями❤️', reply_markup=markup)
        bot.register_next_step_handler(message, nachalo)
    else:
        bot.send_message(message.chat.id, 'Не совсем понял тебя... Давай попробуем ещё раз')
        bot.register_next_step_handler(message, nachalo)


def vcurs(message):
    if message.text == 'Мой Курс❤️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Вводное занятие')
        btn2 = types.KeyboardButton('Общая биология')
        btn3 = types.KeyboardButton('Ботаника')
        btn4 = types.KeyboardButton('Грибы и Лишайники')
        btn5 = types.KeyboardButton('Зоология')
        btn6 = types.KeyboardButton('Анатомия')
        btn7 = types.KeyboardButton('Эволюция')
        btn8 = types.KeyboardButton('Экология')
        markup.row(btn1)
        markup.row(btn2)
        markup.row(btn3)
        markup.row(btn4)
        markup.row(btn5)
        markup.row(btn6)
        markup.row(btn7)
        markup.row(btn8)
        bot.send_message(message.chat.id, '✨Вот занятия Курса ОГЭ, доступные тебе:)')
        bot.send_message(message.chat.id, '(Выбери нужное)', reply_markup=markup)
        bot.register_next_step_handler(message, vvod)
    elif message.text == 'Телеграм-канал Капибары':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Ссылка на Телеграм-канал', url='https://t.me/capybara_school')
        markup.row(btn1)
        bot.send_message(message.chat.id, 'Это наш основной канал, тут преподаватель делится многими интересными и полезными материалами , а так же рассказывает о своей жизни, медицине и биологии.', reply_markup=markup)
        bot.register_next_step_handler(message, vcurs)
    elif message.text == '/restart':
        bot.register_next_step_handler(message, start)
    elif message.text == '/link':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Ссылка на беседу', url='https://t.me/+Dd9o9PDg-vs5ZWEy')
        markup.row(btn1)
        bot.send_message(message.chat.id, 'Это  чат с твоим преподавателем и однокурсниками. Ко времени онлайн занятий тут будут приходить ссылки на них. А еще тут можно что-то обсудить, поделиться впечатлениями и новостями❤️', reply_markup=markup)
        bot.register_next_step_handler(message, vcurs)
    else:
        bot.send_message(message.chat.id, 'Не совсем понял тебя... Давай попробуем ещё раз')
        bot.register_next_step_handler(message, vcurs)
        
def vvod(message):
    if message.text == 'Вводное занятие':
        markup = types.InlineKeyboardMarkup()
        markups = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.InlineKeyboardButton('Скрипт', callback_data='skrp0')
        btn2 = types.InlineKeyboardButton('ДЗ', callback_data='dz1')
        btn = types.KeyboardButton('Выбрать другое занятие')
        markup.row(btn1, btn2)
        markups.row(btn)
        bot.send_message(message.chat.id, f'https://us06web.zoom.us/rec/share/Dx6ou6OTayjihoG5SRWnBX1GMLOmDe5AEs9UIADdYPxycwCcZfCl4QPY1IzCzWNS.IqgpH4sI6Ajm1Br6', reply_markup=markup, parse_mode="html")
        bot.send_message(message.chat.id, 'Смотри, учи, запоминай!', reply_markup=markups)
        bot.register_next_step_handler(message, hlp)
    elif message.text == 'Общая биология':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Занятие 1')
        btn2 = types.KeyboardButton('Занятие 2')
        btn3 = types.KeyboardButton('Занятие 3')
        btn4 = types.KeyboardButton('Занятие 4')
        btn5 = types.KeyboardButton('Выбрать другой раздел')
        markup.row(btn1)
        markup.row(btn2)
        markup.row(btn3)
        markup.row(btn4)
        markup.row(btn5)
        bot.send_message(message.chat.id, '✨Вот список занятий по Общей биологии:)')
        bot.send_message(message.chat.id, '(Выбери нужное, в нем ты найдешь запись веба, скрипт и домашку к нему)', reply_markup=markup)
        bot.register_next_step_handler(message, zad)
    elif message.text == 'Ботаника':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Занятие 1')
        btn2 = types.KeyboardButton('Занятие 2')
        btn3 = types.KeyboardButton('Занятие 3')
        btn4 = types.KeyboardButton('Занятие 4')
        btn5 = types.KeyboardButton('Занятие 5')
        btn6 = types.KeyboardButton('Занятие 6')
        btn7 = types.KeyboardButton('Выбрать другой раздел')
        markup.row(btn1)
        markup.row(btn2)
        markup.row(btn3)
        markup.row(btn4)
        markup.row(btn5)
        markup.row(btn6)
        markup.row(btn7)
        bot.send_message(message.chat.id, '✨Вот список занятий по Общей биологии:)')
        bot.send_message(message.chat.id, '(Выбери нужное, в нем ты найдешь запись веба, скрипт и домашку к нему)', reply_markup=markup)
        bot.register_next_step_handler(message, botan)
    elif message.text == 'Грибы и Лишайники':
        markup = types.InlineKeyboardMarkup()
        markups = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.InlineKeyboardButton('Скрипт', callback_data='skrp0')
        btn2 = types.InlineKeyboardButton('ДЗ', callback_data='dz1')
        btn = types.KeyboardButton('Выбрать другое занятие')
        markup.row(btn1, btn2)
        markups.row(btn)
        bot.send_message(message.chat.id, f'https://us06web.zoom.us/rec/share/Dx6ou6OTayjihoG5SRWnBX1GMLOmDe5AEs9UIADdYPxycwCcZfCl4QPY1IzCzWNS.IqgpH4sI6Ajm1Br6', reply_markup=markup, parse_mode="html")
        bot.send_message(message.chat.id, 'Смотри, учи, запоминай!', reply_markup=markups)
        bot.register_next_step_handler(message, hlp)
    elif message.text == '/restart':
        bot.register_next_step_handler(message, start)
    elif message.text == '/link':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Ссылка на беседу', url='https://t.me/+Dd9o9PDg-vs5ZWEy')
        markup.row(btn1)
        bot.send_message(message.chat.id, 'Это  чат с твоим преподавателем и однокурсниками. Ко времени онлайн занятий тут будут приходить ссылки на них. А еще тут можно что-то обсудить, поделиться впечатлениями и новостями❤️', reply_markup=markup)
        bot.register_next_step_handler(message, vvod)
    else:
        bot.send_message(message.chat.id, 'Не совсем понял тебя... Давай попробуем ещё раз')
        bot.register_next_step_handler(message, vvod)
    
def botan(message):
    if message.text == 'Занятие 1':
        markup = types.InlineKeyboardMarkup()
        markups = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.InlineKeyboardButton('Скрипт', callback_data='skrp1')
        btn2 = types.InlineKeyboardButton('ДЗ', callback_data='dz1')
        btn = types.KeyboardButton('Выбрать другой занятие')
        markup.row(btn1, btn2)
        markups.row(btn)
        bot.send_message(message.chat.id, f'Занятие 1 <b>«Введение в Анатомию»</b> \n <i>Дата онлайн-занятия:22.07.2023</i> \n <i>Время: 10:00 мск</i> \n https://youtube.com/live/3qandDxgKqM?feature=share', reply_markup=markup, parse_mode="html")
        bot.send_message(message.chat.id, 'Смотри, учи, запоминай!', reply_markup=markups)
        bot.register_next_step_handler(message, hlp)
    elif message.text == 'Занятие 2':
        markup = types.InlineKeyboardMarkup()
        markups = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.InlineKeyboardButton('Скрипт', callback_data='skrp1')
        btn2 = types.InlineKeyboardButton('ДЗ', callback_data='dz1')
        btn = types.KeyboardButton('Выбрать другое занятие')
        markup.row(btn1, btn2)
        markups.row(btn)
        bot.send_message(message.chat.id, f'Занятие 1 <b>«Введение в Анатомию»</b> \n <i>Дата онлайн-занятия:22.07.2023</i> \n <i>Время: 10:00 мск</i> \n https://youtube.com/live/3qandDxgKqM?feature=share', reply_markup=markup, parse_mode="html")
        bot.send_message(message.chat.id, 'Смотри, учи, запоминай!', reply_markup=markups)
        bot.register_next_step_handler(message, hlp)
    elif message.text == 'Занятие 3':
        markup = types.InlineKeyboardMarkup()
        markups = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.InlineKeyboardButton('Скрипт', callback_data='skrp1')
        btn2 = types.InlineKeyboardButton('ДЗ', callback_data='dz1')
        btn = types.KeyboardButton('Выбрать другое занятие')
        markup.row(btn1, btn2)
        markups.row(btn)
        bot.send_message(message.chat.id, f'Занятие 1 <b>«Введение в Анатомию»</b> \n <i>Дата онлайн-занятия:22.07.2023</i> \n <i>Время: 10:00 мск</i> \n https://youtube.com/live/3qandDxgKqM?feature=share', reply_markup=markup, parse_mode="html")
        bot.send_message(message.chat.id, 'Смотри, учи, запоминай!', reply_markup=markups)
        bot.register_next_step_handler(message, hlp)
    elif message.text == 'Занятие 4':
        markup = types.InlineKeyboardMarkup()
        markups = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.InlineKeyboardButton('Скрипт', callback_data='skrp1')
        btn2 = types.InlineKeyboardButton('ДЗ', callback_data='dz1')
        btn = types.KeyboardButton('Выбрать другое занятие')
        markup.row(btn1, btn2)
        markups.row(btn)
        bot.send_message(message.chat.id, f'Занятие 1 <b>«Введение в Анатомию»</b> \n <i>Дата онлайн-занятия:22.07.2023</i> \n <i>Время: 10:00 мск</i> \n https://youtube.com/live/3qandDxgKqM?feature=share', reply_markup=markup, parse_mode="html")
        bot.send_message(message.chat.id, 'Смотри, учи, запоминай!', reply_markup=markups)
        bot.register_next_step_handler(message, hlp)
    elif message.text == 'Занятие 5':
        markup = types.InlineKeyboardMarkup()
        markups = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.InlineKeyboardButton('Скрипт', callback_data='skrp1')
        btn2 = types.InlineKeyboardButton('ДЗ', callback_data='dz1')
        btn = types.KeyboardButton('Выбрать другое занятие')
        markup.row(btn1, btn2)
        markups.row(btn)
        bot.send_message(message.chat.id, f'Занятие 1 <b>«Введение в Анатомию»</b> \n <i>Дата онлайн-занятия:22.07.2023</i> \n <i>Время: 10:00 мск</i> \n https://youtube.com/live/3qandDxgKqM?feature=share', reply_markup=markup, parse_mode="html")
        bot.send_message(message.chat.id, 'Смотри, учи, запоминай!', reply_markup=markups)
        bot.register_next_step_handler(message, hlp)
    elif message.text == 'Занятие 6':
        markup = types.InlineKeyboardMarkup()
        markups = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.InlineKeyboardButton('Скрипт', callback_data='skrp1')
        btn2 = types.InlineKeyboardButton('ДЗ', callback_data='dz1')
        btn = types.KeyboardButton('Выбрать другое занятие')
        markup.row(btn1, btn2)
        markups.row(btn)
        bot.send_message(message.chat.id, f'Занятие 1 <b>«Введение в Анатомию»</b> \n <i>Дата онлайн-занятия:22.07.2023</i> \n <i>Время: 10:00 мск</i> \n https://youtube.com/live/3qandDxgKqM?feature=share', reply_markup=markup, parse_mode="html")
        bot.send_message(message.chat.id, 'Смотри, учи, запоминай!', reply_markup=markups)
        bot.register_next_step_handler(message, hlp)
    elif message.text == 'Выбрать другой раздел':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Вводное занятие')
        btn2 = types.KeyboardButton('Общая биология')
        btn3 = types.KeyboardButton('Ботаника')
        btn4 = types.KeyboardButton('Грибы и Лишайники')
        btn5 = types.KeyboardButton('Зоология')
        btn6 = types.KeyboardButton('Анатомия')
        btn7 = types.KeyboardButton('Эволюция')
        btn8 = types.KeyboardButton('Экология')
        markup.row(btn1)
        markup.row(btn2)
        markup.row(btn3)
        markup.row(btn4)
        markup.row(btn5)
        markup.row(btn6)
        markup.row(btn7)
        markup.row(btn8)
        bot.send_message(message.chat.id, '✨Вот занятия Курса ОГЭ, доступные тебе:)')
        bot.send_message(message.chat.id, '(Выбери нужное)', reply_markup=markup)
        bot.register_next_step_handler(message, vvod)
    elif message.text == '/restart':
        bot.register_next_step_handler(message, start)
    elif message.text == '/link':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Ссылка на беседу', url='https://t.me/+Dd9o9PDg-vs5ZWEy')
        markup.row(btn1)
        bot.send_message(message.chat.id, 'Это  чат с твоим преподавателем и однокурсниками. Ко времени онлайн занятий тут будут приходить ссылки на них. А еще тут можно что-то обсудить, поделиться впечатлениями и новостями❤️', reply_markup=markup)
        bot.register_next_step_handler(message, botan)
    else:
        bot.send_message(message.chat.id, 'Не совсем понял тебя... Давай попробуем ещё раз')
        bot.register_next_step_handler(message, botan)


def zad(message):
    if message.text == 'Занятие 1':
        markup = types.InlineKeyboardMarkup()
        markups = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.InlineKeyboardButton('Скрипт', callback_data='skrp1')
        btn2 = types.InlineKeyboardButton('ДЗ', callback_data='dz1')
        btn = types.KeyboardButton('Выбрать другое занятие')
        markup.row(btn1, btn2)
        markups.row(btn)
        bot.send_message(message.chat.id, f'Занятие 1 <b>«Введение в Анатомию»</b> \n <i>Дата онлайн-занятия:22.07.2023</i> \n <i>Время: 10:00 мск</i> \n https://youtube.com/live/3qandDxgKqM?feature=share', reply_markup=markup, parse_mode="html")
        bot.send_message(message.chat.id, 'Смотри, учи, запоминай!', reply_markup=markups)
        bot.register_next_step_handler(message, hlp1)
    elif message.text == 'Занятие 2':
        markup = types.InlineKeyboardMarkup()
        markups = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.InlineKeyboardButton('Скрипт', callback_data='skrp2')
        btn2 = types.InlineKeyboardButton('ДЗ', callback_data='dz2')
        btn = types.KeyboardButton('Выбрать другое занятие')
        markup.row(btn1, btn2)
        markups.row(btn)
        bot.send_message(message.chat.id, f'Занятие 2 <b>«Остеология.Миология.Синдесмология»</b> \n <i>Дата онлайн-занятия:24.07.2023</i> \n <i>Время: 10:00 мск</i> \n https://youtube.com/live/7mt3-eoxXvk?feature=share', reply_markup=markup, parse_mode="html")
        bot.send_message(message.chat.id, 'Смотри, учи, запоминай!', reply_markup=markups)
        bot.register_next_step_handler(message, hlp1)
    elif message.text == 'Занятие 3':
        markup = types.InlineKeyboardMarkup()
        markups = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.InlineKeyboardButton('Скрипт', callback_data='skrp3')
        btn2 = types.InlineKeyboardButton('ДЗ', callback_data='dz3')
        btn = types.KeyboardButton('Выбрать другое занятие')
        markup.row(btn1, btn2)
        markups.row(btn)
        bot.send_message(message.chat.id, f'Занятие 3 <b>«Спланхнология»</b> \n <i>Дата онлайн-занятия:26.07.2023</i> \n <i>Время: 10:00 мск</i> \n https://youtube.com/live/zprqxa0a2rs?feature=share', reply_markup=markup, parse_mode="html")
        bot.send_message(message.chat.id, 'Смотри, учи, запоминай!', reply_markup=markups)
        bot.register_next_step_handler(message, hlp1)
    elif message.text == 'Занятие 4':
        markup = types.InlineKeyboardMarkup()
        markups = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.InlineKeyboardButton('Скрипт', callback_data='skrp4')
        btn2 = types.InlineKeyboardButton('ДЗ', callback_data='dz4')
        btn = types.KeyboardButton('Выбрать другое занятие')
        markup.row(btn1, btn2)
        markups.row(btn)
        bot.send_message(message.chat.id, f'Занятие 4 <b>«Кровеносная и Дыхательная системы»</b> \n <i>Дата онлайн-занятия:29.07.2023</i> \n <i>Время: 10:00 мск</i> \n https://youtube.com/live/4JnZrUOSnWw?feature=share', reply_markup=markup, parse_mode="html")
        bot.send_message(message.chat.id, 'Смотри, учи, запоминай!', reply_markup=markups)
        bot.register_next_step_handler(message, hlp1)
    elif message.text == 'Выбрать другой раздел':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Вводное занятие')
        btn2 = types.KeyboardButton('Общая биология')
        btn3 = types.KeyboardButton('Ботаника')
        btn4 = types.KeyboardButton('Грибы и Лишайники')
        btn5 = types.KeyboardButton('Зоология')
        btn6 = types.KeyboardButton('Анатомия')
        btn7 = types.KeyboardButton('Эволюция')
        btn8 = types.KeyboardButton('Экология')
        markup.row(btn1)
        markup.row(btn2)
        markup.row(btn3)
        markup.row(btn4)
        markup.row(btn5)
        markup.row(btn6)
        markup.row(btn7)
        markup.row(btn8)
        bot.send_message(message.chat.id, '✨Вот занятия Курса ОГЭ, доступные тебе:)')
        bot.send_message(message.chat.id, '(Выбери нужное)', reply_markup=markup)
        bot.register_next_step_handler(message, vvod)
    elif message.text == '/link':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Ссылка на беседу', url='https://t.me/+Dd9o9PDg-vs5ZWEy')
        markup.row(btn1)
        bot.send_message(message.chat.id, 'Это  чат с твоим преподавателем и однокурсниками. Ко времени онлайн занятий тут будут приходить ссылки на них. А еще тут можно что-то обсудить, поделиться впечатлениями и новостями❤️', reply_markup=markup)
        bot.register_next_step_handler(message, zad)
    elif message.text == '/restart':
        bot.register_next_step_handler(message, start)
    else:
        bot.send_message(message.chat.id, 'Не совсем понял тебя... Давай попробуем ещё раз')
        bot.register_next_step_handler(message, zad)

def hlp(message):
    if message.text == 'Выбрать другое занятие':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Занятие 1')
        btn2 = types.KeyboardButton('Занятие 2')
        btn3 = types.KeyboardButton('Занятие 3')
        btn4 = types.KeyboardButton('Занятие 4')
        btn5 = types.KeyboardButton('Занятие 5')
        btn6 = types.KeyboardButton('Занятие 6')
        btn7 = types.KeyboardButton('Выбрать другой раздел')
        markup.row(btn1)
        markup.row(btn2)
        markup.row(btn3)
        markup.row(btn4)
        markup.row(btn5)
        markup.row(btn6)
        markup.row(btn7)
        bot.send_message(message.chat.id, '✨Вот занятия Курса ОГЭ, доступные тебе:)')
        bot.send_message(message.chat.id, '(Выбери нужное, в нем ты найдешь запись веба, скрипт и домашку к нему)', reply_markup=markup)
        bot.register_next_step_handler(message, botan)
    elif message.text == '/restart':
        bot.register_next_step_handler(message, start)
    elif message.text == '/link':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Ссылка на беседу', url='https://t.me/+Dd9o9PDg-vs5ZWEy')
        markup.row(btn1)
        bot.send_message(message.chat.id, 'Это  чат с твоим преподавателем и однокурсниками. Ко времени онлайн занятий тут будут приходить ссылки на них. А еще тут можно что-то обсудить, поделиться впечатлениями и новостями❤️', reply_markup=markup)
        bot.register_next_step_handler(message, hlp)
    else:
        bot.send_message(message.chat.id, 'Не совсем понял тебя... Давай попробуем ещё раз')
        bot.register_next_step_handler(message, hlp)

def hlp1(message):
    if message.text == 'Выбрать другое занятие':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Занятие 1')
        btn2 = types.KeyboardButton('Занятие 2')
        btn3 = types.KeyboardButton('Занятие 3')
        btn4 = types.KeyboardButton('Занятие 4')
        btn5 = types.KeyboardButton('Выбрать другой раздел')
        markup.row(btn1)
        markup.row(btn2)
        markup.row(btn3)
        markup.row(btn4)
        markup.row(btn5)
        bot.send_message(message.chat.id, '✨Вот занятия Курса ОГЭ, доступные тебе:)')
        bot.send_message(message.chat.id, '(Выбери нужное, в нем ты найдешь запись веба, скрипт и домашку к нему)', reply_markup=markup)
        bot.register_next_step_handler(message, zad)
    elif message.text == '/restart':
        bot.register_next_step_handler(message, start)
    elif message.text == '/link':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Ссылка на беседу', url='https://t.me/+Dd9o9PDg-vs5ZWEy')
        markup.row(btn1)
        bot.send_message(message.chat.id, 'Это  чат с твоим преподавателем и однокурсниками. Ко времени онлайн занятий тут будут приходить ссылки на них. А еще тут можно что-то обсудить, поделиться впечатлениями и новостями❤️', reply_markup=markup)
        bot.register_next_step_handler(message, hlp1)
    else:
        bot.send_message(message.chat.id, 'Не совсем понял тебя... Давай попробуем ещё раз')
        bot.register_next_step_handler(message, hlp1)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'dz0':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Отправить ДЗ на проверку', url='https://t.me/baisov_islam')
        markup.row(btn1)
        bot.send_message(callback.message.chat.id, f'<a href="https://drive.google.com/drive/folders/1-xcolR4XfSY7pE00LoR3gdAhO8Hu3P3k">Вот ссылка на дз к занятию</a>', reply_markup=markup, parse_mode="html")
    if callback.data == 'dz1':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Отправить ДЗ на проверку', url='https://t.me/baisov_islam')
        markup.row(btn1)
        bot.send_message(callback.message.chat.id, f'<a href="https://drive.google.com/drive/folders/1-xcolR4XfSY7pE00LoR3gdAhO8Hu3P3k">Вот ссылка на дз к занятию</a>', reply_markup=markup, parse_mode="html")
    if callback.data == 'dz2':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Отправить ДЗ на проверку', url='https://t.me/baisov_islam')
        markup.row(btn1)
        bot.send_message(callback.message.chat.id, f'Дз  ты найдешь в скрипте \n (и не забудь отправить дз на проверку преподавателю) \n https://youtu.be/wcov8v0hrHY', reply_markup=markup, parse_mode="html")
    if callback.data == 'dz3':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Отправить ДЗ на проверку', url='https://t.me/baisov_islam')
        markup.row(btn1)
        bot.send_message(callback.message.chat.id, f'Дз  ты найдешь в скрипте \n (и не забудь отправить дз на проверку преподавателю) \n https://youtu.be/wcov8v0hrHY', reply_markup=markup, parse_mode="html")
    if callback.data == 'dz4':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Отправить ДЗ на проверку', url='https://t.me/baisov_islam')
        markup.row(btn1)
        bot.send_message(callback.message.chat.id, f'Дз  ты найдешь в скрипте \n (и не забудь отправить дз на проверку преподавателю) \n https://youtu.be/wcov8v0hrHY', reply_markup=markup, parse_mode="html")
    if callback.data == 'dz5':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Отправить ДЗ на проверку', url='https://t.me/baisov_islam')
        markup.row(btn1)
        bot.send_message(callback.message.chat.id, f'Дз  ты найдешь в скрипте \n (и не забудь отправить дз на проверку преподавателю) \n https://youtu.be/wcov8v0hrHY', reply_markup=markup, parse_mode="html")
    if callback.data == 'dz6':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Отправить ДЗ на проверку', url='https://t.me/baisov_islam')
        markup.row(btn1)
        bot.send_message(callback.message.chat.id, f'Дз  ты найдешь в скрипте \n (и не забудь отправить дз на проверку преподавателю) \n https://youtu.be/wcov8v0hrHY', reply_markup=markup, parse_mode="html")
    if callback.data == 'skrp0':
        bot.send_message(callback.message.chat.id, '<a href="https://drive.google.com/file/d/1SvW61YqWEa3lQClm2enPtsT0ByLs6dpT/view">Вот ссылка на скрипт к занятию</a>:\n', parse_mode="html")
    if callback.data == 'skrp1':
        bot.send_message(callback.message.chat.id, '<a href="https://drive.google.com/drive/folders/1-tmWfPmfVnWUIY7sKq3NIufBvfvKAmVQ">Вот ссылка на скрипт к занятию</a>:\n Обязательно распечатай скрипт перед занятием', parse_mode="html")
    if callback.data == 'skrp2':
        bot.send_message(callback.message.chat.id, '<a href="https://drive.google.com/drive/folders/1-tmWfPmfVnWUIY7sKq3NIufBvfvKAmVQ">Вот ссылка на скрипт к занятию</a>:\n Обязательно распечатай скрипт перед занятием', parse_mode="html")
    if callback.data == 'skrp3':
        bot.send_message(callback.message.chat.id, '<a href="https://drive.google.com/drive/folders/1-tmWfPmfVnWUIY7sKq3NIufBvfvKAmVQ">Вот ссылка на скрипт к занятию</a>:\n Обязательно распечатай скрипт перед занятием', parse_mode="html")
    if callback.data == 'skrp4':
        bot.send_message(callback.message.chat.id, '<a href="https://drive.google.com/drive/folders/1-tmWfPmfVnWUIY7sKq3NIufBvfvKAmVQ">Вот ссылка на скрипт к занятию</a>:\n Обязательно распечатай скрипт перед занятием', parse_mode="html")
    if callback.data == 'skrp5':
        bot.send_message(callback.message.chat.id, '<a href="https://drive.google.com/drive/folders/1-tmWfPmfVnWUIY7sKq3NIufBvfvKAmVQ">Вот ссылка на скрипт к занятию</a>:\n Обязательно распечатай скрипт перед занятием', parse_mode="html")
    if callback.data == 'skrp6':
        bot.send_message(callback.message.chat.id, '<a href="https://drive.google.com/drive/folders/1-tmWfPmfVnWUIY7sKq3NIufBvfvKAmVQ">Вот ссылка на скрипт к занятию</a>:\n Обязательно распечатай скрипт перед занятием', parse_mode="html")
    elif message.text == '/link':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Ссылка на беседу', url='https://t.me/+Dd9o9PDg-vs5ZWEy')
        markup.row(btn1)
        bot.send_message(message.chat.id, 'Это  чат с твоим преподавателем и однокурсниками. Ко времени онлайн занятий тут будут приходить ссылки на них. А еще тут можно что-то обсудить, поделиться впечатлениями и новостями❤️', reply_markup=markup)
        bot.register_next_step_handler(message, hlp)


def link(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Ссылка на беседу', url='https://t.me/+Dd9o9PDg-vs5ZWEy')
    markup.row(btn1)
    bot.send_message(message.chat.id, 'Это  чат с твоим преподавателем и однокурсниками. Ко времени онлайн занятий тут будут приходить ссылки на них. А еще тут можно что-то обсудить, поделиться впечатлениями и новостями❤️', reply_markup=markup)
    bot.register_next_step_handler(message, hlp)



@bot.message_handler(commands=['restart'])
def restart(message):
    bot.register_next_step_handler(message, start)

@bot.message_handler(commands=['info'])
def main(message):
    bot.delete_my_commands()
    bot.clear_step_handler()
    bot.send_message(message.chat.id, message)


bot.infinity_polling()
