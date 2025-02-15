import asyncio
from datetime import datetime
from app.handlers import on_timer_triggered

async def timer(bot):
    while True:
        current_time = datetime.now().time()
        if current_time.minute in {00, 30} and current_time.second == 10 :
            await on_timer_triggered(bot)
        await asyncio.sleep(1)
