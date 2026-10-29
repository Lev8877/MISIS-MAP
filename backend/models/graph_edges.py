from database import Base

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey


class GraphEdge(Base):
    __tablename__ = 'graph_edges'

    id: Mapped[int] = mapped_column(primary_key=True)
    node_from_id: Mapped[int] = mapped_column(ForeignKey('graph_nodes.id'))
    node_to_id: Mapped[int] = mapped_column(ForeignKey('graph_nodes.id'))
    length_meters: Mapped[float] = mapped_column()
    edge_type: Mapped[str] = mapped_column(String(50))
