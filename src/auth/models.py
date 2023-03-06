from uuid import uuid4

from sqlalchemy.dialects.postgresql import UUID
from werkzeug.security import check_password_hash, generate_password_hash

from src.auth.exceptions import UserPasswordException
from src.ext.database import TimestampedModel, db


class User(TimestampedModel):
    id = db.Column(db.BigInteger, primary_key=True)
    external_id = db.Column(
        UUID(as_uuid=True),
        unique=True,
        default=uuid4,
        server_default=db.func.uuid_generate_v4(),
    )
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    is_active = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"

    def __str__(self):
        return self.username

    @property
    def is_authenticated(self):
        return True

    def get_id(self):
        return self.external_id

    def check_password(self, password):
        if check_password_hash(self.password, password):
            return True
        raise UserPasswordException("Senha inválida")

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def authenticate(self, password):
        return self.check_password(password) and self.is_active
