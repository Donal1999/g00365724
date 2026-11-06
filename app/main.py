from fastapi import Depends, FastAPI,Response, status, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from sqlalchemy.sql import Select
from app.database import engine, get_db
from app.models import Base, record_DB
from app.schemas import recordCreate, recordRead

app = FastAPI(title="Example template")

Base.metadata.create_all(bind=engine)

@app.get("/health")
def health():
    return{"status": "ok"}


@app.post("/requests", response_model= recordRead, status_code= status.HTTP_201_CREATED)
def createRecord(newRecord: recordCreate,   db: Session=Depends(get_db)):
    db_record = record_DB(**newRecord.model_dump())
    db.add(db_record)
    try:
        db.commit()
        db.refresh(db_record)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                detail= "Equiment Id or Student Id invalid ")
    return db_record

@app.get("/requsts",response_model=list[recordRead], status_code=status.HTTP_200_OK)
def getRecords(db:Session = Depends(get_db)):
    statement= Select(record_DB).order_by(record_DB.id)
    return db.execute(statement).scalars.all()
    
    
    


