from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/Режим_Работы')
b2 = KeyboardButton('/Расположение')
b3 = KeyboardButton('/Меню')
b4 = KeyboardButton('Оставить номер', request_contact=True)
b5 =KeyboardButton('Отправить где я',request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).add(b2).add(b3).row(b4,b5)
