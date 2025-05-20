FROM python:3.12-slim

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

COPY src/ ./src/

CMD ["poetry", "run", "uvicorn", "src:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]