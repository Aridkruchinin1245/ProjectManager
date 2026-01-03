from sqlalchemy import select
from backend.core.database import AsyncSessionFactory
from backend.crud.users_crud import get_user_data_by_email, get_user_data_by_id
from backend.models.models import TaskBase

async def create_new_task(description: str, email: str, project_id: int):
    async with AsyncSessionFactory() as session:
        user = await get_user_data_by_email(email)
        user_id = user['id']

        session.add(TaskBase(
            description = description,
            declarant_id = user_id,
            project_id = project_id
        ))

        await session.commit()


async def get_task_id(id: int):
    async with AsyncSessionFactory() as session:
        query = select(TaskBase).where(TaskBase.project_id == id)
        data = await session.execute(query)
        data = data.scalars().all()

        extended_data = []

    for task in data:
        user_data = await get_user_data_by_id(task.declarant_id)
        name = f'{user_data['first_name']} {user_data['last_name']}'

        task.declarant_name = name

        extended_data.append(task)

    return extended_data
