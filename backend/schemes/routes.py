from pydantic import BaseModel, ConfigDict


class NodeData(BaseModel):
    id: int
    floor_id: int
    x: float
    y: float

    model_config = ConfigDict(from_attributes=True)


class GetRouteResponse(BaseModel):
    distance: float
    nodes: list[NodeData]
