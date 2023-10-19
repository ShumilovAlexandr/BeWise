import uvicorn

from fastapi import FastAPI

from api.routers import router


app = FastAPI(
    title="BeWise Test",
    description="Тестовое задание")


app.include_router(router)

