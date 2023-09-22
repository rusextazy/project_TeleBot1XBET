from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.keyboards import kb_main_menu
from keyboards.keyboards_menu import kb_menu
from keyboards.keyboards_bank import replenish_bank

router = Router()


@router.message(F.text == "Пополнить 💳➕")
async def replenish(msg: Message):
    await msg.answer(text="Укажите удобный вам способ пополнения счета", reply_markup=kb_main_menu)
    await msg.answer(text="Выберите банк:", reply_markup=replenish_bank)


@router.message(F.text == "Вывести 💳➖")
async def withdraw(msg: Message):
    await msg.answer(text="1")
    await msg.answer(text="1")


@router.message(F.text == "Инструкция 📝")
async def instructions(msg: Message):
    await msg.answer(text="1")


@router.message(F.text == "Криптообмен 🎯")
async def crypto_exchange(msg: Message):
    await msg.answer(text="1")


@router.message(F.text == "Поддержка 🤝")
async def support_text(msg: Message):
    await msg.answer(text="1")


@router.message(F.text == "На главную")
@router.message(F.text == "Отмена")
@router.message(F.text == "Меню")
async def main_menu(msg: Message):
    await msg.reply(text="Вы вернулись на главное меню!", reply_markup=kb_menu)
