import httpx
import json

from sqlalchemy import select
from fastapi_cache.decorator import cache


from .database import Quiz
from .db_config import get_session


async def get_data_from_api(value: int) -> json:
    """
    Функция осуществляет запрос к стороннему API сервису и запрашивает
    определенное количество результатов.
    """
    result = httpx.get(f"https://jservice.io/api/random?count={value}")
    res = result.json()
    return res


async def check_element_in_db(unique_id: int) -> bool:
    """Функция проверяет, есть ли элемент в базе данных."""
    stmt = select(Quiz).where(Quiz.question_id == unique_id)
    if stmt is not None:
        return False
    else:
        return True


async def get_last_request() -> dict:
    stmt = select(Quiz).order_by(Quiz.question_id.desc())
    return stmt
