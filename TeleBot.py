import telegram
from Covid import Statistics
from telegram.ext import MessageHandler, CommandHandler, Filters, Updater

updater = Updater(token='1220830296:AAFpxTw3yYE_URG0OZxeQFp7BgjXKWomKDc', use_context=True)
dispatcher = updater.dispatcher
cls = Statistics()

def start(update, context):
    start_msg_ar = "للبدء ارسل علم دولتك وسوف أرد عليك بأحدث المعلومات عن فيروس كورونا."
    Start_msg = "Covid19 bot created By FAR7AN & Moha369, Send your country flag to get the latest information about Corona virus in your country. \n" + start_msg_ar
    context.bot.send_message(chat_id=update.effective_chat.id, text=Start_msg)

Start = CommandHandler('start', start)
dispatcher.add_handler(Start)

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
        context.bot.send_message(chat_id=update.effective_chat.id, text='Country not supported yet, contact creators to add your country...')


Send = MessageHandler(Filters.text, Send)
dispatcher.add_handler(Send)

updater.start_polling()
