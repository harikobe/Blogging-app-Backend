# models.py

from sqlalchemy import Column, Integer, String, Boolean,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from .database import engine
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text #for giving some conditions in the timestamp

Base = declarative_base()


Base.metadata.create_all(bind=engine)


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    completed = Column(Boolean, default=False)

    
