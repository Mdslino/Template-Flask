# Template Aplicação Flask

O Repositório está disponível como um template para ser usado como base para novos projetos Flask.

## Ambiente

Python 3.11+

## Instalando dependências

```bash
make install
```

## Testando

```bash
make test
```

## Executando

### Em desenvolvimento

```bash
make run-dev
```

### Em produção

```bash
make run
```

Acesse:

- Website: <http://localhost:8000>

- Endpoints:
  - <https://localhost:8000/auth/login>
  - <https://localhost:8000/auth/logout>
  - <https://localhost:8000/auth/signup>

## Funcionalidades

- [x] Autenticação
- [x] Cadastro de usuários
- [x] Migrações
- [x] Testes
- [x] Docker
- [ ] Admin

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
├── poetry.lock
├── pyproject.toml
├── README.md
├── src
│   ├── app.py
│   ├── blueprints
│   │   ├── __init__.py
│   │   └── webui
│   │       ├── __init__.py
│   │       └── views.py
│   ├── config.py
│   ├── ext
│   │   ├── admin.py
│   │   ├── auth.py
│   │   ├── configuration.py
│   │   ├── database.py
│   │   ├── debug.py
│   │   ├── __init__.py
│   │   ├── mail.py
│   │   └── migrations.py
│   ├── __init__.py
│   └── templates
│       ├── base.html
│       ├── includes
│       │   ├── footer.html
│       │   └── navbar.html
│       └── index.html
└── tests
    ├── conftest.py
    ├── __init__.py
    └── test_api.py

9 directories, 32 files
```
