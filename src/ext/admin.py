from flask import redirect, url_for
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user

from src.config import settings
from src.ext.database import db


class AuthAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('webui_auth.login'))


class AuthModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('webui_auth.login'))


admin = Admin(
    name=settings.TITLE,
    template_mode=settings.FLASK_ADMIN_TEMPLATE_MODE,
    index_view=AuthAdminIndexView(),
)


def init_app(app):
    admin.init_app(app)
