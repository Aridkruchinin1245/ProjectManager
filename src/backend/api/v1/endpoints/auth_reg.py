from fastapi import APIRouter, HTTPException, status
from backend.core.security import create_token, hash_password
from backend.schemas.authotisation_schemas import RegistrationHandler, AuthorisationHandler
from backend.crud.users_crud import create_user, approve_user


auth_reg_router = APIRouter(tags=['registration, authorisation'])

@auth_reg_router.post('/registration')
async def create_token_registration(data : RegistrationHandler):
    try:
        data = dict(data)
        data_password = hash_password(data['password'])

        if not (await approve_user(email=data['email'], password=data['password'])):

            await create_user(email = data['email'],
                        first_name = data['first_name'],
                        last_name = data['last_name'],
                        password_hash = data_password['hashed'],
                        password_salt = data_password['salt_str'])
            
            token = create_token(data = data)
            return {'access_token' : token}
        
        else:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Аккаунт уже существует')

    except HTTPException:
        raise

@auth_reg_router.post('/authorisation')
async def create_token_authorisation(data : AuthorisationHandler):
    try:
        data = dict(data)

        if await approve_user(email=data['email'], password=data['password']):
            token = create_token(data = data)
            return {'access_token' : token}
        
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Нет такого пользователя')
        
    except HTTPException: 
        raise

