import asyncio
import datetime

async def timer():
    while True:
        current_time = datetime.now().time()
        if current_time.second == 0 or current_time.second == 10 or current_time.second == 20 or current_time.second == 30 or current_time.second == 40 or current_time.second == 50:
            return True
        await asyncio.sleep(1)
