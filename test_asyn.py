import asyncio
import asyncpg

async def test():
    try:
        conn = await asyncpg.connect(
            user='postgres',
            password='Bismillah123',
            database='shopping_bot_dev',
            host='localhost'
        )
        print("✅ SUCCESS: Connected via asyncpg")
        await conn.close()
    except Exception as e:
        print("❌ FAILED:", e)

asyncio.run(test())
