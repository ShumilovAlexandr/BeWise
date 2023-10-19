<h2>Инструкция по сборке и запуску проекта.</h2>

Далее команды приведены для операционной системы Windows.
1. Клонируем на локальный компьютер себе проект командой git clone https://github.com/ShumilovAlexandr/BeWise
2. в корне проекта создаем виртуальное окружение командой python -m venv venv
3. Запускаем виртуальное окружение командой python . venv/scripts/activate
4. Создайте в корне проекта файл .env, добавьте в него следующие данные:

+ DB_USER= *укажите ваши данные
+ DB_PASS=*укажите ваши данные
+ DB_HOST=db_name
+ DB_PORT=5432
+ DB_NAME=be_wise

+ DATABASE_URL=postgresql+asyncpg://*укажите ваши данные:*укажите ваши данные@db_name:5432/be_wise

+ REDIS_HOST=redis
+ REDIS_PORT=5370

+ POSTGRES_DB=*укажите ваши данные
+ POSTGRES_USER=*укажите ваши данные
+ POSTGRES_PASSWORD=*укажите ваши данные

5. После установки всех необходимых значений, нужно будет запустить сборку 
   проекта командой docker compose build. Далее, после сборки образа, нужно 
   запустить проект командой docker compose up.
6. Проект будет готов к тесту по адресу:[BeWise](http://localhost:8000/docs)

Пример запроса:
```
{
    "question_id": 2
}
```
Пример возвращаемого ответа:
```
[
  {
    "id": 137386,
    "answer": "sesame seed",
    "question": "According to a McDonald's jingle, the Big Mac gets this type of bun",
    "value": 200,
    "airdate": "2009-12-14T20:00:00.000Z",
    "created_at": "2022-12-30T20:18:05.114Z",
    "updated_at": "2022-12-30T20:18:05.114Z",
    "category_id": 15810,
    "game_id": 3253,
    "invalid_count": null,
    "category": {
      "id": 15810,
      "title": "alliterative food & drink",
      "created_at": "2022-12-30T20:18:05.009Z",
      "updated_at": "2022-12-30T20:18:05.009Z",
      "clues_count": 5
    }
  },
{
    "id": 15292,
    "answer": "the Statue of Liberty",
    "question": "France's replica of this statue stands on an island in the Seine & faces west",
    "value": 100,
    "airdate": "1989-02-08T20:00:00.000Z",
    "created_at": "2022-12-30T18:43:52.421Z",
    "updated_at": "2022-12-30T18:43:52.421Z",
    "category_id": 92,
    "game_id": 7593,
    "invalid_count": null,
    "category": {
      "id": 92,
      "title": "travel & tourism",
      "created_at": "2022-12-30T18:37:46.809Z",
      "updated_at": "2022-12-30T18:37:46.809Z",
      "clues_count": 246
    }
  }
]
```
