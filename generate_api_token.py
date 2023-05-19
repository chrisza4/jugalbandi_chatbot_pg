# Python script to generate Jugalbandi API Token

import asyncio
from database import create_engine, PostgresDatabase
import sys
from dotenv import load_dotenv

load_dotenv()

token = sys.argv[1]
quota = sys.argv[2]


async def main():
    db_engine = await create_engine()
    async with db_engine.acquire() as connection:
        await connection.execute(
            """
                    INSERT INTO public.jugalbandi_tokens(
	                  api_key, available_quota, used_quota)
	                  VALUES ($1, $2, $3);
                    """,
            token,
            int(quota),
            0,
        )
        print("Token created successfully")


asyncio.run(main())
