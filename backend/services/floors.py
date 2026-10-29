from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from fastapi import HTTPException

from models.floors import Floor


async def get_floors(session: AsyncSession):
    result = await session.execute(select(Floor).order_by(Floor.building, Floor.number))
    floors = result.scalars().all()

    return {
        'floors': floors
    }


async def get_floor(session: AsyncSession, floor_id: int):
    result = await session.execute(select(Floor).where(Floor.id == floor_id))
    floor = result.scalar_one_or_none()

    if floor is None:
        raise HTTPException(status_code=404, detail='Floor is not found')

    return floor
