from sqlalchemy import Column, Integer, String, Float, DateTime , Boolean
from sqlalchemy.sql import func
from database import Base       


class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    object_detect = Column(String,nullable=False)
    confidence = Column(Float)
    camera_id = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    is_alert = Column(Boolean, default=False)


    