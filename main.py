from fastapi import FastAPI,Depends,HTTPException,responses
import crud,schemas
from database import SessionLocal,engine,Base
from sqlalchemy.orm import Session
import uvicorn
import json
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# create new record
@app.post("/createRecord/",response_model=schemas.Record)
def create_record(record: schemas.RecordCreate,db:Session = Depends(get_db)):
    return crud.db_create_record(db = db, record = record)

# get all record
@app.get("/allRecord",response_model_exclude_none=True)
def get_all_record(db:Session = Depends(get_db)):
    db_all_record = crud.get_all_record(db)
    arr = []
    for item in db_all_record:
        arr.append({"id":item.id,"date":item.date,"time":item.time,"command":item.command,"image_url":item.image_url,"state":item.state})
    return responses.JSONResponse({"data":arr})

# show image
@app.get("/images/{name}")
def show_image(name):
    path = "images/" + name
    return FileResponse(path)


# default config
if __name__ == '__main__':
    uvicorn.run(app=app,host="127.0.0.1",port=8000)