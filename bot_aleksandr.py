import telebot
import parser_currency
from telebot import types

bot = telebot.TeleBot("5123285996:AAHbe3pz1bgjBpszNBDIsI003htyjXp5mxs")


@bot.message_handler(content_types=["text"])
def get_text_message(message):

    if message.text == "/start" or message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, я бот который показывает актуальный курс валюты")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю... Напиши: Привет")

    keyboard = types.InlineKeyboardMarkup()
    key_lira = types.InlineKeyboardButton(text="Турецкая Лира", callback_data="lira")
    keyboard.add(key_lira)
    key_dollar = types.InlineKeyboardButton(text="Американский доллар", callback_data="dollar")
    keyboard.add(key_dollar)
    key_euro = types.InlineKeyboardButton(text="Евро", callback_data="euro")
    keyboard.add(key_euro)

    bot.send_message(message.from_user.id, text="Выбери валюту", reply_markup=keyboard)

    @bot.callback_query_handler(func=lambda call: True)
    def callback_worker(call):
        if call.data == "lira":
            msg = parser_currency.check_currency_lira()
            bot.send_message(call.message.chat.id, msg)


bot.polling(none_stop=True, interval=0)
