from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Поменять расписание')]
    ],
    resize_keyboard=True
)
