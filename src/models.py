from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, Text, Boolean, \
    ForeignKey, TIMESTAMP

metadata = MetaData()

task = Table(
    "task",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(50), nullable=False),
    Column("description", Text),
    Column("completed", Boolean, default=False),
    Column("created", TIMESTAMP, nullable=False, default=datetime.utcnow),
    # Column("user", ForeignKey("user.id"), nullable=False),
)
