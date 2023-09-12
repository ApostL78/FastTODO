from datetime import datetime

from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, ForeignKey, \
    Boolean, MetaData


metadata_auth = MetaData()

user = Table(
    "user",
    metadata_auth,
    Column("id", Integer, primary_key=True),
    Column("email", String(length=320), unique=True, index=True, nullable=False),
    Column("username", String(length=50), nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("hashed_password", String, nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
)