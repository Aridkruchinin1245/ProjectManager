from fastapi import APIRouter, HTTPException, Security, status
from fastapi_jwt import JwtAuthorizationCredentials
from backend.core.security import access_security
from backend.schemas.project_schemas import ProjectSchema
from backend.crud.projects_crud import create_project, get_projects
from datetime import datetime
from backend.crud.users_crud import approve_user

project_router = APIRouter(tags=['project processes'])

@project_router.post('/projectsCreating')
async def creating_project(user_data: ProjectSchema, credentials: JwtAuthorizationCredentials = Security(access_security)):
    try:
        credentials_data = credentials.subject

        await create_project(title=user_data.title,
                       description=user_data.description,
                       deadline=datetime.strptime(user_data.deadline, '%Y-%m-%d').date(),
                       email=credentials_data['email'],
                       command_id=user_data.command_id
                        )
                       
    except Exception as e: 
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f'Ошибка создания проекта {e}')
    
@project_router.get('/getProjects')
async def send_projects(credentials: JwtAuthorizationCredentials = Security(access_security)):
    try:
        data = credentials.subject

        if await approve_user(email=data['email'], password=data['password']):
            return await get_projects()
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Такого пользователя не существует')
        
    except HTTPException:
        raise