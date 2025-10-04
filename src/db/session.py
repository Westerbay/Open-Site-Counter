from sqlalchemy import create_engine, MetaData, Table, Column, String, DateTime

engine = create_engine("sqlite:///./websites.db", future=True)
metadata = MetaData()

websites = Table(
    "websites",
    metadata,
    Column("hostname", String, nullable=False),
    Column("ip", String, nullable=False),
    Column("date", DateTime(timezone=True), nullable=False),
)

def init_db():
    metadata.create_all(bind=engine)
