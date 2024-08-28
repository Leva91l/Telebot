from aiogram.types import ReplyKeyboardMarkup, KeyboardButton




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
