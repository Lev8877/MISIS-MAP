import asyncio
import json

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from dependencies import SessionLocal

from models.room_types import RoomType
from models.floors import Floor
from models.rooms import Room
from models.graph_nodes import GraphNode
from models.graph_edges import GraphEdge


async def import_data(session: AsyncSession, data: dict):
    await session.execute(text('TRUNCATE graph_edges, graph_nodes, rooms, floors, room_types RESTART IDENTITY'))

    room_types = {}
    for item in data['room_types']:
        room_type = RoomType(name=item['name'], category=item['category'])
        session.add(room_type)
        room_types[item['name']] = room_type

    floors = {}
    for item in data['floors']:
        floor = Floor(building=item['building'], number=item['number'], name=item['name'], plan_url=item['plan_url'])
        session.add(floor)
        floors[(item['building'], item['number'])] = floor

    await session.flush()

    rooms = {}
    for item in data['rooms']:
        room = Room(
            floor_id=floors[(item['building'], item['floor'])].id,
            room_type_id=room_types[item['type']].id,
            number=item['number'],
            name=item['name'],
            area=item['area'],
            capacity=item['capacity']
        )
        session.add(room)
        rooms[item['number']] = room

    await session.flush()

    nodes = {}
    for item in data['nodes']:
        room_id = None
        if item['room'] is not None:
            room_id = rooms[item['room']].id

        node = GraphNode(
            code=item['code'],
            floor_id=floors[(item['building'], item['floor'])].id,
            room_id=room_id,
            x=item['x'],
            y=item['y'],
            description=item['description']
        )
        session.add(node)
        nodes[item['code']] = node

    await session.flush()

    for item in data['edges']:
        edge = GraphEdge(
            node_from_id=nodes[item['from']].id,
            node_to_id=nodes[item['to']].id,
            length_meters=item['length'],
            edge_type=item['type']
        )
        session.add(edge)

    await session.commit()


async def main():
    with open('data.json', encoding='utf-8') as file:
        data = json.load(file)

    async with SessionLocal() as session:
        await import_data(session=session, data=data)

    print(f"Imported: {len(data['floors'])} floors, {len(data['rooms'])} rooms, {len(data['nodes'])} nodes, {len(data['edges'])} edges")


if __name__ == '__main__':
    asyncio.run(main())
