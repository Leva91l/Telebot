from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram import Router, F, Bot
import database.requests as rq
import app.keyboards as kb


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id, message.from_user.first_name)

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
async def date_choice(message: Message):
    await message.answer('Выберете дату и время консультации', reply_markup=await kb.all_windows())


@router.callback_query(F.data)
async def monday_callback(callback: CallbackQuery):
    day = callback.data[0:2]
    await rq.make_consult(day)
    await callback.message.answer(
        f'Вы выбрали {day}, 18-00. Напишите свое фио, дата рождения, телефон')  # пользователь пишет всю инфу и бот должен отправить все кате в лс


@router.message(F.text)
async def payment(message: Message, bot: Bot):
    await bot.send_message(chat_id=448356354, text='хэлло муська, как сама')
    await message.answer('Оплатите на карту №777777')