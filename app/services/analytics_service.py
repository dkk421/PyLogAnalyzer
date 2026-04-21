from app.rep.analytics_repository import get_top_errors
from app.rep.log_file_repository import get_log_file_by_id


class AnalyticsService:
    def __init__(self, db):
        self.db = db

    def get_top_errors(self, log_id: int):
        log = get_log_file_by_id(self.db, log_id)

        if log is None:
            return None

        results = get_top_errors(self.db, log_id)

        return [
            {"message": r[0], "count": r[1]}
            for r in results
        ]