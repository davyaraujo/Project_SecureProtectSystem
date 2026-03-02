from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import models, schemas


router = APIRouter(prefix="/events", tags=["events"])

@router.get("/", response_model=list[schemas.EventResponse])

def get_events(db: Session = Depends(get_db)):
    events = db.query(models.Event).all()
    return events

@router.post("/", response_model=schemas.EventResponse)

def create_event(event: schemas.User_Event, db: Session = Depends(get_db)):
    db_event = models.Event(
        object_detect=event.object_detect,
        confidence=event.confidence,
        camera_id=event.camera_id,
        is_alert=event.is_alert
    )
    db.add(db_event)
    db.commit()
    db.refresh(db_event)    
    return db_event

