FROM node:alpine AS build

WORKDIR /app

COPY package.* /app

RUN npm install

COPY src/static/js /app/src/static/js

RUN npm run build

FROM python:3.11.3-slim AS run

WORKDIR /app

RUN apt-get update && apt-get install -y curl make && apt clean && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip poetry

COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-cache

COPY . .

COPY --from=build /app/src/static/js/aap.bundle.* /app/src/static/js

EXPOSE 8000