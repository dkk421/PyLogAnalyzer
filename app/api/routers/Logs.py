from fastapi import APIRouter, UploadFile, File
from app.services.file_service import save_file
from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.rep.log_file_repository import create_log_file

from app.services.parser_service import parse_line
from app.rep.log_entry_repository import create_entries

from app.rep.stats_repository import get_log_stats

from app.rep.log_entry_query_repository import get_entries

from fastapi import HTTPException
from app.rep.log_file_repository import get_log_file_by_id

from app.services.log_service import LogService

from app.services.stats_service import StatsService
from fastapi import HTTPException

from app.schemas.log import LogUploadResponse, LogStatsResponse, LogEntryResponse

from app.schemas.log import LogFileResponse
from fastapi import HTTPException

from fastapi import BackgroundTasks

from app.services.analytics_service import AnalyticsService
from app.schemas.log import TopErrorResponse

router = APIRouter()

@router.post("/upload", response_model=LogUploadResponse)
async def upload(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    background_tasks: BackgroundTasks = None
):
    service = LogService(db)
    return service.upload_log(file, background_tasks)

@router.get("/{log_id}/stats", response_model=LogStatsResponse)
async def get_stats(log_id: int, db: Session = Depends(get_db)):
    service = StatsService(db)
    stats = service.get_stats(log_id)

    if stats is None:
        raise HTTPException(status_code=404, detail="Log file not found")

    return stats

@router.get("/{log_id}/entries", response_model=list[LogEntryResponse])
async def get_log_entries(
    log_id: int,
    db: Session = Depends(get_db),
    level: str | None = None,
    limit: int = 100,
):
    log_file = get_log_file_by_id(db, log_id)

    if log_file is None:
        raise HTTPException(status_code=404, detail="Log file not found")

    entries = get_entries(db, log_id=log_id, level=level, limit=limit)

    return [
        {
            "id": entry.id,
            "timestamp": entry.timestamp,
            "level": entry.level,
            "message": entry.message,
            "raw_line": entry.raw_line,
        }
        for entry in entries
    ]

@router.get("/{log_id}/stats")
async def get_stats(log_id: int, db: Session = Depends(get_db)):
    log_file = get_log_file_by_id(db, log_id)

    if log_file is None:
        raise HTTPException(status_code=404, detail="Log file not found")

    stats = get_log_stats(db, log_id)
    return stats


@router.get("/{log_id}", response_model=LogFileResponse)
async def get_log(log_id: int, db: Session = Depends(get_db)):
    service = LogService(db)
    log = service.get_log(log_id)

    if log is None:
        raise HTTPException(status_code=404, detail="Log file not found")

    return log

@router.get("/{log_id}/top-errors", response_model=list[TopErrorResponse])
async def top_errors(log_id: int, db: Session = Depends(get_db)):
    service = AnalyticsService(db)
    result = service.get_top_errors(log_id)

    if result is None:
        raise HTTPException(status_code=404, detail="Log file not found")

    return result