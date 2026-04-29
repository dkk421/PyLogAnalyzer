from pydantic import BaseModel
from datetime import datetime

class LogUploadResponse(BaseModel):
    log_id: int
    status: str


class LogStatsResponse(BaseModel):
    log_id: int
    total_entries: int
    error_count: int
    warning_count: int
    info_count: int
    unknown_count: int


class LogEntryResponse(BaseModel):
    id: int
    timestamp: str | None
    level: str
    message: str
    raw_line: str

class LogFileResponse(BaseModel):
    id: int
    filename: str
    path: str
    status: str
    uploaded_at: datetime

class TopErrorResponse(BaseModel):
    message: str
    count: int