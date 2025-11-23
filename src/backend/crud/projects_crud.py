from backend.models.models import ProjectBase, UserBase
from backend.core.database import SessionLocal
from datetime import datetime 
from typing import Optional

def create_project(email : str, title: str, description: str, deadline: datetime, start_date: Optional[datetime] = None, lead_id: Optional[int] = None):
    with SessionLocal() as session:

        creator_id = session.query(UserBase).filter(UserBase.email == email).first().user_id
        if not lead_id:
            lead_id = creator_id
            
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
