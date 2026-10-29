from schemes.routes import GetRouteResponse

from services.routes import get_route

from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from dependencies import get_session

router = APIRouter()


@router.get('/route', response_model=GetRouteResponse)
async def get_route_router(from_room_id: int, to_room_id: int, session: AsyncSession = Depends(get_session)):
    return await get_route(session=session, from_room_id=from_room_id, to_room_id=to_room_id)
