from app.rep.stats_repository import get_log_stats
from app.rep.log_file_repository import get_log_file_by_id


class StatsService:
    def __init__(self, db):
        self.db = db

    def get_stats(self, log_id: int):
        log_file = get_log_file_by_id(self.db, log_id)

        if log_file is None:
            return None

        return get_log_stats(self.db, log_id)