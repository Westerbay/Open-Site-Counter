from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class WebsiteRow:
    hostname: str
    ip: str
    date: datetime
