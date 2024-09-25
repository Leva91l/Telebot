from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
import administration.adminkeyboard as akb
from config import ADMIN_ID
from database.requests import admin_close_window, admin_open_window, get_admin_schedule, get_info_about_actualuser

admin_router = Router()
@admin_router.message(Command('admin'))
# @admin_router.message(F.text == 'Админ')
async def adminpanel(message: Message):
    if str(message.from_user.id) == ADMIN_ID:
        await message.answer(
            'Что вы хотите сделать?',
            reply_markup=akb.admin_keyboard
        )
    else:
        await message.answer('Вы не администратор!')


@admin_router.callback_query(F.data == 'close')
async def close_window(callback: CallbackQuery):
    await callback.message.edit_text('Выберите день:', reply_markup=await akb.admin_close_day())


@admin_router.callback_query(F.data == 'open')
async def open_window(callback: CallbackQuery):
    await callback.message.edit_text('Выберите день:', reply_markup=await akb.admin_open_day())


@admin_router.callback_query(F.data == 'schedule')
async def admin_schedule(callback: CallbackQuery):
    await callback.message.edit_text('Все записи на неделю:', reply_markup=await akb.admin_schedule())

@admin_router.callback_query(F.data.startswith('c'))
async def close_day_window(callback: CallbackQuery):
    day = callback.data[1:]
    await admin_close_window(day)
    await callback.message.answer(f'Вы успешно закрыли {day}')


@admin_router.callback_query(F.data.startswith('o'))
async def open_day_window(callback: CallbackQuery):
    day = str(callback.data[1:])
    await admin_open_window(day)
    await callback.message.answer(f'Вы успешно открыли {day}')


@admin_router.callback_query(F.data.startswith('info'))
async def admin_detailed_info(callback: CallbackQuery):
    day = str(callback.data[4:])
    user = await get_info_about_actualuser(day)
    await callback.message.answer(f'На {day} записан(а) {user.name}, {user.birthday} г.р. Номер телефона - {user.number} ')