import telebot
from telebot import types
token = '5462592415:AAEsd92P1Ni984pFC2ZK4WYdFQq8Xup-o-g'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    btn2 = types.KeyboardButton("❓ Задать вопрос")
    btn3 = types.KeyboardButton("👋 Поздороваться")
    btn4 = types.KeyboardButton("❓ Задать вопрос")
    markup.add(btn1, btn2)
    markup.add(btn3, btn4)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я бот для твоей дипломной работы на skillbox.ru".format(
                         message.from_user), reply_markup=markup)


# I can help you create and manage Telegram bots. If you're new to the Bot API, please see the manual (https://core.telegram.org/bots).
#
# You can control me by sending these commands:
#
# /newbot - create a new bot
# /mybots - edit your bots [beta]
#
# Edit Bots
# /setname - change a bot's name
# /setdescription - change bot description
# /setabouttext - change bot about info
# /setuserpic - change bot profile photo
# /setcommands - change the list of commands
# /deletebot - delete a bot
#
# Bot Settings
# /token - generate authorization token
# /revoke - revoke bot access token
# /setinline - toggle inline mode (https://core.telegram.org/bots/inline)
# /setinlinegeo - toggle inline location requests (https://core.telegram.org/bots/inline#location-based-results)
# /setinlinefeedback - change inline feedback (https://core.telegram.org/bots/inline#collecting-feedback) settings
# /setjoingroups - can your bot be added to groups?
# /setprivacy - toggle privacy mode (https://core.telegram.org/bots#privacy-mode) in groups
#
# Games
# /mygames - edit your games (https://core.telegram.org/bots/games) [beta]
# /newgame - create a new game (https://core.telegram.org/bots/games)
# /listgames - get a list of your games
# /editgame - edit a game
# /deletegame - delete an existing game

@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "👋 Поздороваться"):
        bot.send_message(message.chat.id, text="Привеет.. Спасибо что читаешь статью!)")
    elif (message.text == "❓ Задать вопрос"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Как меня зовут?")
        btn2 = types.KeyboardButton("Что я могу?")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)

    elif (message.text == "Как меня зовут?"):
        bot.send_message(message.chat.id, "У меня нет имени..")

    elif message.text == "Что я могу?":
        bot.send_message(message.chat.id, text="Поздороваться с читателями")

    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Поздороваться")
        button2 = types.KeyboardButton("❓ Задать вопрос")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")


bot.polling(none_stop=True)

# bot = telebot.TeleBot(configure.config['5462592415:AAEsd92P1Ni984pFC2ZK4WYdFQq8Xup-o-g']);
#
# bot = telebot.TeleBot('5462592415:AAEsd92P1Ni984pFC2ZK4WYdFQq8Xup-o-g');
#
# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):
#     if message.text == "/start":
#         bot.send_message(message.from_user.id, "Привет это мой первый бот. Не пинайте меня")
#         markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         item_highprice = types.KeyboardButton('ДЕШЕВЫЕ ОТЕЛИ')
#         item_lowprice = types.KeyboardButton('ДОРОГИЕ ОТЕЛИ')
#         markup_reply.add(item_lowprice, item_highprice)
#     elif message.text == "Привет":
#         bot.send_message(message.from_user.id, "Сам Привет! hello")
#     elif message.text == "/help":
#         bot.send_message(message.from_user.id, "Напиши привет")
#     else:
#         bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
#
# bot.polling(none_stop=True, interval=0)
