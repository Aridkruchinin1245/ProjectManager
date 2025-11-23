from fastapi import APIRouter, HTTPException, Security
from fastapi_jwt import JwtAuthorizationCredentials
from backend.core.security import access_security
from backend.crud.users_crud import get_user_data_by_email
from backend.schemas.project_schemas import ProjectSchema
from backend.crud.projects_crud import create_project
from datetime import datetime

project_router = APIRouter()

@project_router.post('/projectsCreating')
def creating_project(user_data: ProjectSchema, credentials: JwtAuthorizationCredentials = Security(access_security)):
    try:
        credentials_data = credentials.subject
        create_project(title=user_data.title,
                       description=user_data.description,
                       deadline=datetime.strptime(user_data.deadline, '%Y-%m-%d').date(),
                       email=credentials_data['email']
                        )
                       
    except Exception as e: 
        raise HTTPException(status_code=500, detail=f"Ошибка создания проекта {e}")