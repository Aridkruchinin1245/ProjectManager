from fastapi import HTTPException, status
from backend.core.security import compare_passwords
from backend.models.models import UserBase
from backend.core.database import AsyncSessionFactory
from sqlalchemy import delete, select, update

from backend.schemas.role_enum import RoleList

async def check_user_by_email(email: str) -> bool:

    async with AsyncSessionFactory() as session:
        stmt = select(UserBase).where(UserBase.email == email)
        data = await session.execute(stmt)
        result = bool(data.scalar())

    return result

async def create_user(email: str, first_name: str, last_name: str,
                      password_hash: str, password_salt: str) -> None:
    
    async with AsyncSessionFactory() as session:
        user = await check_user_by_email(email=email)

        if not user:
            session.add(UserBase(
                email = email,
                first_name=first_name,
                last_name = last_name,
                password_hash = password_hash,
                password_salt = password_salt
            ))
            await session.commit()


async def approve_user(email: str, password: str) -> bool:
   async with AsyncSessionFactory() as session:
        
        stmt = select(UserBase).where(UserBase.email == email)
        data = await session.execute(stmt)
        user = data.scalar_one_or_none()

        if user:
            check = compare_passwords(user.password_hash, user.password_salt, password)
            await session.commit()
        else:
            return False
        
        return check
    

async def get_user_data_by_email(email : str):
    async with AsyncSessionFactory() as session:
        try:
            stmt = select(UserBase).where(UserBase.email == email)
            user = await session.execute(stmt)
            user = user.scalar_one_or_none()

            if user:
                data = {
                    'id':user.id,
                    'first_name':user.first_name,
                    'last_name':user.last_name,
                    'email':user.email,
                    'role':user.role,
                    'avatar_url':user.avatar_url,
                    'created_at':user.created_at,
                    # 'projects_lead':user.projects_lead,
                    'phone':user.phone,
                    }
        
            return data
        
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Юзер не обнаружен {e}')
        

async def delete_users():
    async with AsyncSessionFactory() as session:
        stmt = delete(UserBase)
        await session.execute(stmt)
        await session.commit()


async def get_user_data_by_id(id : int):
    async with AsyncSessionFactory() as session:
        try:
            stmt = select(UserBase).where(UserBase.id == id)
            user = await session.execute(stmt)
            user = user.scalar_one_or_none()
            data = {
                    'id':user.id,
                    'first_name':user.first_name,
                    'last_name':user.last_name,
                    'email':user.email,
                    'role':user.role,
                    'avatar_url':user.avatar_url,
                    'created_at':user.created_at,
                    # 'projects_lead':user.projects_lead,
                    'phone':user.phone,
                }
            
            return data
        
        except:
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Юзер не обнаружен {user} k')


async def all_users():
    async with AsyncSessionFactory() as session:
        stmt = select(UserBase)
        data = await session.execute(stmt)
        data = data.scalars().all()

        users = [user.to_dict() for user in data]
        await session.commit()
    
    return users


async def update_role_email(role: RoleList, email: str):
    async with AsyncSessionFactory() as session:
        try:
            stmt = update(UserBase).filter(UserBase.email == email).values(role = role.role.value)
            await session.execute(stmt)
            await session.commit()
        except Exception as e:
            raise e


async def change_user_name(email: str, first_name: str, last_name: str):
    async with AsyncSessionFactory() as session:
        stmt = update(UserBase).filter(UserBase.email == email).values(first_name = first_name, last_name=last_name)
        await session.execute(stmt)
        await session.commit()
    