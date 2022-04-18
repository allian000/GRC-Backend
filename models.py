# Database models table
from ast import Str
from sqlalchemy import Boolean, Column, Integer, String
from database import Base

class Record(Base):
    __tablename__ = "command_record"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(String(32),nullable=False)
    time = Column(String(32),nullable=False)
    command = Column(Integer,nullable=False)
    image_url = Column(String(32),nullable=False)
    state = Column(String(32),nullable=False)