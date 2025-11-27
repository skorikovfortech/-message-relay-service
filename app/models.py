from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import ForeignKey, func
from datetime import datetime

from app.core.base import Base


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    telegram_id: Mapped[int] = mapped_column(unique=True)


class Messages(Base):
    __tablename__ = "messages"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    text: Mapped[str]
    message_date: Mapped[datetime] = mapped_column(server_default=func.now())
