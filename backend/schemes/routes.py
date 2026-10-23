from pydantic import BaseModel


class NodeData(BaseModel):
    id: int
    floor_id: int
    x: float
    y: float


class GetRouteResponse(BaseModel):
    distance: float
    nodes: list[NodeData]
