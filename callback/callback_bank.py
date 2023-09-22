from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

router = Router()


class MBANK_REFILL(StatesGroup):
    SUM = State()
    ID = State()
    SKRIN = State()
    language = State()


@router.callback_query(F.data.in_(('mbank_popolnit', 'elkart_popolnit', 'opima_popolnit', 'terminal_popolnit')))
async def process_callback(callback: types.CallbackQuery, state: FSMContext):
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
    await state.set_state(MBANK_REFILL.SUM)
    await callback.answer()
