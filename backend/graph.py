import heapq


class Graph:
    def __init__(self):
        self.neighbors = {}

    def add_node(self, node_id: int):
        self.neighbors[node_id] = []

    def add_edge(self, from_node_id: int, to_node_id: int, length: float):
        self.neighbors[from_node_id].append((to_node_id, length))
        self.neighbors[to_node_id].append((from_node_id, length))

    def shortest_path(self, start_node_id: int, end_node_id: int):
        distances = {start_node_id: 0}
        previous = {}
        visited = set()
        queue = [(0, start_node_id)]

        while queue:
            distance, node_id = heapq.heappop(queue)

            if node_id in visited:
                continue
            visited.add(node_id)

            if node_id == end_node_id:
                break

            for neighbor_id, length in self.neighbors[node_id]:
                new_distance = distance + length

                if neighbor_id not in distances or new_distance < distances[neighbor_id]:
                    distances[neighbor_id] = new_distance
                    previous[neighbor_id] = node_id
                    heapq.heappush(queue, (new_distance, neighbor_id))

        if end_node_id not in distances:
            return None

        path = [end_node_id]
        while path[-1] != start_node_id:
            path.append(previous[path[-1]])
        path.reverse()

        return path, distances[end_node_id]
