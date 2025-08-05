from sqlalchemy import Table, Column, Integer, String
from app.db.database import metadata


movies = Table(
    "movies",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("movie_name", String, nullable=False),
)
