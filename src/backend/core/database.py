from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy import create_engine
from backend.models.models import Base
from backend.core.config import settings
# from backend.services.logger import logger

async_engine = create_async_engine(
    url = settings.async_db_url,
    echo = True #ток на время разработки
)

AsyncSessionFactory = async_sessionmaker(
    bind=async_engine,
    autoflush=False,
    autocommit=False,
    class_=AsyncSession
)

def create_tables():
    sync_url = settings.sync_db_url
    sync_engine = create_engine(sync_url)
    Base.metadata.create_all(bind=sync_engine)