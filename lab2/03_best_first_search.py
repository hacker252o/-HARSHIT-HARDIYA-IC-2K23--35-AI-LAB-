import heapq

graph = {
    "A": [("B", 1), ("C", 1)],
    "B": [("D", 1), ("E", 1)],
    "C": [("F", 1)],
    "D": [],
    "E": [("G", 1)],
    "F": [("G", 1)],
    "G": []
}
heuristic = {"A": 5, "B": 4, "C": 2, "D": 4, "E": 2, "F": 1, "G": 0}

def best_first(start, goal):
    frontier = [(heuristic[start], start)]
    visited = set()
    parent = {start: None}

    while frontier:
        _, node = heapq.heappop(frontier)
        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1]

        for neighbour, _ in graph[node]:
            if neighbour not in visited and neighbour not in parent:
                parent[neighbour] = node
                heapq.heappush(frontier, (heuristic[neighbour], neighbour))
    return None

print("Path:", best_first("A", "G"))
