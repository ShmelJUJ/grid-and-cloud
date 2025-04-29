## Описание

Приложение предоставляет два основных эндпоинта:

- `POST /add`: добавляет пару `key` + `value` в базу данных.
- `GET /items`: возвращает все сохранённые пары.

# POST /add

Добавляет запись в базу данных:

{
  "key": "example",
  "value": "some string"
}

# GET /items

Возвращает список всех записей:

[
  {
    "key": "example",
    "value": "some string"
  }
]

# UI

http://localhost:8000/docs — Swagger UI