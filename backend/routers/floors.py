from schemes.floors import GetFloorsResponse, FloorData

from services.floors import get_floors, get_floor

from fastapi import APIRouter

router = APIRouter()


@router.get('/floors', response_model=GetFloorsResponse)
async def get_floors_router():
    return await get_floors()


@router.get('/floors/{floor_id}', response_model=FloorData)
async def get_floor_router(floor_id: int):
    return await get_floor(floor_id=floor_id)
