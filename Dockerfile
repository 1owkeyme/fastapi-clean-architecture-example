FROM python:3.11-alpine as backend-base

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

FROM backend-base

ENV POETRY_VERSION=1.7.1

WORKDIR /app

RUN pip install --no-cache-dir poetry==${POETRY_VERSION} && \
    poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./

RUN poetry install --only=main --no-root --no-interaction --no-cache

COPY src ./src

COPY alembic.ini ./alembic.ini

COPY start.sh ./start.sh

RUN chmod 755 /app/start.sh

CMD ["/app/start.sh"]


