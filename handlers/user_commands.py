import datetime

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from keyboards.keyboards_menu import kb_menu
from lexicon.lexicon_ru import start_text

from keyboards.keyboards_menu import kb_menu


router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(start_text.format(name=msg.from_user.full_name, time=datetime.datetime.today()),
                     reply_markup=kb_menu)


@router.message(Command("menu"))
async def menu_handler(msg: Message):
    await msg.answer(text='Вы попали в главное меню!', reply_markup=kb_menu)
