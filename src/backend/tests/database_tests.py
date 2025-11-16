import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.models.models import Base


@pytest.fixture
def test_db():
    test_db_url = 'sqlite:///test_db.db'
    engine = create_engine(
        url = test_db_url,
        connect_args={'check_same_thread' : False}
    )

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()


def test_create_operations():
    pass