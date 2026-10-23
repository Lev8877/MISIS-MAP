def test_get_floors(client):
    response = client.get('/floors')

    assert response.status_code == 200, response.json()
    assert len(response.json()['floors']) == 2


def test_get_floor_not_found(client):
    response = client.get('/floors/9999')

    assert response.status_code == 404, response.json()
