from app.services.file_service import save_file
from app.rep.log_file_repository import create_log_file
from app.rep.log_entry_repository import create_entries
from app.services.parser_service import parse_line

from app.rep.log_file_repository import get_log_file_by_id

class LogService:
    def __init__(self, db):
        self.db = db

    def upload_log(self, file, background_tasks):
        file_path = save_file(file)

        log = create_log_file(self.db, file.filename, str(file_path))

        background_tasks.add_task(
            self.process_log,
            log.id,
            str(file_path)
        )

        return {
            "log_id": log.id,
            "status": "uploaded"
        }

    def get_log(self, log_id: int):
        log = get_log_file_by_id(self.db, log_id)

        if log is None:
            return None

        return {
            "id": log.id,
            "filename": log.filename,
            "path": log.path,
            "status": log.status,
            "uploaded_at": log.uploaded_at,
        }

    def process_log(self, log_id: int, file_path: str):
        from app.rep.log_entry_repository import create_entries
        from app.services.parser_service import parse_line
        from app.rep.log_file_repository import update_status, get_log_file_by_id

        log = get_log_file_by_id(self.db, log_id)

        try:
            update_status(self.db, log, "processing")

            with open(file_path, "r") as f:
                lines = f.readlines()

            parsed = []
            for line in lines:
                result = parse_line(line)
                if result:
                    parsed.append(result)

            create_entries(self.db, parsed, log_id)

            update_status(self.db, log, "processed")

        except Exception:
            update_status(self.db, log, "failed")