from fastapi import HTTPException
from backend.core.security import compare_passwords
from backend.models.models import UserBase
from backend.core.database import SessionLocal


def create_user(email: str, first_name: str, last_name: str, password_hash: str, password_salt: str):
    with SessionLocal() as session:
        check = session.query(UserBase).filter(UserBase.email == email).first()
        if check == None:
            session.add(UserBase(
                email = email,
                first_name=first_name,
                last_name = last_name,
                password_hash = password_hash,
                password_salt = password_salt
            ))
            session.commit()


def check_user(email, password):
    with SessionLocal() as session:
        user = session.query(UserBase).filter(UserBase.email == email).first()
        if user:
            check = compare_passwords(user.password_hash, user.password_salt, password)
            session.commit()
        else:
            return False
        return check
    

def get_user_data_by_email(email : str):
    with SessionLocal() as session:
        try:
            user = session.query(UserBase).filter(UserBase.email == email).first()
            session.commit()
            data = {
                'user_id':user.user_id,
                'first_name':user.first_name,
                'last_name':user.last_name,
                'email':user.email,
                'role':user.role,
                'avatar_url':user.avatar_url,
                'created_at':user.created_at,
                'projects_lead':user.projects_lead,
                'phone':user.phone,
            }
        
            return data
        
        except:
            return HTTPException(status_code=404, detail='Юзер не обнаружен')
        

if __name__=='__main__':
    print(check_user(email='misakrucinin80@gmail.com', password='1'))