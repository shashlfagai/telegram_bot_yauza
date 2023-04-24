import telebot
from telebot import types

#создаем и обозначаем бота
bot = telebot.TeleBot('5562033158:AAFwl0KNn4EqRtp2DHXrs7TqWyjSyEDjk3s')

#создаем команду старт,с кнопки основного меню и пишем приветственное сообщение
@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Для покупателей!', 'Для дизайнеров!', 'Для стилистов и фотографов!']])
    bot.send_message(message.chat.id, 'Здравствуйте, мы открыты с 12 до 21 ежедневно. Москва, Лучников переулок 4с1 (метро "Китай-город"), вход в арке слева ✨', reply_markup=keyboard)

#задаем на прием текстовое сообщение и присваеваем действия кноакам главного меню
@bot.message_handler(content_types=['text'])
def message(message):
    
    if message.text == 'Для покупателей!':
        keyboardgostart = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboardgostart.add(*[types.KeyboardButton(name) for name in ['Как оплатить заказ?' , 'Информация по доставке', 'Подарочный сертификат']])
        keyboardgostart.add(*[types.KeyboardButton(name) for name in ['Назад']])
        bot.send_message(message.chat.id, 'Выберите кнопку', reply_markup=keyboardgostart)
    
    elif message.text == 'Для дизайнеров!':
        bot.send_message(message.chat.id, 'Сслыка на группу')
    
    elif message.text == 'Для стилистов и фотографов!':
        bot.send_message(message.chat.id, 'Пока!')        
    
    elif message.text == 'Как оплатить заказ?':
        keyboardgostart = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboardgostart.add(*[types.KeyboardButton(name) for name in ['Назад']])
        bot.send_message(message.chat.id, 'Оплатить заказ можно онлайн переводом по номеру телефона 89670888169 на любой привязанный банк', reply_markup=keyboardgostart)

bot.polling(none_stop=True, interval=0)