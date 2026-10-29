from typing import TYPE_CHECKING

from database import Base

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey


if TYPE_CHECKING:
    from models.room_types import RoomType


class Room(Base):
    __tablename__ = 'rooms'

    id: Mapped[int] = mapped_column(primary_key=True)
    floor_id: Mapped[int] = mapped_column(ForeignKey('floors.id'))
    room_type_id: Mapped[int] = mapped_column(ForeignKey('room_types.id'))
    number: Mapped[str] = mapped_column(String(20), unique=True)
    name: Mapped[str] = mapped_column(String(255))
    area: Mapped[float | None] = mapped_column()
    capacity: Mapped[int | None] = mapped_column()

    room_type: Mapped['RoomType'] = relationship(lazy='selectin')
