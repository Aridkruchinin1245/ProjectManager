from backend.models.models import ProjectBase
from backend.core.database import SessionLocal

def create_project(title, lead_id):
    with SessionLocal() as session:
        session.add(ProjectBase(
            title = title,
            lead_id = lead_id
        ))
        session.commit()

if __name__ == "__main__":
    create_project('someproject', 1)
