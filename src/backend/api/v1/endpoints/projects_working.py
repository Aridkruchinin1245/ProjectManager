from fastapi import APIRouter, HTTPException, Security
from fastapi_jwt import JwtAuthorizationCredentials
from backend.core.security import access_security
from backend.schemas.project_schemas import ProjectSchema
from backend.crud.projects_crud import create_project

project_router = APIRouter()

@project_router.post('/projectsCreating')
def creating_project(user_data: ProjectSchema, credentials: JwtAuthorizationCredentials = Security(access_security)):
    try:
        credentials_data = credentials.subject
        
    except Exception as e: 
        raise HTTPException(status_code=500, detail=f"Ошибка создания проекта {e}")