import telegram
from Covid import Statistics
from telegram.ext import MessageHandler, Filters, Updater

updater = Updater(token='1220830296:AAFpxTw3yYE_URG0OZxeQFp7BgjXKWomKDc', use_context=True)
dispatcher = updater.dispatcher
cls = Statistics()

def Send(update, context):
    msg = update.message
    print(msg)

    countries = cls.countries_info
    list = []
    for country in countries:
        data = country.get("code", "")
        list.append(data)
        msg_caps = msg.text.upper()
    if msg_caps in list:
        cases = cls.by_country(msg_caps)['total_cases']
        context.bot.send_message(chat_id=update.effective_chat.id, text=cases)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text='Country not Found')


Send = MessageHandler(Filters.text, Send)
dispatcher.add_handler(Send)

updater.start_polling()
