from database import Base

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey


class GraphNode(Base):
    __tablename__ = 'graph_nodes'

    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(String(50), unique=True)
    floor_id: Mapped[int] = mapped_column(ForeignKey('floors.id'))
    room_id: Mapped[int | None] = mapped_column(ForeignKey('rooms.id'), unique=True)
    x: Mapped[float] = mapped_column()
    y: Mapped[float] = mapped_column()
    description: Mapped[str] = mapped_column(String(255))
