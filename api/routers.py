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
                            check_element_in_db)
from api.database import Quiz


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
        # Кеширую запрашиваемое количество значений
        await redis.set("count_numb", count.question_count)

        await session.commit()

        # Делаем запрос к базе данных на предмет получения всех записей
        stmt_old = select(Quiz)
        old_data = await session.execute(stmt_old)

        # Если количество записей в базе данных равно текущему количеству
        # возвращенных результатов, то возвращаем пустой результат

        # Получаю закешированное ранее значение
        count_value = await redis.get("count_numb")

        if len(old_data.scalars().all()) == count.question_count:
            return []
        elif len(old_data.scalars().all()) != json.loads(count_value):
            result = await redis.get("data")
            return json.loads(result)

    except IntegrityError:
        await session.rollback()
        raise HTTPException(status_code=500, detail="Ошибка при попытке "
                                                    "загрузки в базу данных")


