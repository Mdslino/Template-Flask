from flask import g

from src.auth.models import User
from src.ext.database import db


def test_login(client, auth_user):
    response = client.post(
        "/auth/login",
        data={"username": "my_username@domain.com", "password": "my_password"},
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert g._login_user is not None


def test_logout(client):
    response = client.get("/auth/logout", follow_redirects=True)
    assert response.status_code == 200


def test_signup(client):
    username = "my_username@domain.com"
    password = "my_password"
    response = client.post(
        "/auth/signup",
        data={
            "username": username,
            "password": password,
            "confirm_password": password,
        },
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert g._login_user is not None
    user = db.session.execute(
        db.select(User).where(User.username == username)
    ).scalar_one()
    assert user is not None
    assert user.external_id == g._login_user.external_id
