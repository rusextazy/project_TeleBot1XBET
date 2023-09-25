from aiogram import F, Router, types, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile
from aiogram.fsm.state import State, StatesGroup

from keyboards.keyboards_menu import kb_menu
from keyboards.keyboards import exit_oplatil, adms
from lexicon import lexicon_ru

router = Router()


class REPLENISHMENT(StatesGroup):
    SUM = State()
    PROVER = State()
    ID = State()
    SCREEN = State()
    EXAMINATION = State()


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
    await state.set_state(REPLENISHMENT.PROVER)
    await callback.answer()


@router.callback_query(F.data.in_(('yes', 'no')))
async def process_callback(callback: types.CallbackQuery, bot: Bot, state: FSMContext):

    if callback.data == 'yes':
        await bot.send_message(chat_id=id_message, text="✅")
        await bot.send_message(chat_id=id_message, text="Пополнение на счет по введенным вами реквизитам прошел успешно!✅\nСпасибо что используете нашу кассу!🤗")
        await bot.send_message(chat_id='-1001838527137', text=lexicon_ru.odobreno_adm_replenishment.format(id=id_message,
                                                                                                            name=chel_message,
                                                                                                            user=user_message))
    elif callback.data == 'no':
        await bot.send_message(chat_id=id_message, text="❌")
        await bot.send_message(chat_id=id_message, text="Ваш перевод до сих пор не поступил!❌\nПожалуйста проверьте правильно ли вы ввели реквизиты.")
        await bot.send_message(chat_id='-1001838527137', text=lexicon_ru.otkloneno_adm_replenishment.format(id=id_message,
                                                                                                            name=chel_message,
                                                                                                            user=user_message))
    await callback.message.delete_reply_markup()
    await callback.answer()


@router.message(REPLENISHMENT.PROVER)
async def get_prover_replenishment(msg: Message, state: FSMContext):
    await state.update_data(summa=msg.text)
    summa_rab_sum = await state.get_data()
    print(summa_rab_sum['summa'])
    await msg.answer(text="❗️Пожалуйста❗️\nВ качестве проверки напишите пожалуйста текстом\nчерез какой банк Вы "
                          "пополняете✅✅✅\nПример: mbank, MBANK, мбанк, МБАНК")
    await state.set_state(REPLENISHMENT.SUM)


@router.message(REPLENISHMENT.SUM)
async def get_id_replenishment(msg: Message, state: FSMContext):
    await state.update_data(prover=msg.text)
    summa_rab_prov = await state.get_data()
    print(summa_rab_prov['prover'])
    summa_rab_sum = await state.get_data()
    if 0 < int(summa_rab_sum['summa']) <= 100000:
        await state.set_state(REPLENISHMENT.ID)
        photo = FSInputFile("photo/123.jpg")
        await msg.answer_photo(photo, caption="Введите ваш ID(номер счета от 1XBET)")
    else:
        await msg.answer(
            text='Вы ввели некорректное число.\nВводить можно от 1 до 100000 сом.', reply_markup=kb_menu)
        await state.clear()


@router.message(REPLENISHMENT.ID)
async def get_zp_replenishment(msg: Message, state: FSMContext):
    await state.update_data(id=msg.text)
    id_rab_id = await state.update_data()
    print(id_rab_id['id'])
    if int(id_rab_id['id']) > 0:
        await state.set_state(REPLENISHMENT.SCREEN)
        summa_rab_sum = await state.get_data()
        await msg.answer(
            f"Отправьте {summa_rab_sum['summa']} сом по выбранном вами реквизитам:\nПосле перевода нажмите \"Я оплатил\"",
            reply_markup=exit_oplatil)
        await msg.answer(text="+996-997-089-991")
    else:
        await msg.answer(
            text='Вы ввели некорректное число.', reply_markup=kb_menu)
        await state.clear()


@router.message(REPLENISHMENT.SCREEN)
async def get_screen_replenishment(msg: Message, state: FSMContext):
    await state.update_data(skrin=msg.text)
    await state.set_state(REPLENISHMENT.EXAMINATION)
    await msg.answer(text=lexicon_ru.oplatil)


@router.message(REPLENISHMENT.EXAMINATION)
async def get_examination_replenishment(msg: Message, bot: Bot, state: FSMContext):
    await state.update_data(language=msg.text)
    screen_replenishment = msg.photo[-1].file_id
    id_rab_id = await state.update_data()
    summa_rab_sum = await state.get_data()
    summa_rab_prov = await state.get_data()
    await msg.answer(lexicon_ru.oplata.format(id_xbet=id_rab_id['id'], summa=summa_rab_sum['summa'], sposob=summa_rab_prov['prover']))
    await msg.answer(text="❤️", reply_markup=kb_menu)
    await bot.send_message(chat_id='-1001838527137',
                           text=lexicon_ru.proverk_adm_replenishment.format(id=msg.from_user.id, name=msg.from_user.full_name,
                                                              user=msg.from_user.username, id_1xbet=id_rab_id['id'],
                                                              summa=summa_rab_sum['summa'], sposob=summa_rab_prov['prover']), reply_markup=adms)
    await bot.send_photo(chat_id='-1001838527137', photo=screen_replenishment)
    global id_message
    id_message = msg.chat.id
    global chel_message
    chel_message = msg.from_user.full_name
    global user_message
    user_message = msg.from_user.username
    await state.clear()


#ИСПРАВИТЬ ГЛОБАЛЬНЫЕ ПЕРЕМЕННЫЕ