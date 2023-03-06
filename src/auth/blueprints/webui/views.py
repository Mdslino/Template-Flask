from flask import current_app as app
from flask import flash, redirect, render_template, request, url_for
from flask_login import login_user, logout_user

from src.auth.forms import LoginForm, SignupForm
from src.auth.models import User
from src.auth.utils import send_activation_email
from src.ext.database import db


def login():
    """
    Login View
    Login user and redirect to index page
    """
    logger = app.logger

    form = LoginForm(request.form)
    if request.method == "POST":
        logger.info("Login attempt")
        if form.validate_on_submit():
            logger.info("Form validated")
            if user := db.session.execute(
                db.select(User).where(User.username == form.username.data)
            ).scalar_one_or_none():
                logger.info("User found")
                if not user.is_active:
                    logger.warning("User is not active")
                    flash("Usuário não está ativo. Favor sua conta", "danger")
                    return render_template(
                        "auth/login.html", form=form, title="Entrar"
                    )
                if user.authenticate(form.password.data):
                    logger.info("User authenticated")
                    login_user(user)
                    logger.info("User logged in")
                    flash("Login realizado com sucesso.", "success")
                    logger.info("Redirecting to index")
                    return redirect(url_for("webui.index"))
                else:
                    logger.warning(
                        (
                            "User not authenticated, username or password"
                            " invalid, username: %s"
                        ),
                        user.username,
                    )
                    flash("Usuário ou senha inválidos.", "danger")
            else:
                logger.warning(
                    "User not found, username: %s", form.username.data
                )
                flash("Usuário não encontrado.", "danger")
    logger.info("Rendering login page")
    return render_template("auth/login.html", form=form, title="Entrar")


def logout():
    logger = app.logger

    logger.info("Logout attempt")
    logout_user()
    logger.info("User logged out")
    flash("Logout realizado com sucesso.", "success")
    logger.info("Redirecting to index")
    return redirect(url_for("webui.index"))


def signup():
    """
    Signup View
    Create new user and redirect to index page
    """
    logger = app.logger

    form = SignupForm()
    if request.method == "POST":
        logger.info("Signup attempt")
        if form.validate_on_submit():
            logger.info("Form validated")
            if db.session.execute(
                db.select(User).where(User.username == form.username.data)
            ).scalar_one_or_none():
                logger.warning(
                    "User already exists, username: %s", form.username.data
                )
                flash("Usuário já cadastrado.", "warning")
                logger.info("Redirecting to login")
                return redirect(url_for("webui_auth.login"))
            logger.info("Creating new user")
            user = User(username=form.username.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            logger.info(
                "User created and commited to database successfully %s",
                user.username,
            )
            send_activation_email(user)
            flash(
                (
                    "Cadastro realizado com sucesso. Favor ativar sua conta"
                    " através do e-mail recebido"
                ),
                "success",
            )
            logger.info("Redirecting to index")
            return redirect(url_for("webui.index"))
    logger.info("Rendering signup page")
    return render_template("auth/sigup.html", form=form, title="Cadastrar")


def active(user_external_id):
    """
    Active View
    Activate user account and redirect to index page
    """
    logger = app.logger

    logger.info("Active attempt")
    if user := db.session.execute(
        db.select(User).where(User.external_id == user_external_id)
    ).scalar_one_or_none():
        logger.info("User found")
        if user.is_active:
            logger.warning("User is already active")
            flash("Usuário já está ativo.", "warning")
        else:
            logger.info("Activating user")
            user.is_active = True
            db.session.commit()
            logger.info("User activated successfully")
            flash("Usuário ativado com sucesso.", "success")
    else:
        logger.warning("User not found")
        flash("Usuário não encontrado.", "danger")
    logger.info("Redirecting to index")
    return redirect(url_for("webui.index"))
