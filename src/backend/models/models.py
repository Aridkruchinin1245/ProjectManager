from sqlalchemy.orm import DeclarativeBase, relationship, Mapped, mapped_column
from typing import Optional
from sqlalchemy import String, Integer, DateTime, ForeignKey, Text
from datetime import datetime

class Base(DeclarativeBase): pass


class UserBase(Base):

    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(Integer, primary_key = True, autoincrement = True)
    email: Mapped[str] = mapped_column(String(255), unique = True, nullable = False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable = False)
    password_salt: Mapped[str] = mapped_column(String(64), nullable = False)
    first_name: Mapped[str] = mapped_column(String(50), nullable = False)
    last_name: Mapped[str] = mapped_column(String(50), nullable = False)
    avatar_url: Mapped[Optional[str]] = mapped_column(nullable = True)
    role: Mapped[Optional[str]] = mapped_column(nullable = True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    projects_lead = relationship("ProjectBase", backref="leader")
    task_declarator = relationship("TaskBase", backref="declarator")
    membership = relationship('CommandBase', backref="user")

    def __repr__(self) -> str:
        return f"""User (first_name: {self.first_name},
                last_name: {self.last_name},
                email: {self.email},
                role: {self.role},
                created_at: {self.created_at})"""
    

class ProjectBase(Base):

    __tablename__ = "projects"

    project_id: Mapped[int] = mapped_column(Integer, autoincrement = True, primary_key = True)
    title: Mapped[str] = mapped_column(String(255), unique = True)
    lead_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.user_id"))
    description: Mapped[str] = mapped_column(Text, nullable = False)
    status: Mapped[str] = mapped_column(String(30), nullable = False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    deadline: Mapped[datetime] = mapped_column(DateTime, nullable= False)

    command = relationship("CommandBase", backref = "project")

    def __repr__(self) -> str:
        return f"""Project (title: {self.title},
                            lead: {self.lead_id},
                            description: {self.description},
                            status: {self.status},
                            created_at: {self.created_at},
                            deadline: {self.deadline})"""
    

class TaskBase(Base):

    __tablename__ = 'tasks'

    task_id: Mapped[int] = mapped_column(Integer, primary_key = True, autoincrement = True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
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
    joined_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    role: Mapped[str] = mapped_column(String(30), nullable = False)

    def __repr__(self) -> str:
        return f"""Command (
        created_at: {self.joined_at},
        project_id: {self.project_id},
        user_id: {self.user_id})"""