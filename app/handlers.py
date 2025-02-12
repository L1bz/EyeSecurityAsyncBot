from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
import asyncio

import app.keyborad as kb
from app.db import ConnectDB as user_db

ConnectDB = user_db()
router = Router()

async def on_timer_triggered(bot):
    user_ids = await ConnectDB.get_users()
    for user_id in user_ids:
        if isinstance(user_id, tuple):
               user_id = user_id[0]
        await bot.send_message(chat_id=user_ids, text="Пора сделать упражнение для глаз")


@router.message(CommandStart())
async def cmd_start(message:Message):
    await ConnectDB.connect_user(message)
    
    await message.reply('asdf!', reply_markup  = kb.startkey)


@router.message(F.text=="Поставить напоминание")
async def reminding(message:Message):
    await ConnectDB.change_mode_stauts(message)
    await message.reply('\n Поставлено напоминание на каждый час')

@router.message(F.text=="Набор тренировок для глаз")
async def show_info(message:Message):
    await message.reply('\n Набор тренировок для глаз можно найти тут: https://t.me/EyesSecurity')
