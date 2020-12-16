import Bitcoin_Price
from telegram.ext import Updater , CommandHandler ,MessageHandler,Filters
import requests
from telegram import ReplyKeyboardMarkup
from time import sleep
updater = Updater('954466558:AAE0ORspoWzVNmEQnin7oHq56236UnG7yvc')

################################################ start ###################################
def start(bot,updater):
    
    
    print(updater.message.chat.username)
    chat_id=updater.message.chat_id
    bot.sendMessage(chat_id,"سلام به ربات حامد خوش آمدید   ")




################################################# save data #####################################
    file2write = open("d.txt","w")
    d=f"chat_id:{updater.message.chat_id} \n first_name:{updater.message.chat.first_name} "
    file2write.write(d)
    file2write.close()



################################               send image  #######################################

def img(bot,updater):
    chat_id = updater.message.chat_id
    bot.sendPhoto(chat_id,'https://images.app.goo.gl/rrrJ7Cva5MWNPJZe6')

#########################################  send image from local host #####################
def img2(bot,updater):
    url='https://api.telegram.org/bot954466558:AAE0ORspoWzVNmEQnin7oHq56236UnG7yvc/sendPhoto'
    files={'photo' :open('img/ss.jpg','rb')}
    data={'chat_id': updater.message.chat_id}
    requests.post(url,files=files,data=data)
################################################ send image from localhost  *2* ##############

def img3(bot,updater):
    chat_id = updater.message.chat_id
    bot.sendPhoto(chat_id,open('img/g.jpg','rb'))

 ###############################################    send help ###############################

def help(bot, updater):
    chat_id = updater.message.chat_id
    bot.sendMessage(chat_id, "سلام به ربات حامد خوش آمدید برای دریافت راهنما دکمه ی help رو بزنید")

#####################################   user profile ################################
def up(bot,updater):
    chat_id = updater.message.chat_id
    photos=bot.getUserProfilePhotos(chat_id)
    #bot.sendPhoto(chat_id,'AgACAgQAAxUAAV_XxS3GGZEZNRB8aqo-AaOBvDmKAAJ3qDEbHlDnHdWQP4-90TWPqBMjKl0AAwEAAwIAA2EAA6-DAAIeBA')
    for i in range(photos.total_count):
        chat_id=updater.message.chat_id
        photo=photos.photos[i][0].file_id
        bot.sendPhoto(chat_id,photo)

############################################ inline keyword #############################
def key(bot,updater):
    keyboard=[
        ["hamed","amir"],
        ["farhan","ehsan"],
        ["قیمت بیت کوین"]

    ]
    chat_id =updater.message.chat_id
    #bot.sendChatAction(chat_id,"typing")
    bot.sendMessage(chat_id,"لطفا انتخاب کنید:",reply_markup=ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True))

######################### message handler ##########################

def txt(bot,updater):
    chat_id = updater.message.chat_id
    u=updater.message.text


    if u=="سلام":
         bot.sendMessage(chat_id,"salam")
    elif u=="چطوری؟":
         bot.sendMessage(chat_id,"merci تو چطوری؟")
    elif u=="خوبی؟":
         bot.sendMessage(chat_id,"merci تو چطوری؟")

    elif u=="منم خوبم":
         bot.sendMessage(chat_id,"همیشه شاد و خندون ببینیمت")
    elif u=="عالی":
         bot.sendMessage(chat_id,"همیشه شاد وخندون ببینیمت")
    elif u == "bot":
        bot.sendMessage(chat_id, "جونم عزیزم")
    elif u == "ربات":
        bot.sendMessage(chat_id, "جونم عزیزم")
    elif u== "bot" :
         bot.sendMessage(chat_id, "جونم عزیزم")
    elif u=="دوست دارم":
        bot.sendMessage(chat_id ,"فدا عشقم ")
    elif u=="hamed":
        bot.sendPhoto(chat_id,open('img/hamed.jpg','rb'))
    elif u=="ehsan":
        bot.sendPhoto(chat_id,open('img/ehsan.jpg','rb'))
    elif u=="amir":
        bot.sendPhoto(chat_id,open('img/amir.jpg','rb'))
    elif u=="farhan":
        bot.sendPhoto(chat_id,open('img/farhan.jpg','rb'))
    elif u == "قیمت بیت کوین":
        bot.sendMessage(chat_id,Bitcoin_Price.Get_Price())
    else:
         bot.sendMessage(chat_id,"متوجه نمیشم عزیزم بقیه پی ام ها برام تعریف نشدن")




   #bot.sendMessage(chat_id, "salam")

################################################# getChat group #####################
##################################################   commands ##################################

start_command = CommandHandler("start",start)
img_command = CommandHandler("img",img)
img2_command = CommandHandler("img2",img2)
img3_command=CommandHandler("img3",img3)
pro_command=CommandHandler("pro",up)
key_command=CommandHandler("key",key)
txt_command=MessageHandler(Filters.private,txt)

################################################## dispatcher #################
updater.dispatcher.add_handler(start_command)
updater.dispatcher.add_handler(img_command)
updater.dispatcher.add_handler(img2_command)
updater.dispatcher.add_handler(img3_command)
updater.dispatcher.add_handler(pro_command)
updater.dispatcher.add_handler(key_command)
updater.dispatcher.add_handler(txt_command)

updater.start_polling()
updater.idle()