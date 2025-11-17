from pydantic import BaseModel, Field

class RegistrationHandler(BaseModel):
    first_name: str = Field(max_length=50)
    last_name: str = Field(max_length=50)
    email: str = Field(max_length=255)
    password: str = Field(max_length=100)
