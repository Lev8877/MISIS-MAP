from schemes.rooms import GetRoomsResponse, RoomData

from services.rooms import get_rooms, get_room, search_rooms

from fastapi import APIRouter

router = APIRouter()


@router.get('/rooms', response_model=GetRoomsResponse)
async def get_rooms_router(floor_id: int | None = None):
    return await get_rooms(floor_id=floor_id)


@router.get('/rooms/{room_id}', response_model=RoomData)
async def get_room_router(room_id: int):
    return await get_room(room_id=room_id)


@router.get('/search', response_model=GetRoomsResponse)
async def search_rooms_router(query: str):
    return await search_rooms(query=query)
