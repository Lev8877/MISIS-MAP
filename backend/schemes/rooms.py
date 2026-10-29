from pydantic import BaseModel, ConfigDict


class RoomTypeData(BaseModel):
    name: str
    category: str

    model_config = ConfigDict(from_attributes=True)


class RoomData(BaseModel):
    id: int
    number: str
    name: str
    area: float | None
    capacity: int | None
    floor_id: int
    room_type: RoomTypeData

    model_config = ConfigDict(from_attributes=True)


class GetRoomsResponse(BaseModel):
    rooms: list[RoomData]
