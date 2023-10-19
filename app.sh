#!/bin/bash

# Прогоняем миграции
alembic upgrade head

# Запускаем приложение
uvicorn main:app --host 0.0.0.0 --port 80