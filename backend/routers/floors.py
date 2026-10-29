from schemes.floors import GetFloorsResponse, FloorData

from services.floors import get_floors, get_floor

from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from dependencies import get_session

router = APIRouter()


@router.get('/floors', response_model=GetFloorsResponse)
async def get_floors_router(session: AsyncSession = Depends(get_session)):
    return await get_floors(session=session)


@router.get('/floors/{floor_id}', response_model=FloorData)
async def get_floor_router(floor_id: int, session: AsyncSession = Depends(get_session)):
    return await get_floor(session=session, floor_id=floor_id)
