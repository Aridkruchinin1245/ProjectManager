from pydantic import BaseModel, Field, EmailStr

class AuthorisationHandler(BaseModel):
    email: EmailStr = Field(..., min_length=1, max_length=255, description='емэйл юзера, обязательно правильный формат')
    password: str = Field(..., max_length=100, description='пароль (1,100)')

class RegistrationHandler(AuthorisationHandler):
    first_name: str = Field(..., min_length=1, max_length=100, description='имя юзера (1,100)')
    last_name: str = Field(..., min_length=1, max_length=100, description='фамилия юзера (1,100)')
