from sqlalchemy import func
from app.models.log_entry import LogEntry


def get_top_errors(db, log_id: int, limit: int = 5):
    return (
        db.query(
            LogEntry.message,
            func.count(LogEntry.id).label("count")
        )
        .filter(
            LogEntry.log_id == log_id,
            LogEntry.level == "ERROR"
        )
        .group_by(LogEntry.message)
        .order_by(func.count(LogEntry.id).desc())
        .limit(limit)
        .all()
    )