from aiogram.types import Message, CallbackQuery
from aiogram import Router, F

import administration.adminkeyboard as akb
from app.handlers import router

admin_router = Router()


@admin_router.message(F.text == 'Админ-панель')
async def adminpanel(message: Message):
    await message.answer(
        'Что вы хотите сделать?',
        reply_markup=akb.admin_keyboard
    )


@admin_router.message(F.text == 'Поменять расписание')
async def schedule(message: Message):
    await message.answer(
        'Пожалуйста, выберите день и поменяйте расписание',
        reply_markup = await akb.get_admin_schedule()
    )

@admin_router.callback_query(F.data=='Пн')
async def admin_callback(callback: CallbackQuery):
    await callback.message.answer('abc')
