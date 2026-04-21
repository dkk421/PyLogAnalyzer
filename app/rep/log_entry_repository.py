from app.models.log_entry import LogEntry


def create_entries(db, entries: list[dict], log_id: int):
    objects = []

    for entry in entries:
        obj = LogEntry(
            log_id=log_id,
            timestamp=entry["timestamp"],
            level=entry["level"],
            message=entry["message"],
            raw_line=entry["raw_line"]
        )
        objects.append(obj)

    db.add_all(objects)
    db.commit()