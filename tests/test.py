import pytest

from sqlalchemy import select

from api.utils_func import get_data_from_api
from api.database import Quiz
from .conftest import (client,
                       async_session_maker)


# class TestThirdPartyApi:
#     @pytest.mark.asyncio
#     async def test_response_not_none(self):
#         assert await get_data_from_api(10) != None
#
#     @pytest.mark.asyncio
#     async def test_response_status_ok(self):
#         response = client.get("https://jservice.io/api/random?count=2")
#         assert response.status_code == 200


class TestDataInDb:
    @pytest.mark.asyncio
    async def test_check_elem_in_db(self):
        async with async_session_maker() as session:
            stmt = select(Quiz).where(Quiz)




