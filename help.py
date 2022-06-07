def get_help(bot, id):
    bot.send_message(id, text='Обработка команды /help')
    with open('help.txt') as file:
        text = file.read()
        bot.send_message(id, text=text)
