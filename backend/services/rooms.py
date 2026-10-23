from fastapi import HTTPException

from fake_data import ROOMS


async def get_rooms(floor_id: int | None):
    rooms = ROOMS

    if floor_id is not None:
        rooms = [room for room in ROOMS if room['floor_id'] == floor_id]

    return {
        'rooms': rooms
    }


async def get_room(room_id: int):
    for room in ROOMS:
        if room['id'] == room_id:
            return room

    raise HTTPException(status_code=404, detail='Room is not found')


async def search_rooms(query: str):
    query = query.lower()
    rooms = [room for room in ROOMS if query in room['number'].lower() or query in room['name'].lower()]

    return {
        'rooms': rooms
    }
