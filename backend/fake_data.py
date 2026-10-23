FLOORS = [
    {'id': 1, 'building': 'Б', 'number': 1, 'plan_url': 'plans/b_1.svg'},
    {'id': 2, 'building': 'Б', 'number': 2, 'plan_url': 'plans/b_2.svg'},
]

ROOMS = [
    {'id': 1, 'number': 'Б-101', 'name': 'Аудитория', 'type': 'Аудитория', 'floor_id': 1, 'node_id': 1},
    {'id': 2, 'number': 'Б-102', 'name': 'Компьютерный класс', 'type': 'Аудитория', 'floor_id': 1, 'node_id': 2},
    {'id': 3, 'number': 'Б-103', 'name': 'Буфет', 'type': 'Буфет', 'floor_id': 1, 'node_id': 3},
    {'id': 4, 'number': 'Б-104', 'name': 'Туалет', 'type': 'Туалет', 'floor_id': 1, 'node_id': 4},
    {'id': 5, 'number': 'Б-201', 'name': 'Лекционная аудитория', 'type': 'Аудитория', 'floor_id': 2, 'node_id': 14},
    {'id': 6, 'number': 'Б-202', 'name': 'Лаборатория физики', 'type': 'Лаборатория', 'floor_id': 2, 'node_id': 15},
    {'id': 7, 'number': 'Б-203', 'name': 'Деканат', 'type': 'Кабинет', 'floor_id': 2, 'node_id': 16},
]

NODES = [
    {'id': 1, 'floor_id': 1, 'x': 100, 'y': 250},
    {'id': 2, 'floor_id': 1, 'x': 300, 'y': 250},
    {'id': 3, 'floor_id': 1, 'x': 500, 'y': 350},
    {'id': 4, 'floor_id': 1, 'x': 700, 'y': 350},
    {'id': 5, 'floor_id': 1, 'x': 100, 'y': 300},
    {'id': 6, 'floor_id': 1, 'x': 300, 'y': 300},
    {'id': 7, 'floor_id': 1, 'x': 500, 'y': 300},
    {'id': 8, 'floor_id': 1, 'x': 700, 'y': 300},
    {'id': 9, 'floor_id': 1, 'x': 800, 'y': 300},
    {'id': 10, 'floor_id': 2, 'x': 800, 'y': 300},
    {'id': 11, 'floor_id': 2, 'x': 700, 'y': 300},
    {'id': 12, 'floor_id': 2, 'x': 400, 'y': 300},
    {'id': 13, 'floor_id': 2, 'x': 100, 'y': 300},
    {'id': 14, 'floor_id': 2, 'x': 100, 'y': 250},
    {'id': 15, 'floor_id': 2, 'x': 400, 'y': 350},
    {'id': 16, 'floor_id': 2, 'x': 700, 'y': 250},
]

EDGES = [
    {'from_node_id': 1, 'to_node_id': 5, 'length': 5},
    {'from_node_id': 2, 'to_node_id': 6, 'length': 5},
    {'from_node_id': 3, 'to_node_id': 7, 'length': 5},
    {'from_node_id': 4, 'to_node_id': 8, 'length': 5},
    {'from_node_id': 5, 'to_node_id': 6, 'length': 20},
    {'from_node_id': 6, 'to_node_id': 7, 'length': 20},
    {'from_node_id': 7, 'to_node_id': 8, 'length': 20},
    {'from_node_id': 8, 'to_node_id': 9, 'length': 10},
    {'from_node_id': 9, 'to_node_id': 10, 'length': 15},
    {'from_node_id': 10, 'to_node_id': 11, 'length': 10},
    {'from_node_id': 11, 'to_node_id': 12, 'length': 30},
    {'from_node_id': 12, 'to_node_id': 13, 'length': 30},
    {'from_node_id': 13, 'to_node_id': 14, 'length': 5},
    {'from_node_id': 12, 'to_node_id': 15, 'length': 5},
    {'from_node_id': 11, 'to_node_id': 16, 'length': 5},
]
