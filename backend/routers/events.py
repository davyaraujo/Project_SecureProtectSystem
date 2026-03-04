from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from database import get_db
import models, schemas
import json


router = APIRouter(prefix="/events", tags=["events"])

@router.get("/", response_model=list[schemas.EventResponse])

def get_events(db: Session = Depends(get_db)):
    events = db.query(models.Event).all()
    return events

@router.post("/", response_model=schemas.EventResponse)

async def create_event(event: schemas.User_Event,request:Request, db: Session = Depends(get_db)):
    db_event = models.Event(
        object_detect=event.object_detect,
        confidence=event.confidence,
        camera_id=event.camera_id,
        is_alert=event.is_alert
    )
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    manager  = request.app.state.manager 
    await manager.broadcast(json.dumps({
        "ID" : db_event.id,
        "object_detect" : db_event.object_detect,
        "confidence" : db_event.confidence,
        "camera_id" : db_event.camera_id,
        "is_alert" : db_event.is_alert,
        "created_at" : str(db_event.created_at)
    }))
    return db_event

