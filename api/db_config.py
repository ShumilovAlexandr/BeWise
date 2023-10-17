import os

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import (AsyncSession,
                                    create_async_engine)
from sqlalchemy.orm import sessionmaker

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DATABASE = os.getenv('DATABASE_URL')


engine = create_async_engine(
    DATABASE
)

async_session = sessionmaker(engine,
                             class_=AsyncSession,
                             expire_on_commit=False
                             )


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
