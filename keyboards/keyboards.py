from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb_main_menu = [
    [KeyboardButton(text="На главную")]
]

kb_main_menu = ReplyKeyboardMarkup(keyboard=kb_main_menu, resize_keyboard=True)
exit_oplatil = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Я оплатил")], [KeyboardButton(text="На главную")]], resize_keyboard=True)
