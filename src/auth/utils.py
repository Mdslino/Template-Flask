from flask import current_app as app
from flask import render_template, url_for
from flask_mail import Message

from src.ext.mail import mail


def send_activation_email(user):
    """Send an activation email to the user."""
    user_external_id = user.external_id
    auth_endpoint = url_for(
        "webui_auth.active", user_external_id=user_external_id
    )
    msg = Message(
        "Olá, {}!".format(user.username),
        recipients=[user.username],
        html=render_template(
            "emails/active.html",
            auth_endpoint=auth_endpoint,
        ),
    )

    try:
        mail.send(msg)
    except Exception as e:
        app.logger.exception(e)
        raise e
