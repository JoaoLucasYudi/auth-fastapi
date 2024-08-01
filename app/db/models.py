from sqlalchemy import Column, String, INTEGER
from sqlalchemy.sql.sqltypes import Integer
from sqlalchemy.util.typing import TypeGuard

from app.db.connection import Base

class UserModel(Base):
    __tablename__ = 'users'
    id = Column('íd', Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column('name', String, nullable=False, unique=True)
    password = Column('password', String, nullable=False)
