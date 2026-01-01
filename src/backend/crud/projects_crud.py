from backend.crud.users_crud import get_user_data_by_id
from backend.models.models import ProjectBase, UserBase
from backend.core.database import AsyncSessionFactory
from sqlalchemy import delete, select
from datetime import datetime 
from typing import Optional

async def compose_leader_name_id(data, id: int) -> str:
    first_name = await get_user_data_by_id(data[id]['lead_id'])
    first_name = first_name['first_name']

    last_name = await get_user_data_by_id(data[id]['lead_id'])
    last_name = last_name['last_name']

    full = first_name + ' ' + last_name
    return full

async def compose_creator_name_id(data, id: int) -> str:
    first_name = await get_user_data_by_id(data[id]['creator_id'])
    first_name = first_name['first_name']

    last_name = await get_user_data_by_id(data[id]['creator_id'])
    last_name = last_name['last_name']

    full = first_name + ' ' + last_name
    return full


async def create_project(email : str, title: str, description: str, command_id: int,
                         deadline: datetime, start_date: Optional[datetime] = None,
                         lead_id: Optional[int] = None) -> None:
    async with AsyncSessionFactory() as session:

        stmt = select(UserBase).where(UserBase.email == email)
        data = await session.execute(stmt)
        creator_id = data.scalar_one_or_none().id

        if creator_id:
            if not lead_id:
                lead_id = creator_id

        session.add(ProjectBase(
            title = title,
            lead_id = lead_id,
            description = description,
            deadline = deadline,
            start_date = start_date,
            creator_id = creator_id,
            command_id = command_id
        ))
        await session.commit()


async def get_projects(): 
    try:
        async with AsyncSessionFactory() as session:
            stmt = select(ProjectBase)
            result = await session.scalars(stmt)
            scalar = result.all()

            data = [project.to_dict() for project in scalar]
            await session.commit()

        for id in range(len(data)):
            
            leader_name = await compose_leader_name_id(data, id)
                              
            creator_name = await compose_creator_name_id(data, id)
                              
            data[id]['leader_name'] = leader_name
            data[id]['creator_name'] = creator_name

        return data
    
    except Exception as e:
        raise 


async def delete_projects():
    async with AsyncSessionFactory() as session:
        stmt = delete(ProjectBase)
        await session.execute(stmt)
        await session.commit()
        

