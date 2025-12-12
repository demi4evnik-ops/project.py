import telebot
import datetime
from json_parser import tema



BOT_TOKEN = "8259610181:AAFehPMv3chN34RzfLtGrw44Wr3yflwy1Z8"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'begin'])
def start(message):
    bot.send_message(message.chat.id , "Hello")


@bot.message_handler(commands=['date'])
def date(message):
    t = datetime.datetime.now()
    bot.send_message(message.chat.id, f'Сегодня {t}')


@bot.message_handler(commands=['krosword'])
def krosword(message):
    
    bot.send_message(message.chat.id, "Введите на какую тему вы хотите кросворд доступные темы: кино,история,земля")
    bot.register_next_step_handler_by_chat_id(message.chat.id, callback = choose_tema)
    
def choose_tema(message):
    text = message.text
    data = tema(text)
    if data is None:
        bot.send_message(message.chat.id, "Вы ввели не сущесвующую тему!")
        krosword(message)
    else:    
        ask_1(message,data)

def ask_1(message, data):
    bot.send_message(message.chat.id,data[0]["question"])
    bot.register_next_step_handler_by_chat_id(message.chat.id,ask_2, data)
    real_answer = data[0]["answer"].lower()
    





def ask_2(message, data):
    user_answer = message.text.lower()
    real_answer = data[0]["answer"].lower()
    if user_answer == real_answer:
       bot.send_message(message.chat.id, "Это был правильный ответ")
       bot.send_message(message.chat.id,data[1]["question"])
       bot.register_next_step_handler_by_chat_id(message.chat.id,ask_3, data)
    elif not user_answer == '/stop':
        bot.send_message(message.chat.id, "Ответ не правильный.Попробуйте еще раз.")
        bot.register_next_step_handler_by_chat_id(message.chat.id,ask_2, data)
    

def ask_3(message, data):
    user_answer = message.text.lower()
    real_answer = data[1]["answer"].lower()
    if user_answer == real_answer:
       bot.send_message(message.chat.id, "Это был правильный ответ")
       bot.send_message(message.chat.id,data[2]["question"])
       bot.register_next_step_handler_by_chat_id(message.chat.id,ask_4, data)
    elif not user_answer == '/stop':
        bot.send_message(message.chat.id, "Ответ не правильный.Попробуйте еще раз.")
        bot.register_next_step_handler_by_chat_id(message.chat.id,ask_3, data)


def ask_4(message, data):
    user_answer = message.text.lower()
    real_answer = data[2]["answer"].lower()
    if user_answer == real_answer:
       bot.send_message(message.chat.id, "Это был правильный ответ")
       bot.send_message(message.chat.id,data[3]["question"])
       bot.register_next_step_handler_by_chat_id(message.id,ask_5, data)
    elif not user_answer == '/stop':
        bot.send_message(message.chat.id, "Ответ не правильный.Попробуйте еще раз.")
        bot.register_next_step_handler_by_chat_id(message.chat.id,ask_4, data)

def ask_5(message, data):
    user_answer = message.text.lower()
    real_answer = data[3]["answer"].lower()
    if user_answer == real_answer:
       bot.send_message(message.chat.id, "Это был правильный ответ")
       bot.send_message(message.chat.id,data[4]["question"])
       bot.register_next_step_handler_by_chat_id(message.chat.id,ask_6, data)
    elif not user_answer == '/stop':
        bot.send_message(message.chat.id, "Ответ не правильный.Попробуйте еще раз.")
        bot.register_next_step_handler_by_chat_id(message.chat.id,ask_5, data)

def ask_6(message,data):
    user_answer = message.text.lower()
    real_answer = data[3]["answer"].lower()
    if user_answer == real_answer:
       bot.send_message(message.chat.id, "Это был правильный ответ")
    elif not user_answer == '/stop':
         bot.send_message(message.chat.id, "Ответ не правильный.Попробуйте еще раз.")
         bot.register_next_step_handler_by_chat_id(message.chat.id,ask_6, data)
    




    
@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, text=f"Sorry bye")







bot.polling()


