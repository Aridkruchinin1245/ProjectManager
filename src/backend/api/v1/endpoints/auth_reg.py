from fastapi import APIRouter, HTTPException
from backend.core.security import create_token, hash_password
from backend.schemas.authotisation_schemas import RegistrationHandler, AuthorisationHandler
from backend.crud.users_crud import create_user, check_user


auth_reg_router = APIRouter()

@auth_reg_router.post('/registration')
def create_token_registration(data : RegistrationHandler):
    try:
        data = dict(data)
        data_password = hash_password(data['password'])
        
        create_user(email = data['email'],
                    first_name = data['first_name'],
                    last_name = data['last_name'],
                    password_hash = data_password['hashed'],
                    password_salt = data_password['salt_str'])
        
        token = create_token(data = data)

        return {'access_token' : token}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'ошибка регистрации {e}')


@auth_reg_router.post('/authorisation')
def create_token_authorisation(data : AuthorisationHandler):
    try:
        data = dict(data)

        if check_user(email=data['email'], password=data['password']):
            token = create_token(data = data)
            return {'access_token' : token}
        else:
            raise HTTPException(status_code=404, detail='Нет такого пользователя')
        
    except Exception as e: 
        raise HTTPException(status_code=500, detail=f'ошибка авторизации {e}')

