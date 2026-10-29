from schemes.rooms import GetRoomsResponse, RoomData

from services.rooms import get_rooms, get_room, search_rooms

from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from dependencies import get_session

router = APIRouter()


@router.get('/rooms', response_model=GetRoomsResponse)
async def get_rooms_router(session: AsyncSession = Depends(get_session), floor_id: int | None = None):
    return await get_rooms(session=session, floor_id=floor_id)


@router.get('/rooms/{room_id}', response_model=RoomData)
async def get_room_router(room_id: int, session: AsyncSession = Depends(get_session)):
    return await get_room(session=session, room_id=room_id)


@router.get('/search', response_model=GetRoomsResponse)
async def search_rooms_router(query: str, session: AsyncSession = Depends(get_session)):
    return await search_rooms(session=session, query=query)
