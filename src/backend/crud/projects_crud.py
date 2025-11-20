from backend.models.models import ProjectBase
from backend.core.database import SessionLocal
from datetime import datetime 

def create_project(title: str, lead_id: int, description: str, deadline: datetime, start_date: datetime, creator_id: str):
    with SessionLocal() as session:
        session.add(ProjectBase(
            title = title,
            lead_id = lead_id,
            description = description,
            deadline = deadline,
            start_date = start_date,
            creator_id = creator_id
        ))
        session.commit()

if __name__ == "__main__":
    create_project('someproject', 1)
