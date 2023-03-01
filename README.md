# Arquitetura Definitiva para Projetos Flask

Esse projeto é um fork do projeto do Bruno Rocha, apresentado na Pyjamas Live 2020. [Arquitetura Definitiva para Projetos Flask](https://github.com/codeshow/003-arquitetura-flask)

O Repositório está disponível como um template para ser usado como base para novos projetos Flask.


## Ambiente

Python 3.8+

## Instalando dependências

```bash
make install
```

## Testando

```bash
make test
```

## Executando

```bash
make run
```

Acesse:

- Website: http://localhost:5000

- Endpoints:
  - https://localhost:5000/auth/login
  - https://localhost:5000/auth/logout
  - https://localhost:5000/auth/signup

## Funcionalidades
* [x] Autenticação
* [x] Cadastro de usuários
* [x] Migrações
* [x] Testes
* [x] Docker


## Structure

```bash
.
├── docker-compose.yaml
├── Dockerfile
├── init.sql
├── Makefile
├── migrations
│   ├── alembic.ini
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions
│       └── efd051590cf6_.py
├── poetry.lock
├── pyproject.toml
├── README.md
├── src
│   ├── app.py
│   ├── auth
│   │   ├── blueprints
│   │   │   ├── __init__.py
│   │   │   └── webui
│   │   │       ├── __init__.py
│   │   │       └── views.py
│   │   ├── exceptions.py
│   │   ├── forms.py
│   │   ├── __init__.py
│   │   └── models.py
│   ├── blueprints
│   │   ├── __init__.py
│   │   └── webui
│   │       ├── __init__.py
│   │       └── views.py
│   ├── config.py
│   ├── ext
│   │   ├── auth.py
│   │   ├── configuration.py
│   │   ├── database.py
│   │   ├── __init__.py
│   │   └── migrations.py
│   ├── __init__.py
│   ├── static
│   │   ├── css
│   │   ├── images
│   │   └── js
│   │       └── bulma
│   │           ├── alert.js
│   │           ├── bulma.js
│   │           ├── dropdown.js
│   │           ├── file.js
│   │           ├── message.js
│   │           ├── modal.js
│   │           ├── navbar.js
│   │           ├── notification.js
│   │           ├── panel.js
│   │           ├── panelTabs.js
│   │           └── tabs.js
│   └── templates
│       ├── auth
│       │   ├── login.html
│       │   └── sigup.html
│       ├── base.html
│       ├── includes
│       │   ├── footer.html
│       │   └── navbar.html
│       └── index.html
└── tests
    ├── auth
    │   ├── __init__.py
    │   ├── test_models.py
    │   └── test_views.py
    ├── conftest.py
    ├── factory.py
    ├── __init__.py
    └── test_api.py

19 directories, 54 files
```
