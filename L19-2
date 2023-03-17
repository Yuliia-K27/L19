import heapq

def shortest_path(graph, start, end):
    distances = {node: float('inf') for node in graph.nodes()}
    distances[start] = 0
    queue = [(0, start)]
    visited = set()

    while queue:
        (current_distance, current_node) = heapq.heappop(queue)
        if current_node == end:
            path = []
            while current_node != start:
                path.insert(0, current_node)
                current_node = previous[current_node]
            path.insert(0, start)
            return path, current_distance

        visited.add(current_node)
        for neighbor, distance in graph[current_node].items():
            if neighbor in visited:
                continue
            new_distance = current_distance + distance['weight']
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current_node
                heapq.heappush(queue, (new_distance, neighbor))

    return "There is no path between " + start + " and " + end
    
start = 'Lviv'
end = 'Kyiv'
path, distance = shortest_path(G, start, end)
print("Shortest path between", start, "and", end, "is", path)
print("Distance:", distance)
