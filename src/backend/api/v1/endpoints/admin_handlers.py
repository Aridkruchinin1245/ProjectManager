from fastapi import APIRouter, HTTPException, status, Security
from backend.core.security import access_security
from fastapi_jwt import JwtAuthorizationCredentials
from backend.core.security import check_admin
from backend.crud.projects_crud import delete_projects
from backend.crud.users_crud import delete_users

admin_router = APIRouter()

@admin_router.delete('/deleteProjects')
def delete_project_handler(credentials: JwtAuthorizationCredentials = Security(access_security)):
    try:
        data = credentials.subject
        if check_admin(email=data['email'], password=data['password']):
            delete_projects()
        else:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Пользователь не является админом')
    except HTTPException:
        raise


@admin_router.delete('/deleteUsers')
def delete_project_handler(credentials: JwtAuthorizationCredentials = Security(access_security)):
    try:
        data = credentials.subject
        if check_admin(email=data['email'], password=data['password']):
            delete_users()
        else:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Пользователь не является админом')
    except HTTPException:
        raise

