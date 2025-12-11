
from fastapi import APIRouter, Security, HTTPException, status
from backend.core.security import access_security
from fastapi_jwt import JwtAuthorizationCredentials
from backend.crud.users_crud import all_users, check_user, get_user_data_by_email, get_user_data_by_id


user_data_router = APIRouter()

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
        
