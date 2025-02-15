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
    
    # Запускаем таймер в фоновом режиме
    asyncio.create_task(timer(bot))
    
    # Включаем маршрутизатор
    dp.include_router(router)
    
    try:
        # Запуск опроса бота
        await dp.start_polling(bot)
    except KeyboardInterrupt:
        print("Остановка по запросу пользователя.")
        await close()  # Закрытие соединений и завершение работы

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        asyncio.run(close())
        print('Exit')