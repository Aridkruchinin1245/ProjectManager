from pydantic import BaseModel, Field

class ProjectSchema(BaseModel):
    title: str = Field(max_length=255, min_length=1)
    description: str
    command_id: int
    deadline: str
    