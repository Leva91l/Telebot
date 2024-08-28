from aiogram.types import Message
from aiogram import Router, F

import administration.adminkeyboard as akb

admin_router = Router()

@admin_router.message(F.text=='Админ-панель')
async def adminpanel(message: Message):
    await message.answer(
        'Что вы хотите сделать?',
        reply_markup=akb.admin_keyboard
    )