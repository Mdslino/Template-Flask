from flask import flash, redirect, render_template, request, url_for
from flask_login import login_user, logout_user

from src.auth.forms import LoginForm, SignupForm
from src.auth.models import User
from src.ext.database import db


def login():
    form = LoginForm(request.form)
    if request.method == "POST":
        if form.validate_on_submit():
            if user := db.session.execute(
                db.select(User).where(User.username == form.username.data)
            ).scalar_one_or_none():
                if user.authenticate(form.password.data):
                    login_user(user)
                    flash("Login realizado com sucesso.", "success")
                    return redirect(url_for("webui.index"))
                else:
                    flash("Usuário ou senha inválidos.", "danger")
            else:
                flash("Usuário não encontrado.", "danger")

    return render_template("auth/login.html", form=form, title="Entrar")


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
        "auth/login.html", form=form, title="Cadastrar", flow="Cadastrar"
    )
