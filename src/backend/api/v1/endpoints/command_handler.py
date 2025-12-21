from fastapi import APIRouter, Security
from fastapi_jwt import JwtAuthorizationCredentials
from backend.core.security import access_security

command_router = APIRouter(tags=['commands'])

@command_router.post('/createCommand')
async def create_command(data : JwtAuthorizationCredentials = Security(access_security)):
    pass