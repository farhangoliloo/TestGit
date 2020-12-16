'''This bot is a digital hub currency price notification bot  , Dcb0101 = Digital currency binary 0101 '''
from telegram.ext import Updater , CommandHandler ,MessageHandler,Filters
import requests
import Bitcoin_Price
import Bot_key
from telegram import ReplyKeyboardMarkup

updater = Updater(Bot_key.bot_key)            #save and start Token_bot

# start def bot

def start (bot,updater) :
    print(updater.message.chat.username , updater.message.chat_id)
    chat_id = updater.message.chat_id
    bot.sendMessage(chat_id , "سلام به ربات اطلاع رسانی قیمت ارز های دیجیتال خوش آمدید " )

#def inline keyboard 

def key(bot,updater):
    keyboard=[
        ["قیمت بیت کوین"]

    ]
    chat_id = updater.message.chat_id
    
    bot.sendMessage(chat_id,"لطفا انتخاب کنید:",reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard = True,one_time_keyboard = True))
   
# def txt Messagehandler

def txt(bot,updater):
    chat_id = updater.message.chat_id
    u = updater.message.text
    if u == 'قیمت بیت کوین':
        bot.sendMessage(chat_id,Bitcoin_Price.Get_Price())
    elif u == 'key':
        True
    else:
         bot.sendMessage(chat_id,"متوجه نمیشم عزیزم بقیه پی ام ها برام تعریف نشدن") 

############################ group chat
def group(bot, updater):
    chat_id = updater.message.chat_id
    u = updater.message.text
    if u == 'قیمت بیت کوین':
        bot.sendMessage(chat_id,Bitcoin_Price.Get_Price())
    elif u == 'key':
        True
    else:
         True
# command handlers

start_command = CommandHandler("start",start)

key_command = CommandHandler("key",key)

#Messagehandler
txt_command=MessageHandler(Filters.private,txt)
group_command = MessageHandler(Filters.group,group)
# dispatchers

updater.dispatcher.add_handler(start_command)

updater.dispatcher.add_handler(key_command)
updater.dispatcher.add_handler(txt_command) 
updater.dispatcher.add_handler(group_command)

updater.start_polling()       #run
updater.idle()