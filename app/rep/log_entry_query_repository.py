from app.models.log_entry import LogEntry


def get_entries(db, log_id: int, level: str | None = None, limit: int = 100):
    query = db.query(LogEntry).filter(LogEntry.log_id == log_id)

    if level:
        query = query.filter(LogEntry.level == level)

    return query.limit(limit).all()