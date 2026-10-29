from database import Base

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String


class RoomType(Base):
    __tablename__ = 'room_types'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    category: Mapped[str] = mapped_column(String(100))
