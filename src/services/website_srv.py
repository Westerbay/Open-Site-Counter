from datetime import datetime, timezone
from db.models import WebsiteRow
from repositories.website_repo import WebsiteRepository
from core.crypto import *
from collections import defaultdict
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker

import base64
import io


class WebsiteService:
    def __init__(self, repo: WebsiteRepository):
        self.repo = repo

    def register(self, hostname: str, ip: str) -> None:
        row = WebsiteRow(
            hostname=hash_value(hostname),
            ip=hash_value(ip),
            date=datetime.now(timezone.utc)
        )
        self.repo.add(row)

    def get_stats(self, hostname: str) -> dict:
        hostname_hash = hash_value(hostname)
        rows = self.repo.get_by_hostname(hostname_hash)

        if not rows:
            return {"ok": False, "message": "Hostname not found"}

        visits = [(r.ip, r.date) for r in rows]

        total_occurrences = len(visits)
        unique_visitors = len(set(ip for ip, _ in visits))

        now = datetime.now(timezone.utc)
        this_month = now.month
        this_year = now.year

        daily_total = defaultdict(int)
        daily_unique = defaultdict(set)

        for ip, date in visits:
            if date.year == this_year and date.month == this_month:
                day = date.date()
                daily_total[day] += 1
                daily_unique[day].add(ip)

        days = sorted(daily_total.keys())
        total_series = [daily_total[d] for d in days]
        unique_series = [len(daily_unique[d]) for d in days]

        # --- Matplotlib ---
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(days, total_series, label="Total connections", marker="o")
        ax.plot(days, unique_series, label="Unique connections", marker="s")
    
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%d %b"))
        ax.xaxis.set_major_locator(mdates.DayLocator())
        fig.autofmt_xdate()  

        ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))
        ax.set_xlabel("Day")
        ax.set_ylabel("Connections")
        ax.set_title(f"Statistics for {hostname}")
        ax.legend()
        ax.grid(True, linestyle="--", alpha=0.4)

        # Export base64
        buf = io.BytesIO()
        plt.tight_layout()
        plt.savefig(buf, format="png", dpi=150)
        plt.close(fig)
        img_b64 = base64.b64encode(buf.getvalue()).decode()

        return {
            "ok": True,
            "hostname": hostname,
            "total_occurrences": total_occurrences,
            "unique_visitors": unique_visitors,
            "graph_png_base64": img_b64
        }
