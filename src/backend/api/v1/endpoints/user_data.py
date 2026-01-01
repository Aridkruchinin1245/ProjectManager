from backend.schemas.user_schemas import AddRole, ChangeNameData
from backend.crud.users_crud import change_user_name, update_role_email
from fastapi import APIRouter, Security, HTTPException, status
from backend.core.security import access_security
from fastapi_jwt import JwtAuthorizationCredentials
from backend.crud.users_crud import all_users, approve_user, get_user_data_by_email, get_user_data_by_id


user_data_router = APIRouter(tags=['user procceses'])

@user_data_router.get('/get_name')
async def get_name(credentials: JwtAuthorizationCredentials = Security(access_security)):
    try:
        data = credentials.subject
        user = await get_user_data_by_email(data['email'])
        return user
    except:
        raise


@user_data_router.get('/get_name/{id}')
async def get_name_id(id : int):
    user = await get_user_data_by_id(id = id)
    return user


@user_data_router.get('/users')
async def get_all_users(credentials: JwtAuthorizationCredentials = Security(access_security)):
    data = credentials.subject

    if await approve_user(email=data['email'], password=data['password']):
        return await all_users()
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    

@user_data_router.put('/addRole')
async def update_role(role: AddRole, credentials: JwtAuthorizationCredentials = Security(access_security)):
    email = credentials.subject['email']
    await update_role_email(role=role, email=email)
        

@user_data_router.get('/getUserId')
async def get_user_id(credentials: JwtAuthorizationCredentials = Security(access_security)):
    email = credentials.subject['email']
    data = await get_user_data_by_email(email=email)
    id = data['id']
    return {'id':id}


@user_data_router.post('/changeName')
async def change_name(data: ChangeNameData,
                       credentials: JwtAuthorizationCredentials = Security(access_security)):
    try:
        await change_user_name(credentials.subject['email'], data.first_name, data.last_name)
    except:
        raise