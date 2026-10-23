from graph import Graph


def test_route_same_floor(client):
    response = client.get('/route', params={'from_room_id': 1, 'to_room_id': 3})

    assert response.status_code == 200, response.json()
    assert response.json()['distance'] == 50
    assert [node['id'] for node in response.json()['nodes']] == [1, 5, 6, 7, 3]


def test_route_other_floor(client):
    response = client.get('/route', params={'from_room_id': 1, 'to_room_id': 6})

    assert response.status_code == 200, response.json()
    assert response.json()['distance'] == 135
    assert [node['id'] for node in response.json()['nodes']] == [1, 5, 6, 7, 8, 9, 10, 11, 12, 15]


def test_route_room_not_found(client):
    response = client.get('/route', params={'from_room_id': 1, 'to_room_id': 9999})

    assert response.status_code == 404, response.json()


def test_shortest_path_chooses_detour():
    graph = Graph()
    for node_id in [1, 2, 3]:
        graph.add_node(node_id)
    graph.add_edge(1, 3, 10)
    graph.add_edge(1, 2, 3)
    graph.add_edge(2, 3, 4)

    assert graph.shortest_path(1, 3) == ([1, 2, 3], 7)


def test_shortest_path_without_route():
    graph = Graph()
    graph.add_node(1)
    graph.add_node(2)

    assert graph.shortest_path(1, 2) is None
