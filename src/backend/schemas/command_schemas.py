from pydantic import BaseModel

class CommandAdd(BaseModel):
    data: list[int]