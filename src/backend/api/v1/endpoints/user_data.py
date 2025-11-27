
from fastapi import APIRouter, Security
from backend.core.security import access_security
from fastapi_jwt import JwtAuthorizationCredentials
from backend.crud.users_crud import get_user_data_by_email


user_data_router = APIRouter()

@user_data_router.get('/get_name')
async def get_name(credentials: JwtAuthorizationCredentials = Security(access_security)):
    data = credentials.subject
    user = get_user_data_by_email(data['email'])
    return user