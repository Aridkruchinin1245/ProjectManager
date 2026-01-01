from fastapi import APIRouter, Security
from fastapi_jwt import JwtAuthorizationCredentials
from backend.core.security import access_security
from backend.crud.commands_crud import create_command, select_all_commands
from backend.schemas.command_schemas import CommandAdd

command_router = APIRouter(tags=['commands'])

@command_router.get('/getCommands')
async def get_command(credentials: JwtAuthorizationCredentials = Security(access_security)):
    data = await select_all_commands()
    return data

@command_router.post('/commandId')
async def post_id(data: CommandAdd, credentials: JwtAuthorizationCredentials = Security(access_security)):
    await create_command(data.data, credentials.subject['email'])
