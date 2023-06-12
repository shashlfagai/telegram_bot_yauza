import telebot
from telebot import types


#создаем и обозначаем бота
bot = telebot.TeleBot('6228080739:AAHX6H7ISzUHj1pqoOzxwDCjV0KEkEwuNzE')


# Создаем функцию для создания кнопок
def func_of_buttons(name_of_the_button, message, *args, answer='Выберите кнопку'):
    if message.text == str(name_of_the_button):
# Создаем экземпляр ReplyKeyboardMarkup с параметром resize_keyboard=True
        keyboardgostart = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)        
# Создаем список кнопок, используя значения из аргументов *args
        buttons = [types.KeyboardButton(name) for name in args]        
# Добавляем каждую кнопку из списка buttons в экземпляр ReplyKeyboardMarkup
        for button in buttons:
            keyboardgostart.add(button)        
# Отправляем сообщение с ответом и созданной клавиатурой
        bot.send_message(message.chat.id, answer, reply_markup=keyboardgostart)


# Создаем функцию для пересылки сообщений
def send_certificate_info(message):
# Получаем информацию от пользователя
    certificate_info = message.text
# Отправляем информацию в отдельный чат
    chat_id = 212049897
    bot.send_message(chat_id, f"Отправитель: {message.from_user.first_name} {message.from_user.last_name}\n\n{certificate_info}")
# Отправляем ответ пользователю
    bot.send_message(message.chat.id, "Спасибо за заказ. С вами свяжутся!")
# Переходим в главное меню
    func_of_buttons(home, message, 'Для покупателей!', 'Для дизайнеров!', 'Для стилистов и фотографов!')


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
def message_handler(message):
    home = 'Вернуться в главное меню!'
    func_of_buttons("Для покупателей!", message, 'Как оплатить заказ?', 'Информация по доставке', 'Подарочный сертификат', home)
    func_of_buttons("Для дизайнеров!", message, 'Хочу сотрудничать с YAUZA STORE!', 'Уже работаю с YAUZA STORE!', home)
    func_of_buttons("Для стилистов и фотографов!", message, 'Хочу взять в аренду вещи, для съемки!', home)
    func_of_buttons(home, message, 'Для покупателей!', 'Для дизайнеров!', 'Для стилистов и фотографов!')
#Задаем функционал кнопкам в подменю "Для покупателей"    
    func_of_buttons("Как оплатить заказ?", message, home, answer='Оплатить заказ можно онлайн переводом по номеру телефона 89670888169 на любой привязанный банк')
    func_of_buttons("Информация по доставке", message, 'Быстрая доставка по Москве, в пределах МКАД', 'Доставка по России и в ближайшее модмосковье', home, answer='Куда нужно доставить?')
    func_of_buttons("Подарочный сертификат", message, 'Заказать подарочный сертификат!', home, answer='Для оформления сертификата нам потребуется следующая информация:\nОт кого\nКому\nИ куда направить готовый электронный сертификат\n\nОплатить заказ можно онлайн переводом по номеру телефона или наличными в магазине YAUZA STORE.')    
#Задаем функционал кнопкам в подменю "Информация по доставке"
    func_of_buttons("Быстрая доставка по Москве, в пределах МКАД", message, home, answer='Мы отправляем заказы по Москве, в пределах МКАД курьерской службой (+300₽)\nПри заказе до 6 часов вечера, доставка возможна в день заказа')
    func_of_buttons("Доставка по России и в ближайшее модмосковье", message, home, answer='В ближайшее Подмосковье и в другие города мы доставляем заказы службой доставки сдэк до пункта выдачи (+300₽)')
#Задаем функционал кнопкам в подменю "Подарочный сертификат"
    if message.text == "Заказать подарочный сертификат!":
        keyboard = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, "Пожалуйста, отправьте сюда следующую информацию:\n\nОт чьего имени будет вручен сертификат\n\nКому предназначается сертификат\n\nКуда направить готовый электронный сертификат (почта, мессенджер и т.д.)", reply_markup=keyboard)
        bot.register_next_step_handler(message, send_certificate_info)
#Задаем функционал кнопкам в подменю "Для дизайнеров!"
    func_of_buttons("Хочу сотрудничать с YAUZA STORE!", message, home, answer='')


bot.polling(none_stop=True, interval=0)
