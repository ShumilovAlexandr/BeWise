import datetime
import aioredis
import json

from fastapi import (APIRouter,
                     Depends,
                     HTTPException)
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import (insert,
                        select)
from sqlalchemy.exc import IntegrityError

from api.db_config import get_session
from api.models import QuizModel
from api.utils_func import (get_data_from_api,
                            check_element_in_db,
                            get_last_request)
from api.database import Quiz
from api.db_config import engine

router = APIRouter(
    prefix="/api",
    tags=["api"]
)


@router.post("/get_data")
async def get_and_save_data_in_db(count: QuizModel,
                                  session: AsyncSession =
                                  Depends(get_session)):
    """
    Функция получает и сохраняет данные в БД.

    С помощью дополнительной функции, отправляется запрос к стороннему API.
    Дальше происходит разбор полученных данных и сохранение их в базу данных
    Postgres.
    :param count: количество запрашиваемых вопросов;
    :param session: объект сессии
    """
    data_api = await get_data_from_api(count.question_count)
    redis = aioredis.from_url("redis://localhost")

    try:
        for value in data_api:
            date_time = (value["created_at"][0:10] + " " + value[
                "created_at"][11:19])
            date_and_time = datetime.datetime.strptime(date_time, "%Y-%m-%d "
                                                                  "%H:%M:%S")
            # Пока полученные данные уже имеются в базе данных,
            # будет выполняться дополнительный запрос
            while await check_element_in_db(value["id"]):
                data_api = await get_data_from_api(count.question_count)

            # Пробрасываем данные в базу
            stmt = insert(Quiz).values(
                (value["id"],
                 value["question"],
                 value["answer"],
                 date_and_time))
            await session.execute(stmt)
            # Кеширую полученный результат
            await redis.set("data", json.dumps(data_api))

        await session.commit()

        stmt_old = select(Quiz)
        old_data = await session.execute(stmt_old)

        # Если количество записей в базе данных равно текущему количеству
        # возвращенных результатов, то возвращаем пустой результат
        if len(old_data.scalars().all()) == count.question_count:
            return []
        else:
            # Возвращаю закешированный ранее результат
            value = await redis.get("data")
            return json.loads(value)

    except IntegrityError:
        await session.rollback()
        raise HTTPException(status_code=500, detail="Ошибка при попытке "
                                                    "загрузки в базу данных")


