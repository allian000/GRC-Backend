# Model validation
from pydantic import BaseModel, HttpUrl

class RecordBase(BaseModel):
    command : int

class RecordCreate(RecordBase):
    """
    request model validation：
    command
    date
    time
    """
    date : str
    time : str
    image_url : str
    state : str

class Record(RecordBase):
    """
    model validation：
    id
    command
    date
    time
    image_url
    """
    id : int

    class Config:
        orm_mode = True