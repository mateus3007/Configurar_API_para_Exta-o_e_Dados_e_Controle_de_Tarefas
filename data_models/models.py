from sqlalchemy import Column, String,  Integer, Date,ForeignKey 
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    created = Column(Date)


class Task(Base):
    __tablename__ = 'task'

    id_func = Column(Integer, primary_key=True)
    created = Column(Date)
    updated = Column(Date)
    task = Column(String)
    priority = Column(String)
    status = Column(String)
    user = relationship("user")
    userID = Column(Integer, ForeignKey('user.id'))
        