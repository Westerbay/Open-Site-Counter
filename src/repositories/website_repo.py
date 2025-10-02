from sqlalchemy import insert
from db.session import engine, websites
from db.models import WebsiteRow

class WebsiteRepository:
    def add(self, row: WebsiteRow) -> None:
        with engine.begin() as conn:
            conn.execute(
                insert(websites).values(
                    hostname=row.hostname,
                    ip=row.ip,
                    date=row.date
                )
            )
