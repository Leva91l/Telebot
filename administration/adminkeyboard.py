from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from database.requests import *

admin_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Закрыть расписание на определенный день', callback_data='close')],
        [InlineKeyboardButton(text='Открыть расписание на определенный день', callback_data='open')],
        [InlineKeyboardButton(text='Посмотреть расписание на неделю', callback_data='schedule')],
    ]
)


async def admin_schedule():
    schedule = await get_admin_schedule()
    keyboard = InlineKeyboardBuilder()
    for days in schedule:
        keyboard.add(InlineKeyboardButton(text=f'{days.day}, {days.date}', callback_data=f'info{days.day}'))
    return keyboard.adjust(2).as_markup()


async def admin_close_day():
    windows = await get_all_windows()
    keyboard = InlineKeyboardBuilder()
    for window in windows:
        keyboard.add(InlineKeyboardButton(text=f'{window.day}, {window.date}',
                                          callback_data=f'c{window.day}'))
    return keyboard.adjust(2).as_markup()


async def admin_open_day():
    windows = await get_all_windows()
    keyboard = InlineKeyboardBuilder()
    for window in windows:
        keyboard.add(InlineKeyboardButton(text=f'{window.day}, {window.date}',
                                          callback_data=f'o{window.day}'))
    return keyboard.adjust(2).as_markup()


