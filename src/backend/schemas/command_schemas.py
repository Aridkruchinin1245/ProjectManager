from pydantic import BaseModel

class CommandAdd(BaseModel):
    user_list: list[int]