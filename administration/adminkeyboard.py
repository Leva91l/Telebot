from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from database.requests import *

admin_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Поменять расписание')]
    ],
    resize_keyboard=True
)


async def get_admin_schedule():
    windows = await get_windows()
    keyboard = InlineKeyboardBuilder()
    for window in windows:
        keyboard.add(InlineKeyboardButton(text=f'{window.day}',
                                          callback_data=f'{window.day}'))
    return keyboard.adjust(2).as_markup()