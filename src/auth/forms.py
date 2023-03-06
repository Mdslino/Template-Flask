from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = EmailField(
        "Email", validators=[DataRequired(message="Email é obrigatório")]
    )
    password = PasswordField(
        "Senha",
        validators=[
            DataRequired(message="Senha é obrigatória"),
            Length(min=8, message="Senha deve ter no mínimo 8 caracteres"),
        ],
    )
    submit = SubmitField("Entrar")


class ResendActivationForm(FlaskForm):
    username = EmailField(
        "Email", validators=[DataRequired(message="Email é obrigatório")]
    )
    submit = SubmitField("Reenviar email de ativação")


class SignupForm(FlaskForm):
    username = EmailField(
        "Email", validators=[DataRequired(message="Email é obrigatório")]
    )
    password = PasswordField(
        "Senha",
        validators=[
            DataRequired(message="Senha é obrigatória"),
            Length(min=8, message="Senha deve ter no mínimo 8 caracteres"),
        ],
    )
    confirm_password = PasswordField(
        "Confirmar senha",
        validators=[
            DataRequired(message="Senha é obrigatória"),
            Length(min=8, message="Senha deve ter no mínimo 8 caracteres"),
        ],
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
