from fastapi import APIRouter, HTTPException, Security
from fastapi_jwt import JwtAuthorizationCredentials
from backend.core.security import access_security
from backend.crud.task_crud import create_new_task, get_task_id
from backend.schemas.task_schemas import TaskCreation

task_router = APIRouter(tags=['Tasks'])

@task_router.post('/createTask')
async def create_task(data: TaskCreation, credentials: JwtAuthorizationCredentials = Security(access_security)):
    await create_new_task(description=data.description,
                    email=credentials.subject['email'],
                    project_id = data.project_id)
    

@task_router.get('/allTasks/{id}')
async def get_tasks(id: int, credentials: JwtAuthorizationCredentials = Security(access_security)):
    tasks = await get_task_id(id)
    return tasks
    
