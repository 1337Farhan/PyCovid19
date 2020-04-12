import telegram
from Covid import Statistics
from telegram.ext import MessageHandler, Filters, Updater




updater = Updater(token='1220830296:AAFpxTw3yYE_URG0OZxeQFp7BgjXKWomKDc', use_context=True)

dispatcher = updater.dispatcher

def Send(update, context):
    print(update.message)
    if f'{update.message.text}'.lower() == 'hello':
        context.bot.send_message(chat_id=update.effective_chat.id, text="Hi")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text='Error')


Send = MessageHandler(Filters.text, Send)
dispatcher.add_handler(Send)

updater.start_polling()
