# Database operating
from sqlalchemy.orm import Session
import models, schemas

# get all record
def get_all_record(db:Session):
    return db.query(models.Record)

# create new record
def db_create_record(db:Session,record:schemas.RecordCreate):
    db_record = models.Record(date = record.date,time = record.time,command = record.command,image_url = record.image_url,state = record.state)
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record