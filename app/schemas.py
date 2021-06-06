from re import compile as re_compile

from pydantic import BaseModel, EmailStr, Field as field, validator
from werkzeug.security import generate_password_hash

from app.exceptions import InvalidEmailError, ShortPasswordError


class SchemaUser(BaseModel):
    email: EmailStr
    password: str = field(..., min_length=8)
    username: str

    @validator('password', pre=True)
    def password_hash(cls, v):
        if len(v) < 6:
            raise ShortPasswordError()
        return generate_password_hash(v)

    @validator('email', pre=True)
    def email_invalid_format(cls, v):
        regex = re_compile(r"^[a-z0-9._%+-]+@[a-zA0-9.-]+\.[a-z]{2,}$")

        if not regex.match(v):
            raise InvalidEmailError()

        return v
