# import httpx
# import pytest

# from httpx import AsyncClient
#
# from api.db_config import async_session
# from sqlalchemy.ext.asyncio import AsyncSession
# from ..main import app
#
# client = httpx.Client()
#
#
# @pytest.fixture(scope="session", autouse=True)
# async def db_conn():
#     session = async_session()
#     try:
#         yield session
#     finally:
#         await session.close()
