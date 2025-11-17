
from backend.models.models import UserBase
from backend.core.database import SessionLocal

def create_user(email, first_name, last_name, password_hash, password_salt):
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


if __name__ == "__main__":
    create_user(
        'testemail',
        'first_name',
        'last_name',
        '123456'
    )
