FROM node:slim AS stage-build

WORKDIR /node_build

COPY package* /node_build/

RUN npm install

COPY . .

RUN npm run build

FROM python:3.11.3-slim AS stage-run

WORKDIR /app

RUN apt-get update && apt-get install -y curl make && apt clean && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip poetry

COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-cache

COPY . .

COPY --from=stage-build /node_build/src/static/js/app.bundle.* /app/src/static/js/

EXPOSE 8000