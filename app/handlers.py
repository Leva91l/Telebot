from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import Router, F

import app.keyboards as kb


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
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
