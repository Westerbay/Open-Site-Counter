from sqlalchemy import insert
from sqlalchemy import select
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
            
    def get_by_hostname(self, hostname: str) -> list[WebsiteRow]:
        rows = []
        with engine.begin() as conn:
            stmt = select(websites).where(websites.c.hostname == hostname)
            result = conn.execute(stmt).fetchall()
            for r in result:
                rows.append(
                    WebsiteRow(
                        hostname=r.hostname, 
                        ip=r.ip, 
                        date=r.date
                    )
                )
        return rows
