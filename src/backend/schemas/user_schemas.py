from pydantic import BaseModel, Field, EmailStr, PositiveInt
from typing import Optional
from backend.schemas.role_enum import RoleList

class User(BaseModel):
    id: PositiveInt = Field(..., description='айди юзера')
    email: EmailStr = Field(..., description='емэйл юзера, обязательно правильный формат')
    phone: Optional[str] = Field(min_length=0, max_length=16, description='телефон юзера (1,16)')
    first_name: str = Field(..., min_length=1, max_length=100, description='имя юзера (1,100)')
    last_name: str = Field(..., min_length=1, max_length=100, description='фамилия юзера (1,100)')
    avatar_url: Optional[str] = Field(min_length=1, max_length=500, description='путь до аватарки (1,500)')
    role: Optional[RoleList] = Field(description='роль из списка')

    class Config:
        use_enum_values = True
        from_attributes = True

class AddRole(BaseModel):
    role: RoleList = Field(...)
