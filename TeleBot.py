#!/usr/bin/python
# -*- coding: utf-8 -*-
import telegram
from main import Statistics
from emoji import emojize, demojize
from telegram.ext import MessageHandler, Filters, Updater, CommandHandler

updater = Updater(token='token', use_context=True) # Don't use old token, its revoked :)
dispatcher = updater.dispatcher
cls = Statistics()

flags = [{'name': 'AF', 'uni': '\U0001f1e6\U0001f1eb'},
          {'name': 'AL', 'uni': '\U0001f1e6\U0001f1f1'},
          {'name': 'DZ', 'uni': '\U0001f1e9\U0001f1ff'},
          {'name': 'AO', 'uni': '\U0001f1e6\U0001f1f4'},
          {'name': 'AR', 'uni': '\U0001f1e6\U0001f1f7'},
          {'name': 'AM', 'uni': '\U0001f1e6\U0001f1f2'},
          {'name': 'AU', 'uni': '\U0001f1e6\U0001f1fa'},
          {'name': 'AT', 'uni': '\U0001f1e6\U0001f1f9'},
          {'name': 'AZ', 'uni': '\U0001f1e6\U0001f1ff'},
          {'name': 'BS', 'uni': '\U0001f1e7\U0001f1f8'},
          {'name': 'BD', 'uni': '\U0001f1e7\U0001f1e9'},
          {'name': 'BY', 'uni': '\U0001f1e7\U0001f1fe'},
          {'name': 'BE', 'uni': '\U0001f1e7\U0001f1ea'},
          {'name': 'BZ', 'uni': '\U0001f1e7\U0001f1ff'},
          {'name': 'BJ', 'uni': '\U0001f1e7\U0001f1ef'},
          {'name': 'BT', 'uni': '\U0001f1e7\U0001f1f9'},
          {'name': 'BO', 'uni': '\U0001f1e7\U0001f1f4'},
          {'name': 'BA', 'uni': '\U0001f1e7\U0001f1e6'},
          {'name': 'BW', 'uni': '\U0001f1e7\U0001f1fc'},
          {'name': 'BR', 'uni': '\U0001f1e7\U0001f1f7'},
          {'name': 'BN', 'uni': '\U0001f1e7\U0001f1f3'},
          {'name': 'BG', 'uni': '\U0001f1e7\U0001f1ec'},
          {'name': 'BF', 'uni': '\U0001f1e7\U0001f1eb'},
          {'name': 'BI', 'uni': '\U0001f1e7\U0001f1ee'},
          {'name': 'KH', 'uni': '\U0001f1f0\U0001f1ed'},
          {'name': 'CM', 'uni': '\U0001f1e8\U0001f1f2'},
          {'name': 'CA', 'uni': '\U0001f1e8\U0001f1e6'},
          {'name': 'CF', 'uni': '\U0001f1e8\U0001f1eb'},
          {'name': 'TD', 'uni': '\U0001f1f9\U0001f1e9'},
          {'name': 'CL', 'uni': '\U0001f1e8\U0001f1f1'},
          {'name': 'CN', 'uni': '\U0001f1e8\U0001f1f3'},
          {'name': 'CO', 'uni': '\U0001f1e8\U0001f1f4'},
          {'name': 'CG', 'uni': '\U0001f1e8\U0001f1ec'},
          {'name': 'CD', 'uni': '\U0001f1e8\U0001f1e9'},
          {'name': 'CR', 'uni': '\U0001f1e8\U0001f1f7'},
          {'name': 'HR', 'uni': '\U0001f1ed\U0001f1f7'},
          {'name': 'CU', 'uni': '\U0001f1e8\U0001f1fa'},
          {'name': 'CY', 'uni': '\U0001f1e8\U0001f1fe'},
          {'name': 'CZ', 'uni': '\U0001f1e8\U0001f1ff'},
          {'name': 'CI', 'uni': '\U0001f1e8\U0001f1ee'},
          {'name': 'DK', 'uni': '\U0001f1e9\U0001f1f0'},
          {'name': 'DJ', 'uni': '\U0001f1e9\U0001f1ef'},
          {'name': 'DO', 'uni': '\U0001f1e9\U0001f1f4'},
          {'name': 'EC', 'uni': '\U0001f1ea\U0001f1e8'},
          {'name': 'EG', 'uni': '\U0001f1ea\U0001f1ec'},
          {'name': 'SV', 'uni': '\U0001f1f8\U0001f1fb'},
          {'name': 'GQ', 'uni': '\U0001f1ec\U0001f1f6'},
          {'name': 'ER', 'uni': '\U0001f1ea\U0001f1f7'},
          {'name': 'EE', 'uni': '\U0001f1ea\U0001f1ea'},
          {'name': 'ET', 'uni': '\U0001f1ea\U0001f1f9'},
          {'name': 'FK', 'uni': '\U0001f1eb\U0001f1f0'},
          {'name': 'FJ', 'uni': '\U0001f1eb\U0001f1ef'},
          {'name': 'FI', 'uni': '\U0001f1eb\U0001f1ee'},
          {'name': 'FR', 'uni': '\U0001f1eb\U0001f1f7'},
          {'name': 'GF', 'uni': '\U0001f1ec\U0001f1eb'},
          {'name': 'TF', 'uni': '\U0001f1f9\U0001f1eb'},
          {'name': 'GA', 'uni': '\U0001f1ec\U0001f1e6'},
          {'name': 'GM', 'uni': '\U0001f1ec\U0001f1f2'},
          {'name': 'GE', 'uni': '\U0001f1ec\U0001f1ea'},
          {'name': 'DE', 'uni': '\U0001f1e9\U0001f1ea'},
          {'name': 'GH', 'uni': '\U0001f1ec\U0001f1ed'},
          {'name': 'GR', 'uni': '\U0001f1ec\U0001f1f7'},
          {'name': 'GL', 'uni': '\U0001f1ec\U0001f1f1'},
          {'name': 'GT', 'uni': '\U0001f1ec\U0001f1f9'},
          {'name': 'GN', 'uni': '\U0001f1ec\U0001f1f3'},
          {'name': 'GW', 'uni': '\U0001f1ec\U0001f1fc'},
          {'name': 'GY', 'uni': '\U0001f1ec\U0001f1fe'},
          {'name': 'HT', 'uni': '\U0001f1ed\U0001f1f9'},
          {'name': 'HN', 'uni': '\U0001f1ed\U0001f1f3'},
          {'name': 'HK', 'uni': '\U0001f1ed\U0001f1f0'},
          {'name': 'HU', 'uni': '\U0001f1ed\U0001f1fa'},
          {'name': 'IS', 'uni': '\U0001f1ee\U0001f1f8'},
          {'name': 'IN', 'uni': '\U0001f1ee\U0001f1f3'},
          {'name': 'ID', 'uni': '\U0001f1ee\U0001f1e9'},
          {'name': 'IR', 'uni': '\U0001f1ee\U0001f1f7'},
          {'name': 'IQ', 'uni': '\U0001f1ee\U0001f1f6'},
          {'name': 'IE', 'uni': '\U0001f1ee\U0001f1ea'},
          {'name': 'IL', 'uni': '\U0001f1ee\U0001f1f1'},
          {'name': 'IT', 'uni': '\U0001f1ee\U0001f1f9'},
          {'name': 'JM', 'uni': '\U0001f1ef\U0001f1f2'},
          {'name': 'JP', 'uni': '\U0001f1ef\U0001f1f5'},
          {'name': 'JO', 'uni': '\U0001f1ef\U0001f1f4'},
          {'name': 'KZ', 'uni': '\U0001f1f0\U0001f1ff'},
          {'name': 'KE', 'uni': '\U0001f1f0\U0001f1ea'},
          {'name': 'XK', 'uni': '\U0001f1fd\U0001f1f0'},
          {'name': 'KW', 'uni': '\U0001f1f0\U0001f1fc'},
          {'name': 'KG', 'uni': '\U0001f1f0\U0001f1ec'},
          {'name': 'LA', 'uni': '\U0001f1f1\U0001f1e6'},
          {'name': 'LV', 'uni': '\U0001f1f1\U0001f1fb'},
          {'name': 'LB', 'uni': '\U0001f1f1\U0001f1e7'},
          {'name': 'LS', 'uni': '\U0001f1f1\U0001f1f8'},
          {'name': 'LR', 'uni': '\U0001f1f1\U0001f1f7'},
          {'name': 'LY', 'uni': '\U0001f1f1\U0001f1fe'},
          {'name': 'LT', 'uni': '\U0001f1f1\U0001f1f9'},
          {'name': 'LU', 'uni': '\U0001f1f1\U0001f1fa'},
          {'name': 'MK', 'uni': '\U0001f1f2\U0001f1f0'},
          {'name': 'MG', 'uni': '\U0001f1f2\U0001f1ec'},
          {'name': 'MW', 'uni': '\U0001f1f2\U0001f1fc'},
          {'name': 'MY', 'uni': '\U0001f1f2\U0001f1fe'},
          {'name': 'ML', 'uni': '\U0001f1f2\U0001f1f1'},
          {'name': 'MR', 'uni': '\U0001f1f2\U0001f1f7'},
          {'name': 'MX', 'uni': '\U0001f1f2\U0001f1fd'},
          {'name': 'MD', 'uni': '\U0001f1f2\U0001f1e9'},
          {'name': 'MN', 'uni': '\U0001f1f2\U0001f1f3'},
          {'name': 'ME', 'uni': '\U0001f1f2\U0001f1ea'},
          {'name': 'MA', 'uni': '\U0001f1f2\U0001f1e6'},
          {'name': 'MZ', 'uni': '\U0001f1f2\U0001f1ff'},
          {'name': 'MM', 'uni': '\U0001f1f2\U0001f1f2'},
          {'name': 'NA', 'uni': '\U0001f1f3\U0001f1e6'},
          {'name': 'NP', 'uni': '\U0001f1f3\U0001f1f5'},
          {'name': 'NL', 'uni': '\U0001f1f3\U0001f1f1'},
          {'name': 'NC', 'uni': '\U0001f1f3\U0001f1e8'},
          {'name': 'NZ', 'uni': '\U0001f1f3\U0001f1ff'},
          {'name': 'NI', 'uni': '\U0001f1f3\U0001f1ee'},
          {'name': 'NE', 'uni': '\U0001f1f3\U0001f1ea'},
          {'name': 'NG', 'uni': '\U0001f1f3\U0001f1ec'},
          {'name': 'KP', 'uni': '\U0001f1f0\U0001f1f5'},
          {'name': 'NO', 'uni': '\U0001f1f3\U0001f1f4'},
          {'name': 'OM', 'uni': '\U0001f1f4\U0001f1f2'},
          {'name': 'PK', 'uni': '\U0001f1f5\U0001f1f0'},
          {'name': 'PS', 'uni': '\U0001f1f5\U0001f1f8'},
          {'name': 'PA', 'uni': '\U0001f1f5\U0001f1e6'},
          {'name': 'PG', 'uni': '\U0001f1f5\U0001f1ec'},
          {'name': 'PY', 'uni': '\U0001f1f5\U0001f1fe'},
          {'name': 'PE', 'uni': '\U0001f1f5\U0001f1ea'},
          {'name': 'PH', 'uni': '\U0001f1f5\U0001f1ed'},
          {'name': 'PL', 'uni': '\U0001f1f5\U0001f1f1'},
          {'name': 'PT', 'uni': '\U0001f1f5\U0001f1f9'},
          {'name': 'PR', 'uni': '\U0001f1f5\U0001f1f7'},
          {'name': 'QA', 'uni': '\U0001f1f6\U0001f1e6'},
          {'name': 'RO', 'uni': '\U0001f1f7\U0001f1f4'},
          {'name': 'RU', 'uni': '\U0001f1f7\U0001f1fa'},
          {'name': 'RW', 'uni': '\U0001f1f7\U0001f1fc'},
          {'name': 'SA', 'uni': '\U0001f1f8\U0001f1e6'},
          {'name': 'SN', 'uni': '\U0001f1f8\U0001f1f3'},
          {'name': 'RS', 'uni': '\U0001f1f7\U0001f1f8'},
          {'name': 'SL', 'uni': '\U0001f1f8\U0001f1f1'},
          {'name': 'SG', 'uni': '\U0001f1f8\U0001f1ec'},
          {'name': 'SK', 'uni': '\U0001f1f8\U0001f1f0'},
          {'name': 'SI', 'uni': '\U0001f1f8\U0001f1ee'},
          {'name': 'SB', 'uni': '\U0001f1f8\U0001f1e7'},
          {'name': 'SO', 'uni': '\U0001f1f8\U0001f1f4'},
          {'name': 'ZA', 'uni': '\U0001f1ff\U0001f1e6'},
          {'name': 'KR', 'uni': '\U0001f1f0\U0001f1f7'},
          {'name': 'SS', 'uni': '\U0001f1f8\U0001f1f8'},
          {'name': 'ES', 'uni': '\U0001f1ea\U0001f1f8'},
          {'name': 'LK', 'uni': '\U0001f1f1\U0001f1f0'},
          {'name': 'SD', 'uni': '\U0001f1f8\U0001f1e9'},
          {'name': 'SR', 'uni': '\U0001f1f8\U0001f1f7'},
          {'name': 'SJ', 'uni': '\U0001f1f8\U0001f1ef'},
          {'name': 'SZ', 'uni': '\U0001f1f8\U0001f1ff'},
          {'name': 'SE', 'uni': '\U0001f1f8\U0001f1ea'},
          {'name': 'CH', 'uni': '\U0001f1e8\U0001f1ed'},
          {'name': 'SY', 'uni': '\U0001f1f8\U0001f1fe'},
          {'name': 'TW', 'uni': '\U0001f1f9\U0001f1fc'},
          {'name': 'TJ', 'uni': '\U0001f1f9\U0001f1ef'},
          {'name': 'TZ', 'uni': '\U0001f1f9\U0001f1ff'},
          {'name': 'TH', 'uni': '\U0001f1f9\U0001f1ed'},
          {'name': 'TL', 'uni': '\U0001f1f9\U0001f1f1'},
          {'name': 'TG', 'uni': '\U0001f1f9\U0001f1ec'},
          {'name': 'TT', 'uni': '\U0001f1f9\U0001f1f9'},
          {'name': 'TN', 'uni': '\U0001f1f9\U0001f1f3'},
          {'name': 'TR', 'uni': '\U0001f1f9\U0001f1f7'},
          {'name': 'TM', 'uni': '\U0001f1f9\U0001f1f2'},
          {'name': 'UG', 'uni': '\U0001f1fa\U0001f1ec'},
          {'name': 'UA', 'uni': '\U0001f1fa\U0001f1e6'},
          {'name': 'AE', 'uni': '\U0001f1e6\U0001f1ea'},
          {'name': 'GB', 'uni': '\U0001f1ec\U0001f1e7'},
          {'name': 'US', 'uni': '\U0001f1fa\U0001f1f8'},
          {'name': 'UY', 'uni': '\U0001f1fa\U0001f1fe'},
          {'name': 'UZ', 'uni': '\U0001f1fa\U0001f1ff'},
          {'name': 'VU', 'uni': '\U0001f1fb\U0001f1fa'},
          {'name': 'VE', 'uni': '\U0001f1fb\U0001f1ea'},
          {'name': 'VN', 'uni': '\U0001f1fb\U0001f1f3'},
          {'name': 'EH', 'uni': '\U0001f1ea\U0001f1ed'},
          {'name': 'YE', 'uni': '\U0001f1fe\U0001f1ea'},
          {'name': 'ZM', 'uni': '\U0001f1ff\U0001f1f2'},
          {'name': 'ZW', 'uni': '\U0001f1ff\U0001f1fc'}]

def start(update, context):
    start_msg_ar = "للبدء ارسل علم دولتك وسوف أرد عليك بأحدث المعلومات عن فيروس كورونا."
    Start_msg = "Covid19 bot created By FAR7AN & Moha369, Send your country flag to get the latest information about Corona virus in your country. \n" + start_msg_ar
    context.bot.send_message(chat_id=update.effective_chat.id, text=Start_msg)

Start = CommandHandler('start', start)
dispatcher.add_handler(Start)

def get_country(msg):
    flag_uni = msg.encode('unicode-escape').decode('utf-8')
    for flag in flags:
        x = flag['uni'].encode('unicode-escape').decode('utf-8')
        if x == flag_uni:
            return flag['name']
        else:
            continue
        return None

def get_message(stats):
    cases = emojize(f":red_circle: Total Cases : {stats['total_cases']}", use_aliases = True)
    deaths = emojize(f":black_circle: Deaths : {stats['total_deaths']}", use_aliases = True)
    recovered = emojize(f":white_circle: Recovered : {stats['recovered']}", use_aliases = True)
    serious = emojize(f":yellow_circle: Serious : {stats['total_serious']}", use_aliases = True)
    active = emojize(f":green_circle: Active : {stats['total_active_cases']}", use_aliases = True)
    message = '\n'.join([cases, deaths, recovered, serious, active])
    return message

def country(update, context):
    msg = update.message.text
    country = get_country(msg)
    if not country:
        context.bot.send_message(chat_id=update.effective_chat.id, text='Country not found, Contact creators on instagram to add your country.')
    stats = cls.by_country(country)
    message = get_message(stats)
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

send = MessageHandler(Filters.text, country)
dispatcher.add_handler(send)

updater.start_polling()
