from backend.crud.users_crud import get_user_data_by_id
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


def get_projects(): 
    try:
        with SessionLocal() as session:
            data = [project.to_dict() for project in session.query(ProjectBase).all()]
            session.commit()

        for project_id in range(len(data)):
            leader_name = get_user_data_by_id(data[project_id]['lead_id'])['first_name'] + ' ' + get_user_data_by_id(data[project_id]['lead_id'])['last_name']
                              
            creator_name = get_user_data_by_id(data[project_id]['creator_id'])['first_name'] + ' ' + get_user_data_by_id(data[project_id]['creator_id'])['last_name'] 
                              
            data[project_id]['leader_name'] = leader_name
            data[project_id]['creator_name'] = creator_name

        return data
    
    except Exception as e:
        raise 


def delete_projects():
    with SessionLocal() as session:
        session.query(ProjectBase).delete()
        session.commit()
        

