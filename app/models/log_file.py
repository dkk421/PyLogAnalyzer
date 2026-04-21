from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.db.base import Base


class LogFile(Base):
    __tablename__ = "log_files"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    path = Column(String)
    status = Column(String, default="uploaded")
    uploaded_at = Column(DateTime, default=datetime.utcnow)