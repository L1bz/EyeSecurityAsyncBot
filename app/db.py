import aiosqlite
import asyncio

class ConnectDB:


    def __init__(self):

        self.db_path = 'app/user.db' 
        self.db = None


    async def start_db(self):

        self.db = await aiosqlite.connect(self.db_path)

        await self.db.execute("""CREATE TABLE IF NOT EXISTS user(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            status BOOL,
            user_time INTEGER
        )""")

        await self.db.commit()


    async def connect_user(self, message):

        user_i = message.chat.id

        async with self.db.execute("""SELECT status FROM user WHERE user_id = ?""", [user_i]) as cursor:

            row = await cursor.fetchone()

            if row is None:

                await self.db.execute("""INSERT INTO user(user_id, status) VALUES(?, ?);""", (user_i, False))
                await self.db.commit()


    async def change_mode_stauts(self, message):

        user_i=message.chat.id
        
        await self.db.execute(f"UPDATE user SET status = true WHERE user_id={user_i}")
        await self.db.commit()


    async def close_db(self):
        await self.db.close()
    

    async def get_users(self):
        async with self.db.execute("""SELECT user_id FROM user WHERE status= true""") as cursor:
            users = await cursor.fetchall()
            return list(users)
