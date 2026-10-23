def test_get_rooms_by_floor(client):
    response = client.get('/rooms', params={'floor_id': 2})

    assert response.status_code == 200, response.json()
    numbers = [room['number'] for room in response.json()['rooms']]
    assert numbers == ['Б-201', 'Б-202', 'Б-203']


def test_get_room_not_found(client):
    response = client.get('/rooms/9999')

    assert response.status_code == 404, response.json()


def test_search_by_name(client):
    response = client.get('/search', params={'query': 'буфет'})

    assert response.status_code == 200, response.json()
    assert response.json()['rooms'][0]['number'] == 'Б-103'


def test_search_by_number(client):
    response = client.get('/search', params={'query': 'б-20'})

    assert response.status_code == 200, response.json()
    assert len(response.json()['rooms']) == 3
