from backend.schemas.user_schemas import AddRole
from backend.crud.users_crud import update_role_email
from fastapi import APIRouter, Security, HTTPException, status
from backend.core.security import access_security
from fastapi_jwt import JwtAuthorizationCredentials
from backend.crud.users_crud import all_users, check_user, get_user_data_by_email, get_user_data_by_id


user_data_router = APIRouter(tags=['user proccesesсч'])

@user_data_router.get('/get_name')
async def get_name(credentials: JwtAuthorizationCredentials = Security(access_security)):
    data = credentials.subject
    user = get_user_data_by_email(data['email'])
    return user


@user_data_router.get('/get_name/{id}')
async def get_name_id(id : int):
    user = get_user_data_by_id(id = id)
    return user


@user_data_router.get('/users')
async def get_all_users(credentials: JwtAuthorizationCredentials = Security(access_security)):
    data = credentials.subject

    if check_user(email=data['email'], password=data['password']):
        return all_users()
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    

@user_data_router.put('/addRole')
async def update_role(role: AddRole, credentials: JwtAuthorizationCredentials = Security(access_security)):
    email = credentials.subject['email']
    update_role_email(role=role.role, email=email)
        

@user_data_router.get('/getUserId')
async def get_user_id(credentials: JwtAuthorizationCredentials = Security(access_security)):
    email = credentials.subject['email']
    id = get_user_data_by_email(email=email)['user_id']
    return {'id':id}