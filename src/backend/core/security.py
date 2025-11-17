from fastapi_jwt import JwtAccessBearer, JwtAuthorizationCredentials
from fastapi import HTTPException, Security
from backend.core.config import settings
import bcrypt

access_security = JwtAccessBearer(secret_key=settings.SECRET_KEY)

def create_token(data:dict):
    try:
        token = access_security.create_access_token(subject=data)
        return token
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'token error {e}')
    

def get_subject(credentials: JwtAuthorizationCredentials = Security(access_security)):
    return credentials.subject


def hash_password(password:str):
    salt = bcrypt.gensalt()
    salt_str = salt.hex()
    hashed = bcrypt.hashpw(password=password.encode("utf-8"), salt=salt).hex()
    return {'salt_str':salt_str, 'hashed':hashed}


def compare_passwords(password_from_db : str, salt : str, password_from_user : str):
    if bytes.fromhex(password_from_db) == bcrypt.hashpw(password = password_from_user.encode("utf-8"), salt=bytes.fromhex(salt)):
        return True
    else:
        return False


if __name__ == "__main__":
    data = hash_password('1234')
    print(compare_passwords(data['hashed'], data['salt_str'], '1234'))