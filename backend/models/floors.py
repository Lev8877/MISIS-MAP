from database import Base

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, UniqueConstraint


class Floor(Base):
    __tablename__ = 'floors'

    __table_args__ = (UniqueConstraint('building', 'number'),)

    id: Mapped[int] = mapped_column(primary_key=True)
    building: Mapped[str] = mapped_column(String(10))
    number: Mapped[int] = mapped_column()
    name: Mapped[str] = mapped_column(String(100))
    plan_url: Mapped[str] = mapped_column(String(255))
