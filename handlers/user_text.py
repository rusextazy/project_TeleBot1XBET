from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.keyboards import kb_main_menu
from keyboards.keyboards_menu import kb_menu

router = Router()


@router.message(F.text == "Пополнить 💳➕")
async def popolnit(msg: Message):
    await msg.answer(text="1")
    await msg.answer(text="1", reply_markup=kb_main_menu)


@router.message(F.text == "Вывести 💳➖")
async def vivod(msg: Message):
    await msg.answer(text="1")
    await msg.answer(text="1")


@router.message(F.text == "Инструкция 📝")
async def instruction(msg: Message):
    await msg.answer(text="1")


@router.message(F.text == "Криптообмен 🎯")
async def kriptoobmen(msg: Message):
    await msg.answer(text="1")


@router.message(F.text == "Поддержка 🤝")
async def podderjka(msg: Message):
    await msg.answer(text="1")


@router.message(F.text == "На главную")
@router.message(F.text == "Отмена")
@router.message(F.text == "Меню")
async def main_menu(msg: Message):
    await msg.reply(text="Вы вернулись на главное меню!", reply_markup=kb_menu)


