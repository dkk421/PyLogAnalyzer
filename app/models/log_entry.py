from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.base import Base


class LogEntry(Base):
    __tablename__ = "log_entries"

    id = Column(Integer, primary_key=True, index=True)
    log_id = Column(Integer, ForeignKey("log_files.id"))

    timestamp = Column(String)
    level = Column(String)
    message = Column(String)
    raw_line = Column(String)