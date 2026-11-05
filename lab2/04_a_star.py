import heapq

graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("D", 2), ("E", 5)],
    "C": [("E", 1)],
    "D": [("G", 5)],
    "E": [("G", 2)],
    "G": []
}
h = {"A": 5, "B": 4, "C": 3, "D": 4, "E": 2, "G": 0}

def a_star(start, goal):
    open_list = [(h[start], 0, start)]
    parent = {start: None}
    cost = {start: 0}

    while open_list:
        _, current_cost, node = heapq.heappop(open_list)

        if node == goal:
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1], current_cost

        if current_cost != cost[node]:
            continue

        for neighbour, edge_cost in graph[node]:
            new_cost = current_cost + edge_cost
            if new_cost < cost.get(neighbour, float("inf")):
                cost[neighbour] = new_cost
                parent[neighbour] = node
                heapq.heappush(open_list, (new_cost + h[neighbour],
                                           new_cost, neighbour))
    return None, float("inf")

path, total = a_star("A", "G")
print("Best path:", path)
print("Total cost:", total)
