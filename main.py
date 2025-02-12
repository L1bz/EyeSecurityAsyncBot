import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN
from app.handlers import router
from app.handlers import ConnectDB, on_timer_triggered
from app.datetimer import timer

bot = Bot(token=TOKEN)
dp = Dispatcher()


async def close():
    await ConnectDB.close_db()  # Убедитесь, что это асинхронный метод
    print('close database')


async def main():
    await ConnectDB.start_db()
    await asyncio.create_task(on_timer_triggered(bot))
    await timer()
    dp.include_router(router)
    try:
        await dp.start_polling(bot)
    except KeyboardInterrupt:
        await close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        asyncio.run(close())
        print('Exit')