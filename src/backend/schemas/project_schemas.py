from pydantic import BaseModel, Field

class ProjectSchema(BaseModel):
    title: str = Field(..., max_length=255, min_length=1, description='название проекта (1,255)')
    description: str = Field(..., min_length=10, max_length=3000, description='описание проекта (10,3000)')
    command_id: int = Field(..., ge=0, description='айди команды')
    deadline: str = Field(..., description='дедлайн проекта')

class ID(BaseModel):
    id: int