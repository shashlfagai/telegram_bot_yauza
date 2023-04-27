import telebot
from telebot import types

#создаем и обозначаем бота
bot = telebot.TeleBot('6228080739:AAHX6H7ISzUHj1pqoOzxwDCjV0KEkEwuNzE')

#создаем команду старт,с кнопки основного меню и пишем приветственное сообщение
@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Для покупателей!']])
    keyboard.add(*[types.KeyboardButton(name) for name in ['Для дизайнеров!']])
    keyboard.add(*[types.KeyboardButton(name) for name in ['Для стилистов и фотографов!']])
    bot.send_message(message.chat.id, 'Здравствуйте, мы открыты с 12 до 21 ежедневно. Москва, Лучников переулок 4с1 (метро "Китай-город"), вход в арке слева ✨', reply_markup=keyboard)

#задаем на прием текстовое сообщение и присваеваем действия кноакам главного меню
@bot.message_handler(content_types=['text'])
def message(message):

#Функционал кнопки "Для покупателей!"    
    if message.text == 'Для покупателей!':
        keyboardgostart = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboardgostart.add(*[types.KeyboardButton(name) for name in ['Как оплатить заказ?']])
        keyboardgostart.add(*[types.KeyboardButton(name) for name in ['Информация по доставке']])
        keyboardgostart.add(*[types.KeyboardButton(name) for name in ['Подарочный сертификат']])
        keyboardgostart.add(*[types.KeyboardButton(name) for name in ['Вернуться в главное меню!']])
        bot.send_message(message.chat.id, 'Выберите кнопку', reply_markup=keyboardgostart)

#Функционал кнопки "Для дизайнеров!"    
    elif message.text == 'Для дизайнеров!':
        keyboardgostart = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboardgostart.add(*[types.KeyboardButton(name) for name in ['Хочу сотрудничать с YAUZA STORE!']])
        keyboardgostart.add(*[types.KeyboardButton(name) for name in ['Уже работаю с YAUZA STORE!']])
        keyboardgostart.add(*[types.KeyboardButton(name) for name in ['Вернуться в главное меню!']])
        bot.send_message(message.chat.id, 'Выберите кнопку', reply_markup=keyboardgostart)

#Функционал кнопки "Для стилистов и фотографов!"    
    elif message.text == 'Для стилистов и фотографов!':
        keyboardgostart = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboardgostart.add(*[types.KeyboardButton(name) for name in ['Хочу взять в аренду вещи, для съемки!']])
        keyboardgostart.add(*[types.KeyboardButton(name) for name in ['Вернуться в главное меню!']])
        bot.send_message(message.chat.id, 'Выберите кнопку', reply_markup=keyboardgostart)

#Функционал кнопки "Вернуться в главное меню!"
    elif message.text == 'Вернуться в главное меню!':
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['Для покупателей!']])
        keyboard.add(*[types.KeyboardButton(name) for name in ['Для дизайнеров!']])
        keyboard.add(*[types.KeyboardButton(name) for name in ['Для стилистов и фотографов!']])
        bot.send_message(message.chat.id, 'Выберите категорию', reply_markup=keyboard)

#Задаем функционал кнопкам в подменю "Для покупателей"
#Функционал кнопки "Как оплатить заказ" 
    elif message.text == 'Как оплатить заказ?':
        keyboardgostart = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboardgostart.add(*[types.KeyboardButton(name) for name in ['Вернуться в главное меню!']])
        bot.send_message(message.chat.id, 'Оплатить заказ можно онлайн переводом по номеру телефона 89670888169 на любой привязанный банк', reply_markup=keyboardgostart)

#Функционал кнопки "'Информация по доставке'" 
    elif message.text == 'Информация по доставке':
        keyboardgostart = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboardgostart.add(*[types.KeyboardButton(name) for name in ['Быстрая доставка по Москве, в пределах МКАД']])
        keyboardgostart.add(*[types.KeyboardButton(name) for name in ['Доставка по России и в ближайшее модмосковье']])
        keyboardgostart.add(*[types.KeyboardButton(name) for name in ['Вернуться в главное меню!']])
        bot.send_message(message.chat.id, 'Куда нужно доставить?',  reply_markup=keyboardgostart)

#Функционал кнопки "Подарочный сертификат" 
    elif message.text == 'Подарочный сертификат':
        keyboardgostart = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboardgostart.add(*[types.KeyboardButton(name) for name in ['Заказать подарочный сертификат!']])
        keyboardgostart.add(*[types.KeyboardButton(name) for name in ['Вернуться в главное меню!']])
        bot.send_message(message.chat.id, 'Для оформления сертификата нам потребуется следующая информация:\nОт кого\nКому\nИ куда направить готовый электронный сертификат\n\nОплатить заказ можно онлайн переводом по номеру телефона или наличными в магазине YAUZA STORE.', reply_markup=keyboardgostart)

#Задаем функционал кнопкам в подменю "Информация по доставке"
#Функционал кнопки "Быстрая доставка по Москве, в пределах МКАД" 
    elif message.text == 'Быстрая доставка по Москве, в пределах МКАД':
        keyboardgostart = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboardgostart.add(*[types.KeyboardButton(name) for name in ['Вернуться в главное меню!']])
        bot.send_message(message.chat.id, 'Мы отправляем заказы по Москве, в пределах МКАД курьерской службой (+300₽)\nПризаказе до 6 часов вечера, доставка возможна в день заказа', reply_markup=keyboardgostart)

#Функционал кнопки "Доставка по России и в ближайшее модмосковье" 
    elif message.text == 'Доставка по России и в ближайшее модмосковье':
        keyboardgostart = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboardgostart.add(*[types.KeyboardButton(name) for name in ['Вернуться в главное меню!']])
        bot.send_message(message.chat.id, 'В ближайшее Подмосковье и в другие города мы доставляем заказы службой доставки сдэк до пункта выдачи (+300₽)', reply_markup=keyboardgostart)

#Задаем функционал кнопкам в подменю "Подарочный сертификат"
#Функционал кнопки "Заказать подарочный сертификат!" 
    elif message.text == 'Заказать подарочный сертификат!':
        keyboardgostart = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboardgostart.add(*[types.KeyboardButton(name) for name in ['Вернуться в главное меню!']])
        bot.send_message(message.chat.id, 'Пожалуйста, напишите следующее:\nОт чьего минеи будет вручен сертификат\nКому преднозначается сертификат\nКуда направить готовый электронный сертификат (почта, мэссенджер, и т.д.)', reply_markup=keyboardgostart)
        
bot.polling(none_stop=True, interval=0)