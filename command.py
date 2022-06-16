def get_items_hotels(bot, id, num_func):
    """
    Возвращает словарь всех найденных отелей с запросом дополнительных параметров
    :param bot:
    :param id:
    :return:
    """
    hotels_dict = dict()
    if type == 1:
        bot.send_message(id, text='Обработка команды /lowprice')
        return hotels_dict
    elif type == 2:
        bot.send_message(id, text='Обработка команды /highprice')
        return hotels_dict
    elif type == 3:
        bot.send_message(id, text='Обработка команды /bestdeal')
        return hotels_dict
    else:
        bot.send_message(id, text='Команда не поддерживается')
        return

    bot.send_message(id, text='Информация предоставлена сайтом rapidapi.com. Обработка команд ')
    return

def get_history(bot, id):
    hotels_dict = dict()
    bot.send_message(id, text='Обработка команды /history')
    return hotels_dict

def get_help(bot, id):
    bot.send_message(id, text='Обработка команды /help')
    with open('help.txt') as file:
        text = file.read()
        bot.send_message(id, text=text)

