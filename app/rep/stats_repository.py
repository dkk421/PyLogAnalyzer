from sqlalchemy import func
from app.models.log_entry import LogEntry


def get_log_stats(db, log_id: int):
    total_entries = db.query(func.count(LogEntry.id)).filter(LogEntry.log_id == log_id).scalar()

    error_count = db.query(func.count(LogEntry.id)).filter(
        LogEntry.log_id == log_id,
        LogEntry.level == "ERROR"
    ).scalar()

    warning_count = db.query(func.count(LogEntry.id)).filter(
        LogEntry.log_id == log_id,
        LogEntry.level == "WARNING"
    ).scalar()

    info_count = db.query(func.count(LogEntry.id)).filter(
        LogEntry.log_id == log_id,
        LogEntry.level == "INFO"
    ).scalar()

    unknown_count = db.query(func.count(LogEntry.id)).filter(
        LogEntry.log_id == log_id,
        LogEntry.level == "UNKNOWN"
    ).scalar()

    return {
        "log_id": log_id,
        "total_entries": total_entries,
        "error_count": error_count,
        "warning_count": warning_count,
        "info_count": info_count,
        "unknown_count": unknown_count,
    }