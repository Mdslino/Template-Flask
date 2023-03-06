from flask import Blueprint

from src.auth.blueprints.webui.views import active, login, logout, signup

bp = Blueprint(
    "webui_auth", __name__, template_folder="templates", url_prefix="/auth"
)

bp.add_url_rule("/login", view_func=login, methods=("GET", "POST"))
bp.add_url_rule("/logout", view_func=logout, methods=("GET",))
bp.add_url_rule("/signup", view_func=signup, methods=("GET", "POST"))
bp.add_url_rule(
    "/active/<uuid:user_external_id>", view_func=active, methods=("GET",)
)


def init_app(app):
    app.register_blueprint(bp)
