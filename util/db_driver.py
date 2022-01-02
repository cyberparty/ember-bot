import aiosqlite

class Database():
    def __init__(self):
        self.database = None

    async def __aenter__(self):
        self.database = await self.database_connection()
        self.cursor = await self.database.cursor()

    async def __aexit__(self):
        self.database.close()
        self.cursor.close()

    async def run_sql(self, sql, *args):
        await self.cursor.execute(sql, *args)
        await self.database.commit()
        res = await self.cursor.fetchall()

        if res:
            return res
        return None

    async def database_connection(self):
        return await aiosqlite.connect("database.db")
