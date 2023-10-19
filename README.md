<h2>Инструкция по сборке и запуску проекта.</h2>

Далее команды приведены для операционной системы Windows.
1. Клонируем на локальный компьютер себе проект командой git clone https://github.com/ShumilovAlexandr/BeWise
2. в корне проекта создаем виртуальное окружение командой python -m venv venv
3. Запускаем виртуальное окружение командой python . venv/scripts/activate
4. Создайте в корне проекта файл .env, добавьте в него следующие данные:

DB_USER= *укажите ваши данные
DB_PASS=*укажите ваши данные
DB_HOST=db_name
DB_PORT=5432
DB_NAME=*укажите ваши данные

DATABASE_URL=postgresql+asyncpg://*укажите ваши данные:*укажите ваши данные@db_name:5432/be_wise

REDIS_HOST=redis
REDIS_PORT=5370

POSTGRES_DB=*укажите ваши данные
POSTGRES_USER=*укажите ваши данные
POSTGRES_PASSWORD=*укажите ваши данные

5. После установки всех необходимых значений, нужно будет запустить сборку 
   проекта командой docker compose build. Далее, после сборки образа, нужно 
   запустить проект командой docker compose up.
6. Проект будет готов к тесту по адресу: 
   http://localhost:8000/docs#/api/get_and_save_data_in_db_api_get_data_post

Пример запроса:

POST /api/get_data

Content-Type: application/json

{
    "question_id": 2
}

Пример ответа:
