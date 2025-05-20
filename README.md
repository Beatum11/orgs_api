Проект представляет собой API для справочника организаций, зданий и видов деятельности с помощью FastAPI, SQLAlchemy (async) и PostgreSQL.

## 📑 Основные компоненты

* **FastAPI** — веб-фреймворк
* **SQLAlchemy (async)** — ORM для работы с БД
* **Alembic** — управление миграциями схемы
* **PostgreSQL** — база данных
* **Poetry** — управление зависимостями и виртуальным окружением
* **Docker & Docker Compose** — контейнеризация приложения
* **Pydantic-Settings** — загрузка настроек из `.env`

## ⚙️ Установка и локальный запуск

1. **Клонировать репозиторий**:

   ```bash
   git clone <url>
   cd orgs_api
   ```

2. **Создать `.env`**:

   ```ini
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=postgres
   POSTGRES_DB=mydb

   DATABASE_URL=postgresql+asyncpg://postgres:postgres@db:5432/mydb
   API_KEYS=key1,key2,key3
   ```

3. **Запустить через Docker Compose**:

   ```bash
   docker-compose up --build
   ```

   * Сервис `db` инициализирует БД и выполнит `db/init.sql`.
   * Сервис `api` стартует на `http://localhost:8000`.

4. **Миграции Alembic**:

   * Создать миграцию:

     ```bash
     alembic revision --autogenerate -m "описание"
     ```
   * Применить миграции:

     ```bash
     alembic upgrade head
     ```

## 🚀 Использование API

* **Документация Swagger:** `http://localhost:8000/docs`

### Заголовки

Все защищённые маршруты требуют заголовок:

```
X-API-KEY: <ваш_ключ>
```

### Примеры запросов

* Получить организацию по ID:

  ```http
  GET /organizations/{id}
  ```

* Поиск по имени:

  ```http
  GET /organizations?name=Копыта
  ```

* Список организаций в здании:

  ```http
  GET /organizations/by-building/{building_id}
  ```

* Организации по виду деятельности (ID):

  ```http
  GET /organizations/by-activity/{activity_id}
  ```

* Поиск организаций по названию вида деятельности:

  ```http
  GET /organizations/by-activity/?activity_name=Еда
  ```

## 🔧 Конфигурация

Настройки в `src/config.py`:

* `DATABASE_URL` — строка подключения к БД
* `API_KEYS` — набор валидных API-ключей (через запятую в `.env`)

## ⚙️ Зависимости

Установлены через Poetry:

```toml
[tool.poetry.dependencies]
fastapi = "^0.100.0"
uvicorn = { extras = ["standard"], version = "^0.23.0" }
sqlalchemy = { version = "^2.0", extras = ["asyncio"] }
asyncpg = "^0.27.0"
pydantic-settings = "^2.0"
python-dotenv = "^1.0"
[...]
```

## 📝 Логи и отладка

* Логи пишутся в `logs/` (путь задаётся в `logger.py`).
* SQL-запросы видны, если `echo=True` у `create_async_engine()`.

---
