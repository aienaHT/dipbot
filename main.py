# Edit Bots
# Основные команды
# /start - команда старт
# /lowprice - топ самых дешёвых отелей в городе
# /highprice - топ самых дорогих отелей в городе
# /bestdeal - топ отелей, наиболее подходящих по цене и расположению
# /history - история поиска отелей
# /help - помощь по командам бота

# Текстовые команды
# hello-world - команда приветствия

import telebot
from telebot import types

from lowprice import get_items_lowprice
from highprice import get_items_highprice
from bestdeal import get_items_bestdeal
from history import get_items_history
from help import get_help

token = '5462592415:AAEsd92P1Ni984pFC2ZK4WYdFQq8Xup-o-g'

bot = telebot.TeleBot(token)

def markup_btn():
    item_lowprice = types.KeyboardButton("👋 Дешевые отели")
    item_highprice = types.KeyboardButton("👋 Дорогие отели")
    item_suitable = types.KeyboardButton("👋 Подходящие отели")
    item_history = types.KeyboardButton("👋 История поиска")
    item_help = types.KeyboardButton("❓ Команды")
    markup_button = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup_button.add(item_lowprice, item_highprice)
    markup_button.add(item_suitable, item_history)
    markup_button.add(item_help)
    return markup_button

def markup_inl():
    item_yes = types.InlineKeyboardButton("Да", callback_data='yes')
    item_no = types.InlineKeyboardButton("Нет", callback_data='no')
    markup_inline = types.InlineKeyboardMarkup(row_width=2)
    markup_inline.add(item_yes, item_no)
    return markup_inline

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
   try:
       if call.message:
           if call.data == "yes":
               bot.edit_message_reply_markup(chat_id=call.message.chat.id , message_id=call.message.id , reply_markup=None)
               bot.send_message(call.message.chat.id, "Выводим информацию с фотографиями")
           if call.data == "no":
               bot.edit_message_reply_markup(chat_id=call.message.chat.id , message_id=call.message.id , reply_markup=None)
               bot.send_message(call.message.chat.id, "Выводим информацию без фотографий")
   except Exception as e:
       print(repr(e))

@bot.message_handler(commands=['start'])
def start(message):
    markup_button = markup_btn()
    bot.send_message(message.chat.id,
                     text="Привет! Я бот дипломной работы на skillbox.ru".format(
                         message.from_user), reply_markup=markup_button)

@bot.message_handler(content_types=['text'])
def func(message):
    print(message.text.lower())
    if message.text == "👋 Дешевые отели" or message.text == '/lowprice':
        get_items_lowprice(bot, message.chat.id)
        markup_inline = markup_inl()
        bot.send_message(message.chat.id,
                         text="Вывести фотографии для каждого отеля ?".format(
                             message.from_user), reply_markup=markup_inline)
    elif message.text == "👋 Дорогие отели" or message.text == '/highprice':
        get_items_highprice(bot, message.chat.id)
        markup_inline = markup_inl()
        bot.send_message(message.chat.id,
                         text="Вывести фотографии для каждого отеля ?".format(
                             message.from_user), reply_markup=markup_inline)
    elif message.text == "👋 Подходящие отели" or message.text == '/bestdeal':
        get_items_bestdeal(bot, message.chat.id)
        markup_inline = markup_inl()
        bot.send_message(message.chat.id,
                         text="Вывести фотографии для каждого отеля ?".format(
                             message.from_user), reply_markup=markup_inline)
    elif message.text == "👋 История поиска" or message.text == '/history':
        get_items_history(bot, message.chat.id)
    elif message.text == "❓ Команды" or message.text == '/help':
        get_help(bot, message.chat.id)
    elif message.text == "/hello-world" or message.text.lower() == 'привет':
        bot.send_message(message.chat.id, text='Name: BotHotels')


bot.polling(none_stop=True)
