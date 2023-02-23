from flask_login import LoginManager

from src.auth.models import User
from src.ext.database import db

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return db.session.execute(
        db.select(User).where(User.external_id == user_id)
    ).scalar_one()


def init_app(app):
    login_manager.init_app(app)
