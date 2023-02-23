from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Senha", validators=[DataRequired()])
    submit = SubmitField("Entrar")


class SignupForm(FlaskForm):
    username = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Senha", validators=[DataRequired()])
    confirm_password = PasswordField(
        "Confirmar senha", validators=[DataRequired()]
    )
    submit = SubmitField("Cadastrar")

    def validate(self, extra_validators=None):
        if not super().validate():
            return False

        if self.password.data != self.confirm_password.data:
            error = "Senhas não conferem"
            self.password.errors.append(error)
            self.confirm_password.errors.append(error)
            return False

        return True
