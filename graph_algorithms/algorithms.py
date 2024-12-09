import heapq

class GraphAlgorithms:
    @staticmethod
    def dijkstra(graph, start):
        distances = {node: float('inf') for node in graph.adjacency_list}
        distances[start] = 0
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in graph.get_neighbors(current_node):
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances
