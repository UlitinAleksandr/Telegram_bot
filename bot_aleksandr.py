import telebot
import parser_currency
from telebot import types

bot = telebot.TeleBot("5103795659:AAFruz4cZExRCRSnvg9mQObTTfcUQEAOHuk")

@bot.message_handler(content_types=["text"])
def get_text_message(message):

    keyboard = types.InlineKeyboardMarkup()
    key_lira = types.InlineKeyboardButton(text="Turkish lira", callback_data="lira")
    keyboard.add(key_lira)
    key_dollar = types.InlineKeyboardButton(text="American dollar", callback_data="dollar")
    keyboard.add(key_dollar)
    key_euro = types.InlineKeyboardButton(text="Euro", callback_data="euro")
    keyboard.add(key_euro)
    bot.send_message(message.from_user.id, text="Choose currency", reply_markup=keyboard)

    @bot.callback_query_handler(func=lambda call: True)
    def callback_worker(call):
        pc = parser_currency
        if call.data == "lira":
            msg = pc.check(pc.LIRA_RUB)
        elif call.data == "euro":
            msg = pc.check(pc.EURO_RUB)
        elif call.data == "dollar":
            msg = pc.check(pc.DOLLAR_RUB)
        bot.send_message(call.message.chat.id, msg)


bot.polling(none_stop=True, interval=0)
