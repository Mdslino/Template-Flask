import pytest

from src.app import create_app, minimal_app
from src.ext.database import db
from tests.factory import UserFactory


@pytest.fixture(scope="session")
def min_app():
    app = minimal_app()
    return app


@pytest.fixture(scope="session", autouse=True)
def app():
    app = create_app()
    with app.app_context():
        db.create_all(app=app)
        yield app
        db.drop_all(app=app)


@pytest.fixture
def auth_user():
    return UserFactory()
