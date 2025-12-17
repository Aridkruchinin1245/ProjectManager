from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.core.config import settings
from backend.models.models import Base
# from backend.services.logger import logger

DATABASE_URL = settings.DATABASE_URL

engine = create_engine(
    url = DATABASE_URL,
    connect_args={'check_same_thread': False}
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

def create_tables():
    try:
        Base.metadata.create_all(bind=engine)
        # logger.info('таблицы созданы')
    except Exception as e:
        # logger.error(f'Ошибка создания бд {e}')
        pass


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()