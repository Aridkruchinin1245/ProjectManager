from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import Column, Integer, VARCHAR, DateTime, ForeignKey, String
from datetime import datetime

class Base(DeclarativeBase): pass

class Users(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    email = Column(VARCHAR(320), unique=True, nullable=False)
    password_hash = Column(VARCHAR(100), nullable=False)
    first_name = Column(VARCHAR(50), nullable=False)
    last_name = Column(VARCHAR(50), nullable=False)
    avatar_url = Column(VARCHAR(100), unique=True)
    role = Column(VARCHAR(100))
    created_at = Column(DateTime, default=datetime.now, nullable=False)

    project_lead = relationship('Projects', back_populates='leader')
    command_member = relationship('Members', back_populates='user')
    declarations = relationship('Tasks', back_populates='declarant')


class Projects(Base):
    __tablename__ = "projects"

    project_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title = Column(VARCHAR(100), nullable=False)
    description = Column(String, nullable=False)
    status = Column(VARCHAR(20), nullable=False)
    lead_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    start_date = Column(DateTime)
    deadline = Column(DateTime)

    leader = relationship('Users', back_populates='project_lead')
    command = relationship('Members', back_populates='project')
    tasks = relationship('Tasks', back_populates='project_instance')

class Members(Base):
    __tablename__ = "members"

    member_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    project_id = Column(Integer, ForeignKey('projects.project_id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    joined_at = Column(DateTime, default=datetime.now)
    role = Column(VARCHAR(30))

    project = relationship('Projects', back_populates='command')
    user = relationship('Users', back_populates='command_member')

class Tasks(Base):
    __tablename__ = "tasks"

    task_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    description = Column(String, nullable=False)
    declarant = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    project_id = Column(Integer, ForeignKey('projects.project_id'))

    project_instance = relationship('Projects', back_populates='tasks')
    user_declarant = relationship('Users', back_populates='declarations')

if __name__ == '__main__':
    pass