from pydantic import BaseModel


class FloorData(BaseModel):
    id: int
    building: str
    number: int
    plan_url: str


class GetFloorsResponse(BaseModel):
    floors: list[FloorData]
