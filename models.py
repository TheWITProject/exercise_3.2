
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Table
from sqlalchemy.orm import relationship

Base = declarative_base()

class Task(Base):
    __tablename__ = "tasks"

    # add properties here
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable = False) #field is required so cannot be nullable
    description = Column(String)
    priority = Column(Integer)
    due_date = Column(Date)

    # add relationships here
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="tasks")


class User(Base):
    __tablename__ = "zoos"

    # add properties here
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable = False)

    # add relationships here
    tasks = relationship("User", back_populates="users") #ONE-TO- MANY relation 
