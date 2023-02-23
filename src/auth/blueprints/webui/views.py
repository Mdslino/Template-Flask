from flask import flash, redirect, render_template, request, url_for
from flask_login import login_user, logout_user, user_logged_in

from src.auth.forms import LoginForm, SignupForm
from src.auth.models import User
from src.ext.database import db


def login():
    form = LoginForm()
    if request.method == "POST":
        if form.validate_on_submit() and (
            user := db.one_or_404(
                db.select(User).where(User.username == form.username.data)
            )
        ):
            if user.authenticate(form.password.data):
                login_user(user)
                flash("Login realizado com sucesso.", "success")
                return redirect(url_for("webui.index"))
            flash("Usuário ou senha inválidos.", "danger")

    return render_template(
        "auth/auth.html", form=form, title="Entrar", flow="Cadastrar"
    )


def logout():
    logout_user()
    return redirect(url_for("webui.index"))


def signup():
    form = SignupForm()
    if request.method == "POST":
        if form.validate_on_submit():
            user = User(username=form.username.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash("Cadastro realizado com sucesso.", "success")
            login_user(user)
            return redirect(url_for("webui.index"))

    return render_template(
        "auth/auth.html", form=form, title="Cadastrar", flow="Cadastrar"
    )
