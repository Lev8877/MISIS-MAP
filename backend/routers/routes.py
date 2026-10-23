from schemes.routes import GetRouteResponse

from services.routes import get_route

from fastapi import APIRouter

router = APIRouter()


@router.get('/route', response_model=GetRouteResponse)
async def get_route_router(from_room_id: int, to_room_id: int):
    return await get_route(from_room_id=from_room_id, to_room_id=to_room_id)
