import pytest
from sqlalchemy import text
from sqlalchemy.orm.session import close_all_sessions
from sqlalchemy_utils import create_database, database_exists, drop_database

from src.app import create_app
from src.ext.database import db
from tests.factory import UserFactory


@pytest.fixture(scope="session")
def app():
    app = create_app()
    return app


@pytest.fixture(scope="session", autouse=True)
def setup_db(app):
    with app.app_context():
        sqlalchemy_database_uri = app.config["SQLALCHEMY_DATABASE_URI"]
        if not database_exists(sqlalchemy_database_uri):
            create_database(sqlalchemy_database_uri)
        db.session.execute(text('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";'))
        db.session.commit()
        yield
        close_all_sessions()


@pytest.fixture(autouse=True)
def setup_tables(app):
    with app.app_context():
        db.create_all()
        yield
        close_all_sessions()
        db.drop_all()


@pytest.fixture
def auth_user():
    return UserFactory()
