from fastapi import HTTPException

from fake_data import FLOORS


async def get_floors():
    return {
        'floors': FLOORS
    }


async def get_floor(floor_id: int):
    for floor in FLOORS:
        if floor['id'] == floor_id:
            return floor

    raise HTTPException(status_code=404, detail='Floor is not found')
