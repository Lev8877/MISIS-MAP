from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, or_

from fastapi import HTTPException

from models.rooms import Room


async def get_rooms(session: AsyncSession, floor_id: int | None):
    statement = select(Room)

    if floor_id is not None:
        statement = statement.where(Room.floor_id == floor_id)

    statement = statement.order_by(Room.number)

    result = await session.execute(statement)
    rooms = result.scalars().all()

    return {
        'rooms': rooms
    }


async def get_room(session: AsyncSession, room_id: int):
    result = await session.execute(select(Room).where(Room.id == room_id))
    room = result.scalar_one_or_none()

    if room is None:
        raise HTTPException(status_code=404, detail='Room is not found')

    return room


async def search_rooms(session: AsyncSession, query: str):
    statement = select(Room).where(or_(Room.number.ilike(f'%{query}%'), Room.name.ilike(f'%{query}%')))
    statement = statement.order_by(Room.number)

    result = await session.execute(statement)
    rooms = result.scalars().all()

    return {
        'rooms': rooms
    }
