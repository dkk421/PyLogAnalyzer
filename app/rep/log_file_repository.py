from app.models.log_file import LogFile


def create_log_file(db, filename: str, path: str):
    log = LogFile(filename=filename, path=path)
    db.add(log)
    db.commit()
    db.refresh(log)
    return log

def get_log_file_by_id(db, log_id: int):
    return db.query(LogFile).filter(LogFile.id == log_id).first()

def update_status(db, log, status: str):
    log.status = status
    db.commit()