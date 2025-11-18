
from fastapi import APIRouter, Security
from backend.core.security import access_security
from fastapi_jwt import JwtAuthorizationCredentials
from backend.crud.users_crud import get_user_data_by_email


utils_router = APIRouter()
# {'email': 'misakrucinin80@gmail.com', 'password': '1'}
@utils_router.get('/get_name')
def get_name(credentials: JwtAuthorizationCredentials = Security(access_security)):
    data = credentials.subject
    user = get_user_data_by_email(data['email'])
    return user['first_name'] + ' ' + user['last_name']