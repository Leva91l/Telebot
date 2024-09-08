from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from database.requests import *
from aiogram.utils.keyboard import InlineKeyboardBuilder

t_consult = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Первичная'), KeyboardButton(text='Вторичная')],
        [KeyboardButton(text='Расшифровка анализов')]],
    resize_keyboard=True, input_field_placeholder='↓Выберите пункт из меню ниже↓')

f_consult = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Видео-созвон')], [KeyboardButton(text='Переписка с голосовыми сообщениями')]
    ],
    resize_keyboard=True,
    input_field_placeholder='↓Выберите пункт из меню ниже↓'
)

m_consult = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Telegram')], [KeyboardButton(text='WatsApp')]
    ],
    resize_keyboard=True,
    input_field_placeholder='↓Выберите пункт из меню ниже↓'
)


registration = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Погнали')]
    ],
    resize_keyboard=True,
)


async def all_windows():
    windows = await get_windows()
    keyboard = InlineKeyboardBuilder()
    for window in windows:
            keyboard.add(InlineKeyboardButton(text=f'{window.day}, {window.date}, {window.time}',
                                              callback_data=f'{window.day}{window.date}{window.time}'))
    return keyboard.adjust(2).as_markup()


payment_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Приступить к оплате')]
    ],
    resize_keyboard=True,
    input_field_placeholder='↓Нажмите, чтобы приступить к оплате↓'
)