from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message


router = Router()


@router.message(F.text == "Пополнить 💳➕")
async def popolnit(msg: Message):
    await msg.answer(text="1")
    await msg.answer(text="1")


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