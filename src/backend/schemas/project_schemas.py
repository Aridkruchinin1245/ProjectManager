from pydantic import BaseModel, Field

class ProjectSchema(BaseModel):
    title: str = Field(max_length=255, min_length=1)
    description: str = Field()
    command_id: int = Field(min=1)
    deadline: str = Field()
    