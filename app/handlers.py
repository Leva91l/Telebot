from aiogram import Router, F, Bot
from aiogram.enums import ContentType
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery, LabeledPrice, PreCheckoutQuery

import app.keyboards as kb
from app.keyboards import payment_keyboard
from config import YOOTOKEN
from database.requests import *

router = Router()


class Reg(StatesGroup):
    name = State()
    number = State()
    birthday = State()
    selected_day = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    # await set_user(message.from_user.id)

    await message.answer(
        'Привет пациент Муськи! Гони свои денежки и проваливай!\nПожалуйста, выберите тип консультации!',
        reply_markup=kb.t_consult
    )


@router.message(F.text == 'Первичная')
@router.message(F.text == 'Вторичная')
@router.message(F.text == 'Расшифровка анализов')
async def format_consult(message: Message):
    await message.answer('Выберите формат консультации', reply_markup=kb.f_consult)


@router.message(F.text == 'Видео-созвон')
@router.message(F.text == 'Переписка с голосовыми сообщениями')
async def messanger(message: Message):
    await message.answer('Выберете мессенджер где проводить  консультацию', reply_markup=kb.m_consult)


@router.message(F.text == 'Telegram')
@router.message(F.text == 'WatsApp')
async def date_choice(message: Message, state: FSMContext):
    await message.answer('Выберете дату и время консультации', reply_markup=await kb.all_windows())
    await state.set_state(Reg.selected_day)


@router.callback_query(Reg.selected_day)
async def monday_callback(callback: CallbackQuery, state: FSMContext):
    full_data = callback.data
    await state.update_data(selected_day=full_data)
    await callback.message.answer(
        f'Вы выбрали {full_data}. Теперь запишем Ваши данные. Введите ФИО:')
    await state.set_state(Reg.name)


@router.message(Reg.name)
async def reg_number(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.number)
    await message.answer('Введите номер телефона')


@router.message(Reg.number)
async def reg_birthday(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    await state.set_state(Reg.birthday)
    await message.answer('Введите дату рождения')


@router.message(Reg.birthday)
async def reg_birthday(message: Message, state: FSMContext):
    await state.update_data(birthday=message.text)
    await state.set_state(None)
    data = await state.get_data()
    print(data)
    await new_user(message.from_user.id, name=data['name'], number=data['number'], birthday=data['birthday'])
    # await state.clear()
    await message.answer('Теперь нужно произвести оплату...', reply_markup=payment_keyboard)


@router.message(F.text == 'Приступить к оплате')
async def order(message: Message, bot: Bot):
    await bot.send_invoice(
        chat_id=message.chat.id,
        title='Консультация',
        description='Консультация у Левченко Е.А.',
        payload='Платеж за консульацию',
        provider_token=YOOTOKEN,
        currency='RUB',
        prices=[LabeledPrice(
            label='123',
            amount=10000
        )]
    )


@router.pre_checkout_query()
async def pre_checkout_query(pre_check: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_check.id, ok=True)


@router.message(F.content_type == ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: Message, state: FSMContext):
    data2 = await state.get_data()
    msg = f'Спасибо за оплату!\n{data2['name']}, вы записались на консультацию к Левченко Е.А. на {data2["selected_day"]}'
    await make_consult(data2['selected_day'])
    return await message.answer(msg)
