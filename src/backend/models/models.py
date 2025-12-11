from sqlalchemy.orm import DeclarativeBase, relationship, Mapped, mapped_column
from typing import Optional
from sqlalchemy import String, Integer, Date, ForeignKey, Text, CheckConstraint
from datetime import date
 

class Base(DeclarativeBase): pass


class UserBase(Base):

    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(Integer, primary_key = True, autoincrement = True)
    email: Mapped[str] = mapped_column(String(255), unique = True, nullable = False)
    phone: Mapped[str] = mapped_column(String(255), unique = True, nullable = True)
    password_hash: Mapped[str] = mapped_column(String(255), nullable = False)
    password_salt: Mapped[str] = mapped_column(String(255), nullable = False)
    first_name: Mapped[str] = mapped_column(String(50), nullable = False)
    last_name: Mapped[str] = mapped_column(String(50), nullable = False)
    avatar_url: Mapped[Optional[str]] = mapped_column(nullable = True)
    role: Mapped[Optional[str]] = mapped_column(nullable = True)
    created_at: Mapped[date] = mapped_column(Date, default=date.today())

    projects_lead = relationship("ProjectBase", backref="leader")
    task_declarator = relationship("TaskBase", backref="declarator")
    membership = relationship('CommandBase', backref="user")
    creatorship = relationship("ProjectBase", backref="creator")

    def __repr__(self) -> str:
        return f"""User (first_name: {self.first_name},
                last_name: {self.last_name},
                email: {self.email},
                role: {self.role},
                created_at: {self.created_at},
                phone: {self.phone})"""
    

    def to_dict(self):
        data = {}

        for c in self.__table__.columns:
            if c.name != 'password_salt' and c.name != 'password_hash':
                value = getattr(self, c.name)
                data[c.name] = value

        return data
    

class ProjectBase(Base):

    __tablename__ = "projects"

    __table_args__ = (
        CheckConstraint('deadline > created_at', name='deadline_after_creation'),
        CheckConstraint("status IN ('Не в работе', 'В работе', 'Завершен')", name='valid_status'),
    )

    project_id: Mapped[int] = mapped_column(Integer, autoincrement = True, primary_key = True)
    title: Mapped[str] = mapped_column(String(255), unique = True)
    lead_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.user_id"))
    description: Mapped[str] = mapped_column(Text, nullable = False)
    status: Mapped[str] = mapped_column(String(30), default='Не в работе')
    created_at: Mapped[date] = mapped_column(Date, default=date.today())
    deadline: Mapped[date] = mapped_column(Date, nullable= False)
    creator_id: Mapped[str] = mapped_column(Integer, nullable=False)
    start_date: Mapped[date] = mapped_column(Date, default=date.today())

    command = relationship("CommandBase", backref = "project")

    def __repr__(self) -> str:
        return f"""Project (title: {self.title},
                            lead: {self.lead_id},
                            description: {self.description},
                            status: {self.status},
                            created_at: {self.created_at},
                            deadline: {self.deadline})"""
    
    def to_dict(self):
        data = {}

        for c in self.__table__.columns:
            value = getattr(self, c.name)
            data[c.name] = value

        return data


class TaskBase(Base):

    __tablename__ = 'tasks'

    task_id: Mapped[int] = mapped_column(Integer, primary_key = True, autoincrement = True)
    created_at: Mapped[date] = mapped_column(Date, default=date.today)
    description: Mapped[str] = mapped_column(Text, nullable = False)
    declarant_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.user_id"))
    project_id: Mapped[int] = mapped_column(Integer, ForeignKey("projects.project_id"))

    def __repr__(self) -> str:
        return f"""Task (
        task_id: {self.task_id},
        created_at: {self.created_at},
        description: {self.description},
        declarant_id: {self.declarant_id},
        project_id: {self.project_id})"""


class CommandBase(Base):

    __tablename__ = "commands"

    id: Mapped[int] = mapped_column(Integer, primary_key = True, autoincrement = True)
    project_id: Mapped[int] = mapped_column(Integer, ForeignKey("projects.project_id"), nullable = False)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.user_id"), nullable = False)
    joined_at: Mapped[date] = mapped_column(Date, default=date.today)
    role: Mapped[str] = mapped_column(String(30), nullable = False)
    command_id: Mapped[int] = mapped_column(Integer, unique=True)

    def __repr__(self) -> str:
        return f"""Command (
        created_at: {self.joined_at},
        project_id: {self.project_id},
        user_id: {self.user_id})"""
    

class CommandMetricBase(Base):
    
    __tablename__ = "command_metrics"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    command_id: Mapped[int] = mapped_column(Integer, ForeignKey('commands.command_id'), nullable=False,)
    succeed_project_percent: Mapped[int] = mapped_column(Integer, nullable=False)
    average_time: Mapped[int] = mapped_column(Integer, nullable=True)
    total_time: Mapped[int] = mapped_column(Integer, nullable=True)
    total_projects: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    def __repr__(self):
        return f"""Command metrics (
            id: {self.id},
            succeed_project_percent: {self.succeed_project_percent},
            average_time: {self.average_time},
            total_time: {self.total_time},
            total_projects: {self.total_projects}
        )"""


class UserMetricBase(Base):
    
    __tablename__ = "user_metrics"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.user_id'), nullable=False, unique=True)
    command_id: Mapped[int] = mapped_column(Integer, ForeignKey('commands.command_id'), nullable=False,)
    succeed_project_percent: Mapped[int] = mapped_column(Integer, nullable=False)
    average_time: Mapped[int] = mapped_column(Integer, nullable=True)
    total_time: Mapped[int] = mapped_column(Integer, nullable=True)
    total_projects: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    def __repr__(self):
            return f"""Command metrics (
                id: {self.id},
                succeed_project_percent: {self.succeed_project_percent},
                average_time: {self.average_time},
                total_time: {self.total_time},
                total_projects: {self.total_projects}
            )"""
