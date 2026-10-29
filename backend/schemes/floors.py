from pydantic import BaseModel, ConfigDict


class FloorData(BaseModel):
    id: int
    building: str
    number: int
    name: str
    plan_url: str

    model_config = ConfigDict(from_attributes=True)


class GetFloorsResponse(BaseModel):
    floors: list[FloorData]
