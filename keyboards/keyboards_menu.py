from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


kb_menu = [
    [KeyboardButton(text="Пополнить 💳➕"),
     KeyboardButton(text="Вывести 💳➖")],
    [KeyboardButton(text="Поддержка 🤝"),
     KeyboardButton(text="Инструкция 📝")],
    [KeyboardButton(text="Криптообмен 🎯")]
]

kb_menu = ReplyKeyboardMarkup(keyboard=kb_menu, resize_keyboard=True)
