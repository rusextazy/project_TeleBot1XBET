from aiogram import F, Router, types


router = Router()


@router.callback_query(F.data.in_(('mbank_popolnit', 'elkart_popolnit', 'opima_popolnit', 'terminal_popolnit')))
async def process_callback(callback: types.CallbackQuery):
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
    await callback.answer()
