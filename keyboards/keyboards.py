from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types

kb_main_menu = [
    [KeyboardButton(text="На главную")]
]

adms = [
        [InlineKeyboardButton(text="Принять", callback_data="yes"),
         InlineKeyboardButton(text="Отклонить", callback_data="no")]
]

adms = types.InlineKeyboardMarkup(inline_keyboard=adms)
kb_main_menu = ReplyKeyboardMarkup(keyboard=kb_main_menu, resize_keyboard=True)
exit_oplatil = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Я оплатил")], [KeyboardButton(text="На главную")]], resize_keyboard=True)
