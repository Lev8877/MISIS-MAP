from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from fastapi import HTTPException

from models.graph_nodes import GraphNode
from models.graph_edges import GraphEdge

from graph import Graph


async def get_room_node(session: AsyncSession, room_id: int):
    result = await session.execute(select(GraphNode).where(GraphNode.room_id == room_id))
    node = result.scalar_one_or_none()

    if node is None:
        raise HTTPException(status_code=404, detail='Room is not found on the map')

    return node


async def get_route(session: AsyncSession, from_room_id: int, to_room_id: int):
    from_node = await get_room_node(session=session, room_id=from_room_id)
    to_node = await get_room_node(session=session, room_id=to_room_id)

    nodes_result = await session.execute(select(GraphNode))
    nodes = nodes_result.scalars().all()

    edges_result = await session.execute(select(GraphEdge))
    edges = edges_result.scalars().all()

    graph = Graph()

    for node in nodes:
        graph.add_node(node.id)

    for edge in edges:
        graph.add_edge(edge.node_from_id, edge.node_to_id, edge.length_meters)

    result = graph.shortest_path(from_node.id, to_node.id)

    if result is None:
        raise HTTPException(status_code=404, detail='Route is not found')

    path, distance = result
    nodes_by_id = {node.id: node for node in nodes}

    return {
        'distance': distance,
        'nodes': [nodes_by_id[node_id] for node_id in path]
    }
