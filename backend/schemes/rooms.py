from pydantic import BaseModel


class RoomData(BaseModel):
    id: int
    number: str
    name: str
    type: str
    floor_id: int


class GetRoomsResponse(BaseModel):
    rooms: list[RoomData]
