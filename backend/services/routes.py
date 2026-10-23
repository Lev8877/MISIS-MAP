from fastapi import HTTPException

from fake_data import NODES, EDGES

from graph import Graph

from services.rooms import get_room


def build_graph():
    graph = Graph()

    for node in NODES:
        graph.add_node(node['id'])

    for edge in EDGES:
        graph.add_edge(edge['from_node_id'], edge['to_node_id'], edge['length'])

    return graph


async def get_route(from_room_id: int, to_room_id: int):
    from_room = await get_room(from_room_id)
    to_room = await get_room(to_room_id)

    graph = build_graph()
    result = graph.shortest_path(from_room['node_id'], to_room['node_id'])

    if result is None:
        raise HTTPException(status_code=404, detail='Route is not found')

    path, distance = result
    nodes_by_id = {node['id']: node for node in NODES}

    return {
        'distance': distance,
        'nodes': [nodes_by_id[node_id] for node_id in path]
    }
