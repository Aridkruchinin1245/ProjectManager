from sqlalchemy import select
from backend.crud.users_crud import get_user_data_by_email
from backend.models.models import CommandBase, CommandMembers
from backend.core.database import AsyncSessionFactory

async def select_all_commands():
    async with AsyncSessionFactory() as session:
        stmt = select(CommandBase)
        data = await session.execute(stmt)
        data = data.scalars().all()
    return data


async def create_command(user_id: list, email: str):
    async with AsyncSessionFactory() as session:
        data = await get_user_data_by_email(email)
        creator_id = data['id']

        new_command = CommandBase(creator_id=creator_id)
        session.add(new_command)
        await session.flush()
        command_id = new_command.id
        await session.commit()

        users = list([
            CommandMembers(user_id=id, command_id=command_id) for id in user_id
        ])

        session.add_all(users)
        await session.commit()
