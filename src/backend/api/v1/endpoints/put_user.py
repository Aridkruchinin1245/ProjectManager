from fastapi import APIRouter, Security
from fastapi_jwt import JwtAuthorizationCredentials
from backend.core.security import access_security
from backend.schemas.user_schemas import AddRole
from backend.crud.users_crud import update_role_email

put_router = APIRouter()

@put_router.put('/addRole')
def update_role(role: AddRole, credentials: JwtAuthorizationCredentials = Security(access_security)):
    email = credentials.subject['email']
    update_role_email(role=role.role, email=email)