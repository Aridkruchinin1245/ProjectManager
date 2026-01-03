from pydantic import BaseModel, Field

class TaskCreation(BaseModel):
    description: str
    project_id: int