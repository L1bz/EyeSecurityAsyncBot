from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

startkey = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Поставить напоминание"),KeyboardButton(text="Набор тренировок для глаз")]
], resize_keyboard=True)