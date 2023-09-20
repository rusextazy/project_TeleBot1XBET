from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from aiogram import types

replenish_bank = [
    [InlineKeyboardButton(text="MBANK", callback_data="mbank_popolnit"),
     InlineKeyboardButton(text="Элкарт", callback_data="elkart_popolnit")],
    [InlineKeyboardButton(text="Optima Bank", callback_data="opima_popolnit"),
     InlineKeyboardButton(text="Терминал", callback_data="terminal_popolnit")]
]

replenish_bank = InlineKeyboardMarkup(inline_keyboard=replenish_bank)
