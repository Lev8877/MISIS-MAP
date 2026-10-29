# Карта МИСиС: бэкенд

API для карты корпусов МИСиС: этажи, помещения, поиск аудитории и кратчайший маршрут от одного кабинета до другого.

Данные хранятся в PostgreSQL. Их загружают из файла data.json скриптом import_data.py.

## Стек

Python 3.13  
FastAPI, Pydantic  
PostgreSQL  
SQLAlchemy, asyncpg  
Alembic  
Pytest, TestClient  
Docker Compose (по желанию, для базы)

## Возможности

Список этажей и данные этажа  
Список помещений, фильтр по этажу  
Карточка помещения с типом, площадью и вместимостью  
Поиск по номеру и названию без учёта регистра  
Кратчайший маршрут между помещениями, в том числе с переходом между этажами (алгоритм Дейкстры)

## Структура базы данных

```text
room_types   Типы помещений: name, category
floors       Этажи: building, number, name, plan_url
rooms        Помещения: number, name, area, capacity, floor_id, room_type_id
graph_nodes  Точки графа: code, floor_id, room_id, x, y, description
graph_edges  Рёбра графа: node_from_id, node_to_id, length_meters, edge_type
```

Точка графа — это дверь помещения, точка коридора или лестница. У двери заполнен room_id, у коридора и лестницы room_id пустой. Координаты x, y задаются в системе координат SVG-плана этажа.

Ребро соединяет две точки, длина указывается в метрах. Лестница — это ребро между точками двух этажей.

## Формат data.json

```text
room_types  name, category
floors      building, number, name, plan_url
rooms       number, name, type, building, floor, area, capacity
nodes       code, building, floor, room, x, y, description
edges       from, to, length, type
```

Помещение ссылается на тип по названию и на этаж по паре building + floor. Точка ссылается на помещение по номеру (room), у коридора и лестницы room = null. Ребро ссылается на точки по их code.

Импорт сначала очищает все таблицы, поэтому его можно запускать повторно после правки data.json.

## Структура проекта

```text
alembic/          Миграции базы данных
models/           Модели SQLAlchemy
routers/          Маршруты API
schemes/          Схемы Pydantic
services/         Бизнес-логика
tests/            Тесты
main.py           Точка входа в приложение
database.py       Базовый класс моделей
dependencies.py   Подключение к базе данных
graph.py          Граф и поиск кратчайшего пути
import_data.py    Загрузка data.json в базу
data.json         Данные корпусов
compose.yaml      PostgreSQL в Docker
requirements.txt  Зависимости Python
```

## Настройка .env

Создайте файл .env в папке backend. За основу можно взять .env.example.

```dotenv
DATABASE_URL=postgresql+asyncpg://postgres:change_me@localhost:5433/misis_map
TEST_DATABASE_URL=postgresql+asyncpg://postgres:change_me@localhost:5433/misis_map_test

POSTGRES_USER=postgres
POSTGRES_PASSWORD=change_me
POSTGRES_DB=misis_map
```

Порт 5433 подходит для базы из Docker Compose. Если PostgreSQL установлен локально, укажите его адрес, обычно порт 5432, и создайте базы misis_map и misis_map_test.

Файл .env не должен попадать в Git.

## База в Docker Compose

```bash
docker compose up -d
docker compose exec postgres createdb -U postgres misis_map_test
```

Вторая команда создаёт базу для тестов, её нужно выполнить один раз.

## Локальный запуск

Все команды выполняются из папки backend.

Создать виртуальное окружение и установить зависимости:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Создать таблицы и загрузить данные:

```powershell
py -m alembic upgrade head
py import_data.py
```

Запустить приложение:

```powershell
uvicorn main:app --reload
```

Swagger: [http://localhost:8000/docs](http://localhost:8000/docs)

## Тесты

```powershell
py -m pytest -v
```

Тесты используют базу из TEST_DATABASE_URL. Перед запуском таблицы в ней пересоздаются и заполняются из data.json.

## Основные маршруты

GET /floors: Список этажей  
GET /floors/{floor_id}: Получение этажа  
GET /rooms: Список помещений, параметр floor_id необязательный  
GET /rooms/{room_id}: Карточка помещения  
GET /search?query=: Поиск помещений  
GET /route?from_room_id=&to_room_id=: Кратчайший маршрут

## Коды ответов

200: успешный запрос  
404: этаж, помещение или маршрут не найдены  
422: некорректные параметры запроса
