from typing import List

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Application Configuration
    DEBUG: bool = False
    TITLE: str = 'Template'
    SERVER_NAME: str = '0.0.0.0:8000'
    PREFERRED_URL_SCHEME: str = 'http'
    SECRET_KEY: str = 'jadkfbsdkjbfbh'
    PASSWORD_SCHEMES: List[str] = ['pbkdf2_sha512', 'md5_crypt']
    EXTENSIONS: List[str] = [
        'src.ext.database:init_app',
        'src.ext.migrations:init_app',
        'src.ext.admin:init_app',
        'src.ext.mail:init_app',
        'src.ext.debug:init_app',
        'src.blueprints.webui:init_app',
    ]

    # Flask-Admin Configuration
    FLASK_ADMIN_NAME: str = 'Admin'
    FLASK_ADMIN_TEMPLATE_MODE: str = 'bootstrap4'
    FLASK_ADMIN_SWATCH: str = 'cerulean'

    # SQLAlchemy Configuration
    SQLALCHEMY_DATABASE_URI: str = (
        'postgresql://postgres:postgres@localhost:5432/postgres'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False

    # Flask-Mail Configuration
    MAIL_SERVER: str = 'smtp.gmail.com'
    MAIL_PORT: int = 465
    MAIL_USE_SSL: bool = True
    MAIL_USERNAME: str = ''
    MAIL_PASSWORD: str = ''
    MAIL_DEFAULT_SENDER: str = ''

    TEMPLATES_AUTO_RELOAD: bool = True
    DEBUG_TOOLBAR_ENABLED: bool = True
    DEBUG_TB_INTERCEPT_REDIRECTS: bool = False
    DEBUG_TB_PROFILER_ENABLED: bool = True
    DEBUG_TB_TEMPLATE_EDITOR_ENABLED: bool = True
    DEBUG_TB_PANELS: List[str] = [
        'flask_debugtoolbar.panels.versions.VersionDebugPanel',
        'flask_debugtoolbar.panels.sqlalchemy.SQLAlchemyDebugPanel',
        'flask_debugtoolbar.panels.timer.TimerDebugPanel',
        'flask_debugtoolbar.panels.headers.HeaderDebugPanel',
        'flask_debugtoolbar.panels.request_vars.RequestVarsDebugPanel',
        'flask_debugtoolbar.panels.template.TemplateDebugPanel',
        'flask_debugtoolbar.panels.route_list.RouteListDebugPanel',
        'flask_debugtoolbar.panels.logger.LoggingPanel',
        'flask_debugtoolbar.panels.profiler.ProfilerDebugPanel',
        'flask_debugtoolbar.panels.config_vars.ConfigVarsDebugPanel',
    ]

    WTF_CSRF_ENABLED: bool = True


settings = Settings()
