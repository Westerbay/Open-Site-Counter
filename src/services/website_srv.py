from datetime import datetime, timezone
from db.models import WebsiteRow
from repositories.website_repo import WebsiteRepository
from core.crypto import encrypt

class WebsiteService:
    def __init__(self, repo: WebsiteRepository):
        self.repo = repo

    def register(self, hostname: str, ip: str) -> None:
        row = WebsiteRow(
            hostname=encrypt(hostname),
            ip=encrypt(ip),
            date=datetime.now(timezone.utc)
        )
        self.repo.add(row)
