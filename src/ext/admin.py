from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from src.auth.models import User
from src.config import settings
from src.ext.database import db

admin = Admin(
    name=settings.TITLE, template_mode=settings.FLASK_ADMIN_TEMPLATE_MODE
)

admin.add_view(ModelView(User, db.session))


def init_app(app):
    admin.init_app(app)
