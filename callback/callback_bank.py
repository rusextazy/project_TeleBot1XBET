from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile
from aiogram.fsm.state import State, StatesGroup

from keyboards.keyboards_menu import kb_menu


router = Router()


class REPLENISHMENT(StatesGroup):
    SUM = State()
    ID = State()
    SKRIN = State()
    language = State()


@router.callback_query(F.data.in_(('mbank_popolnit', 'elkart_popolnit', 'opima_popolnit', 'terminal_popolnit')))
async def process_callback(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data()
    if callback.data == 'mbank_popolnit':
        await callback.message.answer(text='Вы выбрали MBANK')
        await callback.message.answer(text='Укажите сумму пополнения COM🇰🇬')
    elif callback.data == 'elkart_popolnit':
        await callback.message.answer(text='Вы выбрали Элкарт')
        await callback.message.answer(text='Укажите сумму пополнения COM🇰🇬')
    elif callback.data == 'opima_popolnit':
        await callback.message.answer(text='Вы выбрали Оптима Банк')
        await callback.message.answer(text='Укажите сумму пополнения COM🇰🇬')
    elif callback.data == 'terminal_popolnit':
        await callback.message.answer(text='Вы выбрали Терминал')
        await callback.message.answer(text='Укажите сумму пополнения COM🇰🇬')
    await state.set_state(REPLENISHMENT.SUM)
    await callback.answer()


@router.message(REPLENISHMENT.SUM)
async def get_id_mbank(msg: Message, state: FSMContext):
    await state.update_data(summa=msg.text)
    summa_mbank_rab = await state.get_data()
    print(summa_mbank_rab['summa'])
    if int(summa_mbank_rab['summa']) > 0:
        await state.set_state(REPLENISHMENT.ID)
        photo = FSInputFile("photo/123.jpg")
        await msg.answer_photo(photo, caption="Введите ваш ID(номер счета от 1XBET)")
    else:
        await msg.answer(
            text='Вы ввели некорректное число.\nВводить можно от 1 до 100000 сом.', reply_markup=kb_menu)
        await state.clear()
