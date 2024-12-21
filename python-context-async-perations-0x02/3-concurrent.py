import aiosqlite
import asyncio
async def async_fetch_users():
    async with aiosqlite.connect('user.db') as db:
        async with db.execute('SELECT * FROM users') as cursor:
            rows = await cursor.fetchall()
            return(rows)

async def async_fetch_older_users():
    async with aiosqlite.connect('user.db') as db:
        async with db.execute('SELECT * FROM users WHERE age > 40') as cursor:
            rows = await cursor.fetchall()
            return(rows)
async def fetch_concurrently():
    await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users(),
    )
asyncio.run(fetch_concurrently())
     
