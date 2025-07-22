import telebot
from telebot import types
from flask import Flask, request

bot = telebot.TeleBot('7653915501:AAHVJzOa7Y8IVck5qzy0i-bRNz1rd08lKyw')
app = Flask(__name__)

WEBHOOK_URL = 'https://tweakbot.onrender.com/'

bot.remove_webhook()
bot.set_webhook(url=WEBHOOK_URL)

@app.route('/', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return '', 200
    else:
        return 'Unsupported Media Type', 415

if  __name__ == '_main':
    app.run(host='0.0.0.0', port=10000)
    
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Сборки')
    markup.row(btn1)
    btn3 = types.KeyboardButton('Помощь и вопросы')
    markup.row(btn3)
    bot.send_message(message.chat.id, 'Привет, чем могу помочь?', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text.lower() == 'сборки')
def cborka(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('ПД 2.1')
    btn2 = types.KeyboardButton('Синяя фпс ап')
    btn3 = types.KeyboardButton('Красная фпс ап')
    btn4 = types.KeyboardButton('Розовая')
    btn5 = types.KeyboardButton('Черная')
    btn6 = types.KeyboardButton('1243')
    btn7 = types.KeyboardButton('/start')
    markup.row(btn1)
    markup.row(btn2, btn3)
    markup.row(btn4)
    markup.row(btn5)
    markup.row(btn6)
    markup.row(btn7)
    bot.send_message(message.chat.id, 'Выбери чит который вас интерисует', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text.lower() == 'помощь и вопросы')
def helping(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Как установить читы')
    btn2 = types.KeyboardButton('Как обойти бан по лаунчеру')
    btn3 = types.KeyboardButton('123')
    btn4 = types.KeyboardButton('	456')
    btn5 = types.KeyboardButton('/start')
    markup.row(btn1)
    markup.row(btn2, btn3)
    markup.row(btn4)
    markup.row(btn5)
    bot.send_message(message.chat.id, 'Выберите вопрос который вас интерисует', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text.lower() == 'как установить читы')
def gaid(message):
    bot.send_message(message.chat.id, 'В данном гайде https://youtu.be/DtlY-eWkxs8?si=-pxv0ajOCl3UhZ8y')

@bot.message_handler(func=lambda message: message.text.lower() == 'что делать если вылетает?')
def crash(message):
    bot.send_message(message.chat.id, 'Попробуйте переустановить лаунчер или же напишите в телеграм @gullsssss')

@bot.message_handler(func=lambda message: message.text.lower() == 'когда новая сборка?')
def new(message):
    bot.send_message(message.chat.id, 'Новая сборка выходит не по графику, следите за каналом https://t.me/sborkiforrotyanka')

@bot.message_handler(func=lambda message: message.text.lower() == 'можно ли заказать сборку?')
def order(message):
    bot.send_message(message.chat.id, 'Да, заказы принимаются в телеграм @gullsssss')

@bot.message_handler(func=lambda message: message.text.lower() == 'розовая')
def forward_message(message):
    CHANNEL_ID = -1002416731182
    MESSAGE_ID = 7

    bot.copy_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID , message_id=MESSAGE_ID)

@bot.message_handler(func=lambda message: message.text.lower() == 'пд 2.1')
def forward_message(message):
    CHANNEL_ID = -1002416731182
    MESSAGE_ID = 3

    bot.copy_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID , message_id=MESSAGE_ID)

@bot.message_handler(func=lambda message: message.text.lower() == 'синяя фпс ап')
def forward_message(message):
    CHANNEL_ID = -1002416731182
    MESSAGE_ID = 18

    bot.copy_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID , message_id=MESSAGE_ID)

@bot.message_handler(func=lambda message: message.text.lower() == 'красная фпс ап')
def forward_message(message):
    CHANNEL_ID = -1002416731182
    MESSAGE_ID = 12

    bot.copy_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID , message_id=MESSAGE_ID)

@bot.message_handler(func=lambda message: message.text.lower() == 'черная')
def forward_message(message):
    CHANNEL_ID = -1002416731182
    MESSAGE_ID = 46

    bot.copy_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=MESSAGE_ID)

@bot.message_handler(func=lambda message: message.text.lower() == '1243')
def forward_message(message):
     CHANNEL_ID = -1002416731182
     MESSAGE_ID = 56

     bot.copy_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=MESSAGE_ID)

bot.polling(none_stop=True)
